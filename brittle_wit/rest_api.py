import json
import re
import textwrap
import warnings

from collections import OrderedDict, defaultdict
from inspect import Parameter, Signature
from itertools import tee, chain

from brittle_wit.rate_limit import RateLimit
from brittle_wit import TwitterRequest

SLUGS_RE = re.compile(r":[A-Za-z_0-9]+")
SLUG_POSTFIX_RE = re.compile(r"^.*?(:[A-Za-z_0-9]+)$")
SLUG_INFIX_RE = re.compile(r"""^(?:[A-Za-z]*/)?
                               ([A-Za-z0-9_]+)/
                               (\:[A-Za-z_0-9]+)/
                               (.*)$""",
                           re.X)

# Python cannot represent all Twitter API parameter names. They have invalid
# symbols. The following two dictionaries remap these names.
NAME_TO_PY_NAME = {"attribute:street_address": "attribute_street_address",
                   "media[]": "media_arr"}
PY_NAME_TO_NAME = {v: k for k, v in NAME_TO_PY_NAME.items()}


class NSSentinel:
    # XXX: There has to be an existing solution for this.
    def __repr__(self):
        return 'NOT_SPECIFIED'

NOT_SPECIFIED = NSSentinel()


def _generate_signature(api_def):
    """
    Generate a Python function signature from an api definition.

    This object enforces required and optional parameters. It also gives
    readable documentation and tab-completion. It's mostly meant as a
    guide though. It won't enforce strict correctness because the Twitter
    API has requirements like either A or B. In these cases, I mark both A
    and B as optional. If you don't specify one of them, Twitter will balk.
    But, it's reasonably obvious when this occurs, so it's not worth the
    added library complexity.
    """
    params = []

    for name, (optionality, _) in api_def['params'].items():
        name = NAME_TO_PY_NAME.get(name, name)

        if optionality == 'REQUIRED':
            p = Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        else:
            p = Parameter(name, Parameter.KEYWORD_ONLY, default=NOT_SPECIFIED)

        params.append(p)

    return Signature(params)


def _generate_doc_str(api_def, line_width=70, indent_width=4):
    lines = textwrap.wrap(api_def['desc'], line_width) + [""]

    for k, (optionality, desc) in api_def['params'].items():
        lines.append(k + ":\n")

        body = "({}) {}".format(optionality, desc)
        for paragraph in body.splitlines():
            wrapped = textwrap.wrap(paragraph,
                                    line_width - indent_width,
                                    replace_whitespace=False)
            for line in wrapped:
                lines.append(" "*indent_width + line)
            lines.append("")

        lines.append('')

    return "\n".join(lines) + "\n"


def _update_params_ordering_required_first(api_def):
    """
    Updates the api_def IN PLACE, ensuring required params come first.

    The order of each parameter in `rest_api.json` is significant, matching
    the order in the API documentation. However, I can see a situation in
    which a required parameter comes after an optional one. That's fine for
    the documentation, but it's not okay for a Python signature.
    """
    t1, t2 = tee(api_def['params'].items())
    kv_pairs = chain((p for p in t1 if p[1][0] == 'REQUIRED'),
                     (p for p in t2 if p[1][0] != 'REQUIRED'))
    api_def['params'] = OrderedDict(kv_pairs)


def _bind_sig(signature, *args, **kwargs):
    return {PY_NAME_TO_NAME.get(k, k): v
            for k, v in signature.bind(*args, **kwargs).arguments.items()
            if v is not NOT_SPECIFIED}


def _slugged_pythonic_string(url):
    """
    Process a slugged URL

    :param url: the raw API endpoint
    :return: None if this is not a slugged url, otherwise a tuple of the
        python string for format-based interpolation and the slug parameter
        names
    """
    slugged_str = ""

    matches = list(SLUGS_RE.finditer(url))
    if not matches:
        return None

    last_idx = 0
    slug_params = []
    for m in matches:
        j, k = m.start(), m.end()
        slugged_str += url[last_idx:j]
        last_idx = k

        slug_param = m.group(0)[1:]
        slugged_str += "{" + slug_param + "}"
        slug_params.append(slug_param)

    return slugged_str, slug_params


def _generate_slugger(slugged_str, slug_params):
    """
    Create function that pops the slug_params and injects them into the URL.

    Note: The transform function takes the params dictionary, not the expanded
        **kwargs. The params dictionary is modified in place via pop!
    """
    def _slug_transform(params):
        slug_dict = {k: params.pop(k) for k in slug_params}
        return slugged_str.format(**slug_dict)
    return _slug_transform


def _url_to_func_name(service, family, method):
    # Special cases first.
    if service == "account/settings" and method == 'POST':
        return "update_settings"  # There is a 'GET' version

    m = SLUG_POSTFIX_RE.match(service)
    if m:
        postfix = m.group(1)
        service = service.replace(postfix, "by_" + postfix[1:])
    else:
        m = SLUG_INFIX_RE.match(service)
        if m:
            service = m.group(3) + "_by_" + m.group(1) + '_' + m.group(2)[1:]

    f_name = service.replace("/", "_")
    f_name = f_name.replace(family + '_', '')

    return f_name


def generate_api_request_builder_func(api_def):
    _update_params_ordering_required_first(api_def)

    f_name = _url_to_func_name(api_def['service'],
                               api_def['family'],
                               api_def['method'])

    signature = _generate_signature(api_def)

    def f(*args, **kwargs):
        # MAGIC WARNING
        binding = _bind_sig(signature, *args, **kwargs)
        return TwitterRequest(api_def['method'].upper(),
                              api_def['url'],
                              api_def['family'].upper(),
                              api_def['service'].upper(),
                              **binding)
    f.__name__ = f_name
    f.__doc__ = _generate_doc_str(api_def)
    f.__signature__ = signature

    return f


class TwitterAPI:
    def __init__(self, api_defs,
                 update_twitter_request_doc_urls=True,
                 update_rate_limit_defaults=True):

        if update_twitter_request_doc_urls:
            DOC_URLS = TwitterRequest.DOC_URLS

        if update_rate_limit_defaults:
            CLIENT_LIMITS = RateLimit.CLIENT_LIMITS
            APP_LIMITS = RateLimit.APP_LIMITS

        # Each API function belongs to a family.
        families = defaultdict(dict)

        # Build each API function, adding it to its family's dictionary.
        for api_def in api_defs:
            if 'deprecated' in api_def['service']:
                continue  # Nudge!

            f = generate_api_request_builder_func(api_def)
            if f.__name__ in families[api_def['family']]:
                warnings.warn("Conflicting on: " + api_def['reference_url'])
            if not f.__name__.isidentifier():
                fmt = "Bad Name: {} for {}"
                warnings.warn(fmt.format(f.__name__, api_def['reference_url']))
            families[api_def['family']][f.__name__] = f

            if update_twitter_request_doc_urls:
                DOC_URLS[api_def['url']] = api_def['reference_url']

            if update_rate_limit_defaults and api_def['rate_limited']:
                limits = api_def.get('limits')
                if limits:
                    if 'app' in limits:
                        APP_LIMITS[api_def['service']] = int(limits['app'])
                    if 'user' in limits:
                        CLIENT_LIMITS[api_def['service']] = int(limits['user'])

        # Make each family dictionary of api functions accessible via dot
        # accessor. That is, mock module-style access, without modules. There
        # are lots of ways to do this. But, I think creating a new type for
        # each family is the simplest. The str and repr encodings are easy to
        # grok from the REPL. And, the user is free to add end remove methods
        # to each family at will.
        for family_name, obj_dict in families.items():
            self.__dict__[family_name] = type(family_name, (object,), obj_dict)


def build_api(json_file):
    # The parameter ordering has meaning. It's copied from Twitter's API docs.
    decorder = json.JSONDecoder(object_pairs_hook=OrderedDict)
    with open(json_file) as fp:
        defs = decorder.decode(fp.read())
    return TwitterAPI(defs)

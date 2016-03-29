import json
import textwrap

from inspect import Parameter, Signature
from brittle_wit.twitter_request import TwitterRequest


NAME_TO_PY_NAME = {"attribute:street_address": "attribute_street_address",
                   "media[]": "media_arr"}
PY_NAME_TO_NAME = {v: k for k, v in NAME_TO_PY_NAME.items()}


class NSSentinel:
    # XXX: There has to be an existing solution for this.
    def __repr__(self):
        return 'NOT_SPECIFIED'

NOT_SPECIFIED = NSSentinel()


def _param_key_f(p):
    return 0 if p[1][0] == 'REQUIRED' else 1


def generate_signature(api_def):
    """
    Generate a Python function signature from an api definition.

    This object enforces required and optional parameters. It also gives
    readable documentation and tab-completion. It's mostly meant as a
    guide though. It won't enforce strict correctness because the Twitter
    API has requirements like either A or B. In these cases, I mark both A
    and B as optional. If you don't specify one of them, Twitter will balk.
    But, it's reasonably obvious when this occurs, so it's not worth the
    added library complexity.

    Note: As a Hack,
    """
    params = []

    # Ensure required params come first.
    param_defs = sorted(api_def['params'].items(), key=_param_key_f)

    for name, (optionality, _) in param_defs:
        name = NAME_TO_PY_NAME.get(name, name)

        if optionality == 'REQUIRED':
            p = Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        else:
            p = Parameter(name, Parameter.KEYWORD_ONLY, default=NOT_SPECIFIED)

        params.append(p)

    return Signature(params)


def supports_cursor(api_def):

    for param in api_def['params']:
        if param == 'cursor':
            return True
    return False


def generate_doc_str(api_def):
    lines = textwrap.wrap(api_def['desc'], 70) + [""]

    # Ensure required params come first.
    param_defs = sorted(api_def['params'].items(), key=_param_key_f)
    for k, (optionality, desc) in param_defs:
        lines.append(k + ":\n")

        body = '({}) {}'.format(optionality, desc)
        for paragraph in body.splitlines():
            wrapped = textwrap.wrap(paragraph,
                                    70 - 4,
                                    replace_whitespace=False)
            for line in wrapped:
                lines.append("    " + line)
            lines.append("")

        lines.append('')

    return "\n".join(lines) + "\n"


class RestFamily:
    def __init__(self, name):
        self._name = name

    def _add(self, definition):
        f_name = definition['url'].split("1.1/")[-1]
        f_name = f_name.replace("/", "_").replace(".json", "")
        f_name = f_name.replace(definition['family'] + '_', '')

        if hasattr(self, f_name):
            print(f_name)

        def f(*args, **kwargs):
            # MAGIC WARNING
            binding = {PY_NAME_TO_NAME.get(k, k): v
                       for k, v in sig.bind(*args, **kwargs).arguments.items()
                       if v is not NOT_SPECIFIED}
            return TwitterRequest(definition['method'],
                                  definition['url'],
                                  definition['family'],
                                  supports_cursor=supports_cursor(definition),
                                  **binding)
        f.__name__ = f_name
        f.__doc__ = generate_doc_str(definition)
        f.__signature__ = sig = generate_signature(definition)

        self.__dict__[f_name] = f


class RestAPI:
    def __init__(self, definitions):
        for d in definitions:
            family_name = d['family']
            if not hasattr(self, family_name):
                self.__dict__[family_name] = RestFamily(family_name)

            self.__dict__[family_name]._add(d)


def build_api(json_file):
    with open(json_file) as fp:
        defs = json.load(fp)
    return RestAPI(defs)



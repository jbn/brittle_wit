import re
from vaquero import transformations as t
from lxml.html import fromstring as _fromstring


def prepare(src, dst):
    # Copy non-private keys to the destination.
    for k in src:
        if not k.startswith('_'):
            dst[k] = src[k]

    # Convert the html to a lxml node
    src['doc'] = _fromstring(src['_raw_html'])
    del src['_raw_html']


MISSING_URLS = {'get-media-upload-status':
                    "https://upload.twitter.com/1.1/media/upload.json",
                'post-media-upload-finalize':
                    "https://upload.twitter.com/1.1/media/upload.json",
                'post-batch-accounts-account-id-line-items':
                    "https://ads-api.twitter.com/1/batch/accounts/:account_id/line_items",
                'post-batch-accounts-account-id-campaigns':
                    "https://ads-api.twitter.com/1/batch/accounts/:account_id/campaigns"}


def _match_first(node, *css_selectors):
    for selector in css_selectors:
        m = node.cssselect(selector)
        if m:
            return m[0]
    return None


def extract_and_verify_basic_info(src, dst):
    doc = src['doc']
    snippet = doc.cssselect("div[itemprop='articleBody'] > div.section")[0]
    dst['service'] = snippet.attrib['id']

    method, *path = snippet.cssselect('h1')[0].text.split(" ")
    assert dst['method'] == method
    dst['path'] = " ".join(path)
    dst['desc'] = snippet.cssselect("p")[0].text

    try:
        url_section = snippet.cssselect("#resource-url")[0]
        m = _match_first(url_section,
                         'span.pre', 'code.docutils', 'p > em', 'p > cite')

        url = (m if m is not None else url_section).text_content().strip()
        dst['url'] = url
    except IndexError:
        patch_url = MISSING_URLS.get(dst['service'])
        if patch_url:
            dst['url'] = patch_url
        else:
            raise


RESOURCE_INFO_RENAMES = {'response_formats': 'resp_format',
                         'requires_authentication': 'authentication_required'}


def extract_resource_information(src, dst):
    doc = src['doc']
    snippet = doc.cssselect('div#resource-information tr')
    d = {}
    for row in snippet:
        k, v = [item.text_content() for item in row.cssselect('td')]
        d[k] = v
    t.pythonize_ks(d)
    t.rename_ks(d, RESOURCE_INFO_RENAMES)
    for k, v in d.items():
        if k == 'resp_format':
            src[k] = v
        else:
            dst[k] = v


def rate_limited_to_boolean(src, dst):
    dst['rate_limited'] = dst.get('rate_limited') == 'Yes'


def authentication_required_to_boolean(src, dst):
    b = dst.get('authentication_required', "No") != 'No'
    dst['authentication_required'] = b


FORMAT_MAPPING = {'JSON': 'JSON', "204 - No Content": None}


def extract_resp_formats(src, dst):
    if 'resp_format' in src:
        dst['resp_format'] = FORMAT_MAPPING[src['resp_format']]
    else:
        dst['resp_format'] = None


LIMIT_MAP = {'requests_15_min_window_app_auth': 'app',
             'requests_15_min_window_per_app': 'app',
             'requests_15_min_window_user_auth': 'user'}


def extract_limits(src, dst):
    dst['limits'] = {}

    for k, v in dst.items():
        if not k.startswith('requests'):
            continue

        v = v.strip()

        # Special case.
        if v == '15/user and 750/app':
            dst['limits']['user'] = 15
            dst['limits']['app'] = 750
        elif v == 'Refer to your existing rate limit agreements.':
            service = dst['service']
            assert service == 'post-direct-messages-events-new-message-create'
        else:
            k = LIMIT_MAP[k]
            assert k not in dst['limits']
            dst['limits'][k] = int(v)


def _fix_param_desc(d):
    s = d.get('description')
    if s is None:
        return
    s = s.replace(" . ", ". ").replace(" , ", ", ")
    if s.endswith(" ."):
        s = s[:-2] + "."
    d['description'] = s


def _fix_param_default(d):
    default = d.get('default_value')
    if default is not None and default == '':
        del d['default_value']


TYPE_REGEXP = re.compile(r"([\d\w\_]+)\s+Type: (.*)$")


def _fix_param_type(d):
    m = TYPE_REGEXP.match(d['name'])
    if not m:
        return
    d['name'] = m.group(1)
    d['type'] = m.group(2)


VALID_PARAM_KS = {'name', 'default_value', 'example', 'required',
                  'description', 'constraints'}


def _extract_header_from_rows(rows):
    top_row = rows[0]
    items = [td.text_content() or '' for td in top_row.cssselect('td')]
    if not items:
        items = [td.text_content() or '' for td in top_row.cssselect('th')]
        if not items:
            return None

    t.sstrip_all(items)

    ks = [t.pythonize_identifier(k) for k in items]
    return tuple(ks)


def _tail(items):
    head_consumed = False
    for item in items:
        if not head_consumed:
            head_consumed = True
        else:
            yield item


SPECIAL_NAMES = {'follow see note*': 'follow',
                 'track see note*': 'track',
                 'user_ids DEPRECATED': 'user_ids',
                 'locations see note*': 'locations'}


def _extract_param_rows_normal(header, rows):
    data = []

    for tr in _tail(rows):
        items = [td.text_content() or '' for td in tr.cssselect('td')]
        t.sstrip_all(items)

        d = dict(zip(header, items))

        _fix_param_desc(d)
        _fix_param_default(d)
        _fix_param_type(d)

        # Special cases
        d['name'] = SPECIAL_NAMES.get(d['name'], d['name'])

        data.append(d)

    return data


EMBEDDED_PARAM_RE = re.compile("([\w\d\_]+)\s+\(([^\)]+)\)")


def _extract_param_rows_no_header(rows):
    data = []

    for tr in rows:
        items = [td.text_content() or '' for td in tr.cssselect('td')]
        t.sstrip_all(items)
        k, desc = items

        d = {'desc': desc}
        _fix_param_desc(d)

        name, required = EMBEDDED_PARAM_RE.match(k).groups()
        d['name'] = name
        d['required'] = required
        data.append(d)

    return data


def extract_params(src, dst):
    doc = src['doc']
    rows = doc.cssselect('#parameters > table tr')

    if not rows:
        return

    header, data = _extract_header_from_rows(rows), None

    rows = doc.cssselect('#parameters > table tr')
    if set(header).issubset(VALID_PARAM_KS):
        data = _extract_param_rows_normal(header, rows)
    elif len(header) == 2:
        data = _extract_param_rows_no_header(rows)
    else:
        dst['_bad_ks'] = header

    if data:
        dst['params'] = data


def fix_edge_case_params(src, dst):
    for param in dst.get('params', []):
        parts = param['name'].split(' ')
        if len(parts) == 1:
            continue
        param['name'] = parts[0]
        param['required'] = parts[1]


REQUIRED_VALUES = {'True', 'requied', 'required'}


def normalize_required_params(src, dst):
    for param in dst.get('params', []):
        param['required'] = param.get('required') in REQUIRED_VALUES


def extract_example_request(src, dst):
    doc = src['doc']
    example_req = doc.cssselect('#example-request > p')
    if example_req:
        dst['example_request'] = example_req[0].text_content()


def extract_example_response(src, dst):
    doc = src['doc']
    code_sections = doc.cssselect('#example-response > div.code')
    if code_sections:
        dst['example_response'] = code_sections[0].text_content()


def extract_family(_, dst):
    path = dst['path']

    if path.startswith('/1/'):  # Ads
        path = path.replace("/1/", "")

    sub_family = path.split('/')[0]
    dst['family'] = dst['group'] + ":" + sub_family
    assert sub_family


def fix_path(_, dst):
    if dst['path'].startswith('/'):
        dst['path'] = dst['path'][1:]


def update_for_slugs(_, dst):
    dst['slugs'], path = [], dst['path']

    if ':' not in path:
        return

    url = dst['url']

    if 'params' not in dst:
        dst['params'] = []
    known_params = {param['name'] for param in dst['params']}

    parts = path.split("/")
    slugs = [s for s in parts if s.startswith(':')]

    # Order so none can be a prefix of the next.
    for _, slug in reversed(sorted((len(slug), slug) for slug in slugs)):
        k = slug[1:]
        url = url.replace(slug, "{" + k + "}")
        dst['slugs'].append(k)

        if k not in known_params:
            dst['params'].append({'name': k, 'required': True})

    dst['url'] = url


VALID_GROUPS = {'ads', 'rest', 'streaming', 'webhooks'}

VALID_FAMILES = {'ads:accounts',
                 'ads:batch',
                 'ads:bidding_rules',
                 'ads:conversion_attribution',
                 'ads:conversion_event',
                 'ads:iab_categories',
                 'ads:insights',
                 'ads:line_items',
                 'ads:stats',
                 'ads:tailored_audience_memberships',
                 'ads:targeting_criteria',
                 'rest:account',
                 'rest:application',
                 'rest:blocks',
                 'rest:collections',
                 'rest:direct_messages',
                 'rest:favorites',
                 'rest:followers',
                 'rest:friends',
                 'rest:friendships',
                 'rest:geo',
                 'rest:help',
                 'rest:lists',
                 'rest:media',
                 'rest:mutes',
                 'rest:saved_searches',
                 'rest:search',
                 'rest:statuses',
                 'rest:trends',
                 'rest:users',
                 'streaming:c',
                 'streaming:site',
                 'streaming:statuses',
                 'streaming:user',
                 'webhooks:account_activity'}


VALIDATION_SPEC = {
    'authentication_required': ({True, False}, False),
    'desc': (None, None),
    'family': (VALID_FAMILES, None),
    'group': (VALID_GROUPS, None),
    'method': ({'GET', 'POST', 'DELETE'}, 'GET'),
    'resp_format': ({'JSON', None}, 'JSON'),
    'rate_limited': ({True, False}, True),
    'path': (None, None),
    'url': (None, None),
    'reference_url': (None, None)
}


def validate(_, dst):
    for k, (valid_set, default) in VALIDATION_SPEC.items():
        if k not in dst:
            if default is not None:
                dst[k] = default
            else:
                assert False, "Missing and no default on {}".format(k)
        elif valid_set is not None:
            assert dst[k] in valid_set, dst[k]


PARAM_VALIDATION_SPEC = {
    'name': (None, None),
    'required': ({True, False}, None)
}


def validate_params(_, dst):
    if 'params' not in dst:
        dst['params'] = []
        return

    for param in dst['params']:
        for k, (valid_set, default) in PARAM_VALIDATION_SPEC.items():
            if k not in param:
                if default is not None:
                    param[k] = default
                else:
                    assert False, "Missing and no default on {}".format(k)
            elif valid_set is not None:
                assert param[k] in valid_set, param[k]

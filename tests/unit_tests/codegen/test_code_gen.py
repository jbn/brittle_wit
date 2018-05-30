import os
import pytest
import shutil
from tests.helpers import FIXTURES_DIR, load_fixture_txt, load_fixture_json
from api_gen.api_code_gen import (pep8_join,
                                  _generate_param_tokens,
                                  generate_source,
                                  _param_name_translations,
                                  _generate_param_doc,
                                  _generate_doc_str,
                                  _generate_def_line,
                                  _generate_binding,
                                  _generate_url_block,
                                  generate_modules,
                                  _generate_func_name)


def test_pep8_join():
    expected = load_fixture_txt("pep8_join.txt").rstrip()
    sent = "this is a sequence of words some are reallyreallyreallylong"
    tokens = sent.split(" ") * 3
    res = pep8_join(tokens, ", ", init_indent='--', next_indent='::')
    assert res == expected


def test_param_name_translations():
    example = ["with", "array[]", "for", "simple"]
    expected = dict(zip(example, ["with_", "array", "for_", "simple"]))
    assert _param_name_translations(example) == expected


DEF_LINE_1 = """
def account_media_by_id_and_account_id_via_fake(id, account_id_, *,
                                                count=_ELIDE, sort_by=_ELIDE,
                                                cursor=_ELIDE,
                                                with_deleted=_ELIDE,
                                                account_media_ids=_ELIDE):
""".strip()


def test_generate_def_line():
    example_api_def = {'family': 'ads:accounts',
                       'group': 'ads',
                       'method': 'FAKE',
                       'params': [{'name': 'count', 'required': False},
                                  {'name': 'account_id', 'required': True},
                                  {'name': 'sort_by', 'required': False},
                                  {'name': 'cursor', 'required': False},
                                  {'name': 'with_deleted', 'required': False},
                                  {'name': 'account_media_ids',
                                      'required': False},
                                  {'name': 'id', 'required': True}],
                       'path': 'accounts/:account_id/account_media/:id',
                       'slugs': ['account_id', 'id'],
                       'service': 'get-accounts-account-id-account-media-id'}
    renamings = {'account_id': 'account_id_'}
    res = _generate_def_line(example_api_def, True, **renamings)
    assert res == DEF_LINE_1

    example_api_def = {'family': 'ads:accounts',
                       'group': 'ads',
                       'method': 'FAKE',
                       'params': [],
                       'path': 'accounts/list_all',
                       'slugs': [],
                       'service': 'get-accounts-account-id-account-media-id'}
    res = _generate_def_line(example_api_def)
    assert res == "def list_all():"


def test_generate_param_doc():
    example_def = {'description': ("This is a description line." +
                                   " It should wrap correctly so it is " +
                                   " PEP8 compliant."),
                   'type': 'An Integer'}
    expected = ("    :param id: This is a description line. It should " +
                "wrap correctly so it is\n" +
                "        PEP8 compliant. (An Integer)")
    assert _generate_param_doc(example_def, 'id') == expected
    assert _generate_param_doc({}, 'id') is None


def test_generate_doc_str():
    example_api_def = {'family': 'ads:accounts',
                       'group': 'ads',
                       'desc': "An Example",
                       'method': 'FAKE',
                       'params': [{'name': 'count', 'desc': 'A word'},
                                  {'name': 'account_id', 'desc': 'A word'},
                                  {'name': 'sort_by', 'desc': 'A word'},
                                  {'name': 'cursor', 'desc': 'A word'},
                                  {'name': 'with_deleted',
                                      'desc': 'A word'},
                                  {'name': 'account_media_ids',
                                      'desc': 'A word'},
                                  {'name': 'id', 'desc': 'A word'}],
                       'path': 'accounts/:account_id/account_media/:id',
                       'slugs': ['account_id', 'id'],
                       'service': 'get-accounts-account-id-account-media-id'}
    renamings = {'account_id': 'account_id_'}
    expected = load_fixture_txt("doc_str.txt")

    res = _generate_doc_str(example_api_def, **renamings)
    assert res == expected


def test_generate_binding():
    names = ["with", "array[]", "for", "simple"]
    renamings = _param_name_translations(names)
    assert _generate_binding({'params': {}}) == "    binding = {}"

    api_def = {'params': [{'name': "with"},
                          {'name': "array[]"},
                          {'name': "for"},
                          {'name': "simple"}]}

    expected = ("    binding = {'with': with_, 'array[]': array, " +
                "'for': for_, 'simple': simple}")
    assert _generate_binding(api_def, **renamings) == expected


def test_generate_url_block():
    expected = "    url = 'http://google.com/{id}'"
    res = _generate_url_block({'url': "http://google.com/{id}",
                               'slugs': []})
    assert res == expected

    res = _generate_url_block({'url': "http://google.com/{id}",
                               'slugs': ['id']})
    assert res == expected + "\n    url = url.format(**binding)"


def test_generate_modules():
    tmp_dir = os.path.join(FIXTURES_DIR, "skel")
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    definitions = {'public': [{'family': 'x:dog'}, {'family': 'y:cat'}],
                   'private': [{'family': 'y:octopus'}]}

    generate_modules(tmp_dir, definitions, lambda api_def: '')

    expected_paths = [('public_api', '__init__.py'),
                      ('public_api', 'dog.py'),
                      ('public_api', 'cat.py'),
                      ('private_api', 'octopus.py')]

    for path in expected_paths:
        assert os.path.exists(os.path.join(tmp_dir, *path))

    shutil.rmtree(tmp_dir)


def test_generate_signature_str():
    example = {'params': [{'name': 'a', 'required': True},
                          {'name': 'b', 'required': False},
                          {'name': 'c', 'required': False},
                          {'name': 'd', 'required': True}],
               'slugs': ['d']}
    expected = [("d", None), ("a", None), ("*", None),
                ("b", "_ELIDE"), ("c", "_ELIDE")]
    assert _generate_param_tokens(example) == expected


def test_generate_source():
    example = load_fixture_json("get_block_ids.json")
    src = generate_source(example)
    with open(os.path.join(FIXTURES_DIR, "get_block_ids.src"), "w") as fp:
        fp.write(src)
    assert src == load_fixture_txt("get_block_ids.src")


def test_simple():
    example = {'family': 'rest:blocks',
               'method': 'GET',
               'params': [{'name': 'stringify_ids', 'required': False},
                          {'name': 'cursor', 'required': False}],
               'path': 'blocks/ids',
               'slugs': []}

    assert _generate_func_name(example) == "ids"
    assert _generate_func_name(example, True) == "ids_via_get"


def test_long_simple():
    example = {'family': 'rest:direct_messages',
               'method': 'GET',
               'params': [{'name': 'count', 'required': False},
                          {'name': 'cursor', 'required': False}],
               'path': 'direct_messages/events/list',
               'slugs': []}

    assert _generate_func_name(example) == "events_list"
    assert _generate_func_name(example, True) == "events_list_via_get"


def test_longer_simple():
    example = {'family': 'rest:direct_messages',
               'method': 'GET',
               'params': [{'name': 'id', 'required': True}],
               'path': 'direct_messages/welcome_messages/rules/show',
               'slugs': []}

    assert _generate_func_name(example) == "welcome_messages_rules_show"
    assert _generate_func_name(example, True) == \
        "welcome_messages_rules_show_via_get"


def test_slugged():
    example = {'family': 'rest:saved_searches',
               'method': 'GET',
               'params': [{'name': 'id', 'required': True}],
               'path': 'saved_searches/show/:id',
               'slugs': ['id']}

    assert _generate_func_name(example) == "show_by_id"
    assert _generate_func_name(example, True) == "show_by_id_via_get"


def test_long_slugged():
    example = {'family': 'rest:users',
               'method': 'GET',
               'params': [{'name': 'slug', 'required': True}],
               'path': 'users/suggestions/:slug/members',
               'slugs': ['slug']}

    assert _generate_func_name(example) == "suggestions_members_by_slug"
    assert _generate_func_name(example, True) == \
        "suggestions_members_by_slug_via_get"


def test_longer_slugged():
    example = {'family': 'ads:accounts',
               'method': 'GET',
               'params': [{'name': 'count', 'required': False},
                          {'name': 'account_id', 'required': True},
                          {'name': 'sort_by', 'required': False},
                          {'name': 'cursor', 'required': False},
                          {'name': 'with_deleted', 'required': False},
                          {'name': 'account_media_ids', 'required': False},
                          {'name': 'id', 'required': True}],
               'path': 'accounts/:account_id/account_media/:id',
               'slugs': ['account_id', 'id']}

    assert _generate_func_name(example) == "account_media_by_id_and_account_id"
    assert _generate_func_name(example, True) == \
        "account_media_by_id_and_account_id_via_get"


def test_longer_slugged_weird():
    example = {'family': 'ads:stats',
               'method': 'DELETE',
               'params': [{'name': 'account_id', 'required': True},
                          {'name': 'job_id', 'required': True}],
               'path': '1/stats/jobs/accounts/:account_id/:job_id',
               'slugs': ['account_id', 'job_id']}

    assert _generate_func_name(example) == \
        "jobs_accounts_by_job_id_and_account_id"
    assert _generate_func_name(example, True) == \
        "jobs_accounts_by_job_id_and_account_id_via_delete"


def test_too_long():
    example = {'family': 'ads:stats',
               'method': 'DELETE',
               'params': [{'name': 'account_id', 'required': True},
                          {'name': 'another', 'required': True},
                          {'name': 'job_id', 'required': True}],
               'path': '1/stats/jobs/accounts/:account_id/:job_id/:another',
               'slugs': ['account_id', 'job_id', 'another']}

    with pytest.raises(ValueError):
        _generate_func_name(example)


def test_bad_name():
    example = {'family': 'ads:stats',
               'method': 'GET',
               'params': {},
               'path': 'stats',
               'slugs': []}

    assert _generate_func_name(example) == 'stats'

    example['path'] = "stats/arr[]"
    assert _generate_func_name(example) == 'arr'

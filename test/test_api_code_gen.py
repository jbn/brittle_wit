import os
import shutil
import unittest
from test.helpers import FIXTURES_DIR
from brittle_wit.api_code_gen import (generate_modules,
                                      pep8_join,
                                      _generate_param_tokens,
                                      generate_source,
                                      _param_name_translations,
                                      _generate_def_line,
                                      _generate_func_name)


class TestAPICodeGen(unittest.TestCase):

    def test_pep8_join(self):
        with open(os.path.join(FIXTURES_DIR, "pep8_join.txt")) as fp:
            expected = fp.read().rstrip()
        sent = "this is a sequence of words some are reallyreallyreallylong"
        tokens = sent.split(" ") * 3
        res = pep8_join(tokens, ", ", init_indent='--', next_indent='::')
        self.assertEqual(res, expected)

    DEF_LINE_1 = """
def account_media_by_id_and_account_id_via_fake(id, account_id_, *,
                                                count=ELIDE, sort_by=ELIDE,
                                                cursor=ELIDE,
                                                with_deleted=ELIDE,
                                                account_media_ids=ELIDE):
""".strip()

    def test_generate_def_line(self):
        example_api_def = {'family': 'ads:accounts',
                           'group': 'ads',
                           'method': 'FAKE',
                           'params': [{'name': 'count', 'required': False},
                                      {'name': 'account_id', 'required': True},
                                      {'name': 'sort_by', 'required': False},
                                      {'name': 'cursor', 'required': False},
                                      {'name': 'with_deleted',
                                          'required': False},
                                      {'name': 'account_media_ids',
                                          'required': False},
                                      {'name': 'id', 'required': True}],
                           'path': 'accounts/:account_id/account_media/:id',
                           'slugs': ['account_id', 'id'],
                           'service':
                                'get-accounts-account-id-account-media-id'}
        renamings = {'account_id': 'account_id_'}
        res = _generate_def_line(example_api_def, True, **renamings)
        self.assertEqual(res, TestAPICodeGen.DEF_LINE_1)


    def test_param_name_translations(self):
        example = ["with", "array[]", "for", "simple"]
        expected = dict(zip(example, ["with_", "array", "for_", "simple"]))
        self.assertEqual(_param_name_translations(example), expected)

    def test_generate_modules(self):
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
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, *path)),
                            path)

        shutil.rmtree(tmp_dir)

    def test_generate_signature_str(self):
        example = {'params': [{'name': 'a', 'required': True},
                              {'name': 'b', 'required': False},
                              {'name': 'c', 'required': False},
                              {'name': 'd', 'required': True}],
                   'slugs': ['d']}
        expected = [("d", None), ("a", None), ("*", None),
                    ("b", "ELIDE"), ("c", "ELIDE")]
        self.assertEquals(_generate_param_tokens(example), expected)


class TestsGenerateFuncName(unittest.TestCase):

    def test_simple(self):
        example = {'family': 'rest:blocks',
                   'method': 'GET',
                   'params': [{'name': 'stringify_ids', 'required': False},
                              {'name': 'cursor', 'required': False}],
                   'path': 'blocks/ids',
                   'slugs': []}

        self.assertEqual(_generate_func_name(example), "ids")
        self.assertEqual(_generate_func_name(example, True), "ids_via_get")

    def test_long_simple(self):
        example = {'family': 'rest:direct_messages',
                   'method': 'GET',
                   'params': [{'name': 'count', 'required': False},
                              {'name': 'cursor', 'required': False}],
                   'path': 'direct_messages/events/list',
                   'slugs': []}

        self.assertEqual(_generate_func_name(example), "events_list")
        self.assertEqual(_generate_func_name(example, True),
                         "events_list_via_get")

    def test_longer_simple(self):
        example = {'family': 'rest:direct_messages',
                   'method': 'GET',
                   'params': [{'name': 'id', 'required': True}],
                   'path': 'direct_messages/welcome_messages/rules/show',
                   'slugs': []}

        self.assertEqual(_generate_func_name(example),
                         "welcome_messages_rules_show")
        self.assertEqual(_generate_func_name(example, True),
                         "welcome_messages_rules_show_via_get")

    def test_slugged(self):
        example = {'family': 'rest:saved_searches',
                   'method': 'GET',
                   'params': [{'name': 'id', 'required': True}],
                   'path': 'saved_searches/show/:id',
                   'slugs': ['id']}

        self.assertEqual(_generate_func_name(example),
                         "show_by_id")
        self.assertEqual(_generate_func_name(example, True),
                         "show_by_id_via_get")

    def test_long_slugged(self):
        example = {'family': 'rest:users',
                   'method': 'GET',
                   'params': [{'name': 'slug', 'required': True}],
                   'path': 'users/suggestions/:slug/members',
                   'slugs': ['slug']}

        self.assertEqual(_generate_func_name(example),
                         "suggestions_members_by_slug")
        self.assertEqual(_generate_func_name(example, True),
                         "suggestions_members_by_slug_via_get")

    def test_longer_slugged(self):
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

        self.assertEqual(_generate_func_name(example),
                         "account_media_by_id_and_account_id")
        self.assertEqual(_generate_func_name(example, True),
                         "account_media_by_id_and_account_id_via_get")

    def test_longer_slugged_weird(self):
        example = {'family': 'ads:stats',
                   'method': 'DELETE',
                   'params': [{'name': 'account_id', 'required': True},
                              {'name': 'job_id', 'required': True}],
                   'path': '1/stats/jobs/accounts/:account_id/:job_id',
                   'slugs': ['account_id', 'job_id']}

        self.assertEqual(_generate_func_name(example),
                         "jobs_accounts_by_job_id_and_account_id")
        self.assertEqual(_generate_func_name(example, True),
                         "jobs_accounts_by_job_id_and_account_id_via_delete")

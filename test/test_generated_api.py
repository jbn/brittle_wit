import unittest
import inspect
from importlib import import_module
from brittle_wit_core import TwitterRequest
from brittle_wit import ads_api, rest_api, streaming_api, webhooks_api


def submodules_of(module):
    parent_name, modules = module.__name__, []

    for name in dir(module):
        if name.startswith('__') and name.endswith('__'):
            continue

        if not inspect.ismodule(getattr(module, name)):
            continue

        if name == 'brittle_wit':
            continue

        path = "{}.{}".format(parent_name, name)

        modules.append(import_module(path))

    return modules


def api_calls_in(module):
    api_calls = []

    for name in dir(module):
        if not name.lower() == name or name.startswith('_'):
            continue
        api_calls.append(getattr(module, name))

    return api_calls


class TestGeneratedAPI(unittest.TestCase):
    """
    Eventually this needs to be replaced with something more robust. For now,
    it just checks that everything works as in "doesn't err."
    """

    def test_return_types(self):
        numbers = list(str(i) for i in range(10))
        for package in [ads_api, rest_api, streaming_api, webhooks_api]:
            for module in submodules_of(package):
                for api_call in api_calls_in(module):
                    arg_names = inspect.getargs(api_call.__code__).args
                    args = dict(zip(arg_names, numbers[:len(arg_names)]))
                    self.assertTrue(isinstance(api_call(**args), TwitterRequest))

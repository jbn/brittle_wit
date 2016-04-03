import unittest
from brittle_wit.streaming import *


class TestEntryProcessor(unittest.TestCase):
    def test_entry_processor(self):
        ep = EntryProcessor()
        self.assertFalse(ep)
        self.assertEqual(ep.messages, [])

        ep.append(b'"hello world"\r\n{"a": 20}')
        self.assertTrue(ep)
        self.assertEqual(ep.messages, ['hello world'])

        ep.append(b"\r\n42")
        self.assertEqual(ep.messages, [{'a': 20}])

        ep.append(b"\r\n")
        self.assertEqual(ep.messages, [42])
        self.assertEqual(ep.messages, [])



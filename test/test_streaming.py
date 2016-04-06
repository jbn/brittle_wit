import unittest
from brittle_wit.streaming import *


class TestEntryProcessor(unittest.TestCase):
    def test_entry_processor(self):
        ep = EntryProcessor()
        self.assertFalse(ep)
        self.assertEqual(ep.messages(), [])

        ep.process(b'"hello world"\r\n{"a": 20}')
        self.assertTrue(ep)
        self.assertEqual(ep.messages(), [b'"hello world"'])

        ep.process(b"\r\n42")
        self.assertEqual(ep.messages(), [b'{"a": 20}'])

        ep.process(b"\r\n")
        self.assertEqual(ep.messages(), [b"42"])
        self.assertEqual(ep.messages(), [])

        self.assertEqual(ep._buf, b"")
        ep.process(b"x")
        self.assertEqual(ep._buf, b"x")
        ep.process(b"kcd\r\n")
        self.assertEqual(ep.messages(), [b"xkcd"])
        self.assertEqual(ep._buf, b"")
        self.assertEqual(ep._buf, b"")

    def test_purge_mailbox(self):
        ep = EntryProcessor()
        ep.process(b"hello\r\nworld")
        self.assertTrue(ep)
        ep.purge_mailbox()
        self.assertFalse(ep)

    def test_purge_streaming(self):
        ep = EntryProcessor()
        ep.process(b"corrupt_buffer...")
        ep.purge_buffer()
        ep.process(b"good buffer\r\n")
        self.assertEqual(ep.take_one(), b"good buffer")


    def test_take_one(self):
        ep = EntryProcessor()
        ep.process(b"hello\r\nworld")
        self.assertEqual(ep.take_one(), b"hello")
        self.assertFalse(ep)

    def test_iteration(self):
        ep = EntryProcessor()
        ep.process(b"hello\r\nworld\r\n")
        self.assertEqual(list(ep), [b"hello", b"world"])




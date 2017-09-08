import unittest
import os
import bz2
import brittle_wit
from test.helpers import drive_coro_once
from unittest.mock import Mock, MagicMock, patch
from brittle_wit_core import AppCredentials, ClientCredentials, TwitterRequest
from brittle_wit.streaming import *
from test.helpers import FIXTURES_DIR


SERIALIZATION_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'tmp')


class TestEntryProcessor(unittest.TestCase):

    def test_is_initially_empty(self):
        ep = EntryProcessor()
        self.assertFalse(ep)
        self.assertEqual(ep.messages(), [])

    def test_process(self):
        ep = EntryProcessor()

        # Send two messages but don't close the second one.
        ep.process(b'"hello world"\r\n{"a": 20}')
        self.assertTrue(ep)
        self.assertEqual(ep.messages(), [b'"hello world"'])

        # Close the second one; start but don't close another.
        ep.process(b"\r\n42")
        self.assertEqual(ep.messages(), [b'{"a": 20}'])

        # Close it.
        ep.process(b"\r\n")
        self.assertEqual(ep.messages(), [b"42"])

        # There are no messages.
        self.assertEqual(ep.messages(), [])

        # The buffer is an emtpy byte string.
        self.assertEqual(ep._buf, b"")

        # It accumulates bytes.
        ep.process(b"x")
        self.assertEqual(ep._buf, b"x")
        ep.process(b"kcd\r\n")
        self.assertEqual(ep.messages(), [b"xkcd"])
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


class TestParsers(unittest.TestCase):

    def test_noop_entry_parser(self):
        self.assertEqual(noop_entry_parser("hello"), "hello")

    def test_json_entry_parser(self):
        self.assertEqual(json_entry_parser(b"[10, 20, 30]"), [10, 20, 30])


# XXX: TODO: Brittle as fuck.
class TestTwitterStream(unittest.TestCase):

    def setUp(self):
        self.twitter_req = brittle_wit.streaming_api.statuses.filter()
        self.session = Mock()
        self.session.request = Mock()
        self.stream = TwitterStream(self.session,
                                    AppCredentials("app", "secret"),
                                    ClientCredentials(1, "client", "secret"),
                                    self.twitter_req)

    def test_is_not_open_by_default(self):
        self.assertFalse(self.stream.is_open)

    def test_no_double_connecting(self):
        self.stream._connect()
        self.assertTrue(self.session.request.called)
        self.stream._resp = Mock()
        self.stream._resp.connection.closed = False

        with self.assertRaises(RuntimeError):
            self.stream._connect()

    def test_disconnect_closes_underlying_http_req(self):
        self.stream._connect()
        http_req = Mock()
        self.stream._http_req = http_req
        self.stream.disconnect()
        self.assertTrue(http_req.close.called)
        self.assertIs(self.stream._http_req, None)

    def test_reconnect(self):
        self.stream._entry_processor = Mock()
        self.stream.reconnect(clear_prior_messages=True)
        self.assertTrue(self.stream._entry_processor.purge_mailbox.called)
        self.assertTrue(self.stream._entry_processor.purge_buffer.called)

    def test_reconnect_forces_closure(self):
        self.stream._connect()
        self.stream._resp = Mock()
        self.stream._resp.connection.closed = True
        self.stream.reconnect()

    def test__aiter__200_status(self):
        self.stream._resp = Mock()
        self.stream._resp.connection.closed = False

        self.stream._connect = Mock()

        class MockReq:
            async def __aenter__(self):
                resp = Mock()
                resp.connection.closed = False
                resp.status = 200

                return resp

        self.stream._http_req = MockReq()

        drive_coro_once(self.stream.__aiter__())

    def test__aiter__300_status(self):
        class MockResp:

            def __init__(self):
                self.status = 500

            @property
            def connection(self):
                m = Mock()
                m.closed = True
                return m

            async def text(self):
                return "mock text"

        self.stream._resp = MockResp()

        self.stream._connect = Mock()

        class MockReq:
            async def __aenter__(self):
                return MockResp()

        self.stream._http_req = MockReq()

        with self.assertRaises(TwitterError):
            drive_coro_once(self.stream.__aiter__())

    def test__anext__(self):

        class MockRead:

            async def read(self, n):
                return b"this is a message\r\nthis is another\r\n"

        class MockResp:

            @property
            def content(self):
                return MockRead()

        self.stream._resp = MockResp()
        msg = drive_coro_once(self.stream.__anext__())
        self.assertEqual(msg, b"this is a message")
        msg = drive_coro_once(self.stream.__anext__())
        self.assertEqual(msg, b"this is another")

class TestFeedReceivers(unittest.TestCase):

    def test_feed_serializer(self):
        output_path = os.path.join(SERIALIZATION_DIR, "feed.bz2")

        feed_serializer = FeedSerializer(output_path, as_bz2=True)

        messages = [[1, 2], [3, 4]]
        for msg in messages:
            feed_serializer.send(msg)

        # XXX: Ensure close called?
        feed_serializer.close()

        with bz2.open(output_path) as fp:
            res = [json.loads(s.decode('utf8')) for s in fp.readlines()]
            self.assertEqual(res, messages)

        os.unlink(output_path)

    def test_lambda_stream_handler(self):
        received = []
        rcvr = LambdaStreamHandler(lambda msg: received.append(msg))

        messages = [[1, 2], [3, 4]]
        for msg in messages:
            rcvr.send(msg)

        self.assertEqual(received, messages)


class TestStreamingProcessor(unittest.TestCase):

    def setUp(self):
        byte_msgs, json_msgs = [], []
        self.byte_msgs, self.json_msgs = byte_msgs, json_msgs
        self.byte_handler = LambdaStreamHandler(lambda m: byte_msgs.append(m))
        self.json_handler = LambdaStreamHandler(lambda m: json_msgs.append(m))

    def test_subscribe_raw(self):
        sp = StreamProcessor(None)
        sp.subscribe(self.byte_handler, as_json=False)
        self.assertFalse(sp._requires_json)

    def test_subscribe_json(self):
        sp = StreamProcessor(None)
        sp.subscribe(self.json_handler, True)
        self.assertTrue(sp._requires_json)

    def test_no_duplicate_subscriptions(self):
        sp = StreamProcessor(None)
        sp.subscribe(self.json_handler, True)
        with self.assertRaises(RuntimeError):
            sp.subscribe(self.json_handler, True)

    def test_unsubscribe_tracks_need_for_json(self):
        sp = StreamProcessor(None)
        sp.subscribe(self.json_handler, True)
        sp.subscribe(self.byte_handler, False)
        self.assertTrue(sp._requires_json)
        sp.unsubscribe(self.json_handler)
        self.assertFalse(sp._requires_json)

    def test_no_unsubscribe_twice(self):
        sp = StreamProcessor(None)
        sp.subscribe(self.json_handler, True)
        sp.unsubscribe(self.json_handler)
        with self.assertRaises(RuntimeError):
            sp.unsubscribe(self.json_handler)

    def test_receiving_multi(self):
        sp = StreamProcessor(None)
        sp.subscribe(self.byte_handler, False)
        sp.subscribe(self.json_handler, True)

        messages = [[1, 2, 3], [4, 5, 6]]
        for msg in messages:
            sp._send_to_all(json.dumps(msg).encode())

        self.assertEqual(self.json_msgs, messages)
        self.assertEqual(self.byte_msgs,
                         [json.dumps(m).encode() for m in messages])


class TestSaveRawStream(unittest.TestCase):

    def test_save_raw_stream(self):
        output_path = os.path.join(FIXTURES_DIR, "raw_stream")

        # coro = save_raw_stream(session, app_cred, client_cred, req, output_path)
        # drive_coro_once(coro)

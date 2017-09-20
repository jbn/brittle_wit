import aiohttp
import bz2
import os
import unittest

from aiohttp import web
import brittle_wit
from unittest.mock import Mock, MagicMock, patch
from brittle_wit_core import AppCredentials, ClientCredentials, TwitterRequest
from brittle_wit.streaming import *
from test.helpers import (FIXTURES_DIR, AsyncSafeTestCase, MockHTTPResp,
                          SERIALIZATION_DIR, async_patch, async_ignore_sleep,
                          mock_http_req, mock_content_reader,
                          ensure_deleted, mock_stream)


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
class TestTwitterStream(AsyncSafeTestCase):

    def setUp(self):
        self.twitter_req = brittle_wit.streaming_api.statuses.filter()
        self.session = Mock()
        self.session.request = Mock()
        self.stream = TwitterStream(self.session,
                                    AppCredentials("app", "secret"),
                                    ClientCredentials(1, "client", "secret"),
                                    self.twitter_req)

    def test_is_not_open_by_default(self):
        self.assertFalse(self.stream.is_open())

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
        self.stream._http_req = Mock()
        self.stream._resp = Mock()
        self.stream._resp.connection.closed = False
        self.stream.reconnect()

    def test_reconnect_errs_if_open(self):
        self.stream._connect()
        self.stream._http_req = Mock()
        self.stream._resp = Mock()
        self.stream._resp.connection.closed = False
        self.assertTrue(self.stream.is_open())
        with self.assertRaisesRegexp(RuntimeError, 'open stream'):
            self.stream.reconnect(force_close_if_open=False)

    async def test__aiter__200_status(self):
        self.stream._resp = Mock()
        self.stream._resp.connection.closed = False
        self.stream._connect = Mock()
        self.stream._http_req = mock_http_req(200, False)

        self.assertIs(await self.stream.__aiter__(), self.stream)

    async def test__aiter__auto_connect(self):
        self.stream._resp = Mock()
        self.stream._resp.connection.closed = True
        self.stream._connect = Mock()
        self.stream._http_req = mock_http_req(200, False)

        await self.stream.__aiter__()
        self.stream._connect.assert_called_once_with()

    async def test__aiter__300_status(self):
        with patch.object(self.stream, 'is_open', return_value=True) as pred:
            self.stream._http_req = mock_http_req(500, True, 'mock text')

            with self.assertRaises(TwitterError):
                await self.stream.__aiter__()

            pred.assert_called_once_with()

    async def test__anext__(self):
        messages = [b"this is a message\r\nthis is another\r\n"]

        self.stream._resp = mock_content_reader(messages)
        msg = await self.stream.__anext__()
        self.assertEqual(msg, b"this is a message")

        msg = await self.stream.__anext__()
        self.assertEqual(msg, b"this is another")

        with self.assertRaises(StopAsyncIteration):
            msg = await self.stream.__anext__()


class TestFeedReceivers(AsyncSafeTestCase):

    def test_stream_receiver_close_does_nothing_for_base(self):
        StreamReceiver().close()

    def test_feed_serializer_bz2(self):
        output_path = os.path.join(SERIALIZATION_DIR, "feed.bz2")
        ensure_deleted(output_path)

        feed_serializer = FeedSerializer(output_path, as_bz2=True)

        messages = [[1, 2], [3, 4]]
        for msg in messages:
            feed_serializer.send(msg)

        # XXX: Ensure close called?
        feed_serializer.close()

        with bz2.open(output_path) as fp:
            res = [json.loads(s.decode('utf8')) for s in fp.readlines()]
            self.assertEqual(res, messages)

        self.assertEqual(10, 20)
        ensure_deleted(output_path)

    def test_feed_serializer_bz2(self):
        output_path = os.path.join(SERIALIZATION_DIR, "feed.jsonl")
        ensure_deleted(output_path)

        feed_serializer = FeedSerializer(output_path,
                                         overwrite_existing=True,
                                         as_bz2=False)

        messages = [[1, 2], [3, 4]]
        for msg in messages:
            feed_serializer.send(msg)

        # XXX: Ensure close called?
        feed_serializer.close()

        with open(output_path, 'rb') as fp:
            res = [json.loads(s.decode('utf8')) for s in fp.readlines()]
            self.assertEqual(res, messages)

        ensure_deleted(output_path)

    def test_lambda_stream_handler(self):
        received = []
        rcvr = LambdaStreamHandler(lambda msg: received.append(msg))

        messages = [[1, 2], [3, 4]]
        for msg in messages:
            rcvr.send(msg)

        self.assertEqual(received, messages)

    async def test_streaming_http_pipe(self):
        pipe = StreamingHTTPPipe()
        httpd = web.Application()
        httpd.router.add_get('/', pipe.handle)

        msgs = [b'abcdefghij', b'klmnopqrst', b'ABCDEFGHIJ', b'KLMNOPQRST']

        async def dispatch_msgs():
            for msg in msgs:
                pipe.send(msg)

        async def client(n_reads):
            collected = []

            async with aiohttp.ClientSession() as sess:
                async with sess.get('http://localhost:8394') as resp:
                    self.assertEqual(resp.status, 200)

                    for i in range(n_reads):
                        collected.append(await resp.content.read(10))

                    resp.close()

            return collected

        loop = asyncio.get_event_loop()
        await loop.create_server(httpd.make_handler(), "localhost", 8394)

        alice = loop.create_task(client(3))
        bob = loop.create_task(client(4))

        await asyncio.sleep(1)

        await dispatch_msgs()

        self.assertEqual(await asyncio.wait_for(alice, 9), msgs[:3])
        self.assertEqual(await asyncio.wait_for(bob, 9), msgs[:4])

    async def test_streaming_http_pipe_handles_error(self):
        pipe = StreamingHTTPPipe()
        httpd = web.Application()
        httpd.router.add_get('/', pipe.handle)

        msgs = [b'abcdefghij', b'klmnopqrst', b'ABCDEFGHIJ', b'KLMNOPQRST']

        async def dispatch_msgs():
            for resp, _ in pipe._clients.values():
                await resp.write_eof()  # You can't do this. It will err.

            for msg in msgs:
                pipe.send(msg)

        async def client(n_reads):
            collected = []

            async with aiohttp.ClientSession() as sess:
                async with sess.get('http://localhost:8394') as resp:
                    self.assertEqual(resp.status, 200)

                    for i in range(n_reads):
                        data = await resp.content.read(10)
                        if data:
                            collected.append(data)

                    resp.close()

            return collected

        loop = asyncio.get_event_loop()

        await loop.create_server(httpd.make_handler(), "localhost", 8394)

        bob = loop.create_task(client(4))

        await asyncio.sleep(1)

        await dispatch_msgs()

        self.assertEqual(await asyncio.wait_for(bob, 9), [])

class TestStreamingProcessor(AsyncSafeTestCase):

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

    def test_subscribe_receiver_must_implement_send(self):
        sp = StreamProcessor(None)
        with self.assertRaises(AttributeError):
            sp.subscribe(None, True)

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

    async def test_stream_to_subscribers(self):
        expected = [b"a", b"b"]

        sp = StreamProcessor(None)
        sp._twitter_stream = mock_stream(expected)
        sp.subscribe(self.byte_handler, False)
        await sp._stream_to_subscribers()
        self.assertEqual(self.byte_msgs, expected)

    async def test_run_aborts_on_keyboard_interrupt(self):
        sp = StreamProcessor(None)
        sp._twitter_stream = mock_stream([KeyboardInterrupt()])

        # This is more explicit as a reminder: KeyboardInterrupts are weird.
        # There is some weirdness with KeyboardException and nosetest.
        # It can make things seem like they are working!
        raised = False
        try:
            await sp.run()
        except KeyboardInterrupt:
            raised = True
        self.assertTrue(raised)

    async def test_run_reraises_unguarded_exception(self):
        sp = StreamProcessor(None)
        sp._twitter_stream = mock_stream([AttributeError()])
        with self.assertRaises(AttributeError):
            await sp.run()

    async def _assert_run_expectations(self, expected, messages, **overrides):
        sp = StreamProcessor(mock_stream(messages))
        for k, v in overrides.items():
            setattr(sp, k, v)

        with async_ignore_sleep() as sleep_times:
            with patch.object(sp._twitter_stream, 'disconnect') as disconnect:
                with self.assertRaisesRegexp(RuntimeError, "Sentinel"):
                    await sp.run()

            self.assertEqual(len(disconnect.call_args_list), len(expected))
            self.assertEqual(sleep_times(), expected)

    async def test_run_on_timeout_error(self):
        expected = [min(0.25 * i, 16.0) for i in range(1, 66)]
        messages = ([asyncio.TimeoutError()] * len(expected) +
                    [RuntimeError("Sentinel")])
        await self._assert_run_expectations(expected, messages)

    async def test_run_on_client_error(self):
        expected = [min(0.25 * i, 16.0) for i in range(1, 66)]
        messages = ([aiohttp.ClientError()] * len(expected) +
                    [RuntimeError("Sentinel")])
        await self._assert_run_expectations(expected, messages)

    async def test_run_on_420_error(self):
        err = TwitterError(None, None, MockHTTPResp(420, [], None), '')
        expected = [60, 120, 240, 480, 960, 960]
        messages = ([err] * len(expected) + [RuntimeError("Sentinel")])
        await self._assert_run_expectations(expected, messages)

    async def test_run_on_other_twitter_error(self):
        err = TwitterError(None, None, MockHTTPResp(500, [], None), '')
        expected = [5, 10, 20, 40, 80, 160, 320, 320]
        messages = ([err] * len(expected) + [RuntimeError("Sentinel")])
        await self._assert_run_expectations(expected, messages)

    async def test_run_on_rate_limit(self):
        err = TwitterError(None, None, MockHTTPResp(429, [], None), '')
        expected = [42] * 3
        messages = ([err] * len(expected) + [RuntimeError("Sentinel")])

        mock_limit = Mock()
        mock_limit.sleep_time_remaining = 42
        with patch('brittle_wit.rate_limit.RateLimit.from_response', return_value=mock_limit):
            await self._assert_run_expectations(expected, messages, _resp=None)


class TestBasicStreamer(AsyncSafeTestCase):

    async def test_basic_streamer(self):
        app_cred = AppCredentials("app", "secret"),
        client_cred = ClientCredentials(1, "client", "secret"),
        twitter_req = brittle_wit.streaming_api.statuses.sample()
        callback = Mock()

        expected = [b'{"status": "a"}', b'{"status": "b"}', RuntimeError('Sentinel')]

        stream = mock_stream(expected)
        with patch('brittle_wit.streaming.TwitterStream', return_value=stream) as stream:
            with self.assertRaisesRegexp(RuntimeError, 'Sentinel'):
                await basic_streamer(app_cred, client_cred, twitter_req, callback)
            callbacks = [call[0][0] for call in callback.call_args_list]
            self.assertEqual([{'status': "a"}, {'status': "b"}], callbacks)

import json
from collections import deque


class EntryProcessor:
    """
    Splits a stream of bytes into CRLF-separated messages.
    """

    def __init__(self):
        # Note: I tried using a bytearray instead of a byte string but it
        # ended up being slower and having greater jitter than byte strings.
        self._buf = b""
        self._mailbox = deque()

    def process(self, chunk):
        """
        Translate received bytes into messages in a mailbox.

        :param chunk: a chunk of bytes received from the HTTP connection
        """
        self._buf += chunk

        # Streams are `\r\n`-separated JSON messages.
        raw_lines = self._buf.split(b"\r\n")

        # If only one element in the split, then there wasn't a CRLF.
        if len(raw_lines) > 1:

            # The last element may be a b'', which is perfectly fine.
            self._buf = raw_lines[-1]

            # Blank lines are keep-alive messages.
            self._mailbox.extend(l for l in raw_lines[:-1] if l.strip())

    def messages(self):
        """
        Return the messages then reset the mailbox

        :return: the enqueued messages as a list
        """
        return list(iter(self))

    def __bool__(self):
        """
        :return: True if there are any messages available
        """
        return bool(self._mailbox)

    def pop(self):
        """
        :return: the next message in the mailbox
        """
        return self._mailbox.popleft()

    def purge_buffer(self):
        """
        Reset the internal buffer.

        This is useful when restarting a stream. When the old stream
        terminates, the buffer is incomplete. Appending to it will produce a
        corrupt entry.
        """
        self._buf = b''

    def purge_mailbox(self):
        """
        Resets the mailbox so there are no messages
        """
        self._mailbox.clear()

    def __iter__(self):
        """
        :return: an iterator which pops messages of the mailbox until fully
            consumed
        """
        return self._entry_consumer()

    def _entry_consumer(self):
        while self._mailbox:
            yield self.pop()


def noop_entry_parser(entry):
    """
    :return: the entry string without further processing.
    """
    return entry


def json_entry_parser(entry):
    """
    :return: the entry parsed as a JSON object
    """
    return json.loads(entry.decode('ascii'))

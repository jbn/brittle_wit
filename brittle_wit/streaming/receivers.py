import bz2
import gzip
import json
import lzma
import os
import time


class StreamReceiver:
    """
    Base class for stream receivers.

    This isn't an ABC because I can imagine cases for super() chaining and I
    think subclassing code would discover introduced implementation errors
    quickly.
    """

    def send(self, msg):
        """
        :param msg: Either the raw bytes or a json-decoded object.
        """
        pass

    def close(self):
        pass


OPEN_FUNCS = {'.bz2': bz2.open, '.xz': lzma.open, '.gz': gzip.open}


def flexible_open(file_path, append=True):
    """
    Opens an output, binary file with inferred compression (or lack thereof).

    :param file_path: the output file path
    :param append: if False overwrite an existing file otherwise appends to it.
    :return: the opened file
    """
    mode = ('a' if append else 'w') + 'b'

    open_f = OPEN_FUNCS.get(os.path.splitext(file_path.lower())[-1], open)

    return open_f(file_path, mode)


class FeedSerializer(StreamReceiver):
    """
    Write each message to a bz2 file, *syncronously*.
    """

    def __init__(self, output_file, append=True):
        """
        :param as_bz2: if true, saves the file with BZ2 copression.
            BZ2 is useful for Spark/Hadoop analytics as it's splittable and
            compression rate is high. However, it's CPU intensive, which could
            be a problem.
        """
        self._output_stream = flexible_open(output_file, append)

    def send(self, msg):
        if not isinstance(msg, bytes):
            msg = json.dumps(msg).encode()
        self._output_stream.write(msg + b"\n")

    def close(self):
        self._output_stream.close()


class PartitioningFeedSerializer(StreamReceiver):
    """
    A Feed Serializer that creates a new archive partition every n messages.
    """

    def __init__(self, n_per_file, path_tmpl, append=False):
        """
        :param n_per_file: Messages per file before next partition created
        :param path_tmpl: a string representing the output path with a
            placeholder for format that injects the creation time. E.g.
            "my_log.{}.jsonl".
        """
        self._msgs_read = 0
        self._n_per_file = n_per_file
        self._path_tmpl = path_tmpl
        self._append = append

        file_path = self._path_tmpl.format(time.time())
        self._serializer = FeedSerializer(file_path, self._append)

    def send(self, msg):
        self._serializer.send(msg)

        self._msgs_read += 1

        if self._msgs_read >= self._n_per_file:
            self._msgs_read = 0
            self._serializer.close()

            file_path = self._path_tmpl.format(time.time())
            self._serializer = FeedSerializer(file_path, self._append)


class CallableStreamHandler(StreamReceiver):
    """
    Stream receiver that wraps a callable (mostly for testing)
    """

    def __init__(self, underlying_func):
        """
        :param underlying_func: function to invoke for each message received
            by ``#send(msg)``
        """
        self._underlying_func = underlying_func

    def send(self, msg):
        return self._underlying_func(msg)

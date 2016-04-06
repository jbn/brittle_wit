import asyncio


class Ticket:
    """
    A locking, synchronization context manager that enforces FIFO ordering.
    """

    __slots__ = '_ticket_master', '_line', '_antecedent', '_consequent'

    def __init__(self, ticket_master, line, antecedent_lock, consequent_lock):
        """
        :param ticket_master: the TicketMaster that originated this ticket
        :param line: the line this ticket is for
        :param antecedent_lock: the lock that must be acquired before the
            context body can execute
        :param consequent_lock: the lock that must be held until execution
            completes
        """
        self._ticket_master = ticket_master
        self._line = line
        self._antecedent = antecedent_lock
        self._consequent = consequent_lock

    @property
    def line(self):
        return self._line

    @property
    def consequent(self):
        return self._consequent

    async def acquire(self):
        # Immediately acquire the consequent lock. The next ticket
        # uses this as there antecedent. So, the next ticket cannot
        # progress until this ticket releases its consequent.
        await self._consequent.acquire()

        # Attempt to acquire the antecedent. This acts as a
        # barrier on execution. Continue once the antecedent
        # completes.
        async with self._antecedent:
            pass  # This is a barrier

    def release(self):
        # Release the consequent so that the next ticket can proceed.
        self._consequent.release()

        # Allow the TicketMaster to optionally cleanup a line.
        self._ticket_master.notify_finished(self)

    async def __aenter__(self):
        await self.acquire()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.release()




class TicketMaster:

    __slots__ = '_lines'

    def __init__(self):
        self._lines = {}  # line -> consequent

    def is_line_empty(self, line):
        """
        :return: True if the given line is empty
        """
        return line not in self._lines

    def all_lines_empty(self):
        """
        :return: True if the all the lines are empty
        """
        return not self._lines

    def notify_finished(self, ticket):
        """
        Notify this ticket master after ticket use.
        """
        if self._lines[ticket.line] is ticket.consequent:
            del self._lines[ticket.line]

    def take_ticket(self, line, loop=None):
        """
        Take a ticket on a specific line

        :param line: the requested line
        :param loop: the event loop

        :return: a Ticket
        """
        antecedent = self._lines.get(line, asyncio.Lock(loop=loop))
        consequent = asyncio.Lock(loop=loop)
        self._lines[line] = consequent

        return Ticket(self, line, antecedent, consequent)

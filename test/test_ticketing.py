import unittest
from brittle_wit.ticketing import TicketMaster
from test.helpers import *


async def use_ticket(ticket, identifier, busy_work):
    async with ticket:
        await busy_work
        return identifier


class BlowUpError(Exception):
    pass


async def blow_up():
    raise BlowUpError()


async def sim_ticket_master_usage(loop, n):
    tm = TicketMaster()

    tasks = []
    for i in range(n):
        # The first ticketed coro waits the longest....
        # The second waits second longest...
        busy_work = asyncio.sleep((n-1) * 0.02, loop=loop)

        coro = use_ticket(tm.take_ticket('test', loop), i, busy_work)
        tasks.append(loop.create_task(coro))
    results = []

    for task in asyncio.as_completed(tasks, loop=loop):
        results.append(await task)

    return results


async def sim_ticket_master_usage_with_blowup(loop):
    n = 5
    tm = TicketMaster()

    tasks = []
    for i in range(n):
        # The first ticketed coro waits the longest....
        # The second waits second longest..
        if i == 3:
            busy_work = blow_up()
        else:
            busy_work = asyncio.sleep((n-1) * 0.02, loop=loop)

        coro = use_ticket(tm.take_ticket('test', loop), i, busy_work)
        tasks.append(loop.create_task(coro))
    results = []

    for task in asyncio.as_completed(tasks, loop=loop):
        try:
            results.append(await task)
        except BlowUpError:
            pass

    return results


class TestTicketMaster(unittest.TestCase):
    def test_ticket_master(self):
        loop = asyncio.new_event_loop()
        n = 5
        result = loop.run_until_complete(sim_ticket_master_usage(loop, n))
        loop.close()
        self.assertEqual(result, list(range(n)))

    def test_ticket_master_with_failing_coro(self):
        loop = asyncio.new_event_loop()
        coro = sim_ticket_master_usage_with_blowup(loop)
        result = loop.run_until_complete(coro)
        loop.close()

        # Number 3 blows up
        self.assertEqual(result, [0, 1, 2, 4])

    def test_is_line_empty(self):
        tm = TicketMaster()
        self.assertTrue(tm.is_line_empty('main_line'))
        self.assertTrue(tm.is_line_empty('second_line'))
        tm._lines['main_line'] = 'MOCK'
        self.assertFalse(tm.is_line_empty('main_line'))
        self.assertTrue(tm.is_line_empty('second_line'))

    def test_all_lines_empty(self):
        tm = TicketMaster()
        self.assertTrue(tm.all_lines_empty())
        tm._lines['main_line'] = 'MOCK'
        self.assertFalse(tm.all_lines_empty())

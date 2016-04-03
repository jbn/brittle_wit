import asyncio
from collections import namedtuple
from functools import wraps


MockResp = namedtuple("MockResp", "headers")


def pristine_looped(f):
    @wraps(f)
    def _f():
        old_loop = asyncio.get_event_loop()
        new_loop = asyncio.new_event_loop()
        try:
            asyncio.set_event_loop(new_loop)
            f()
        finally:
            new_loop.close()
            asyncio.set_event_loop(old_loop)
    return f


@pristine_looped
def drive_coro_once(coro, timeout=None, swallow_timeout_error=True):
    # XXX: Make this prettier. Create a new loop or something.
    loop = asyncio.get_event_loop()
    try:
        return loop.run_until_complete(asyncio.wait_for(coro, timeout))
    except asyncio.TimeoutError as e:
        if not swallow_timeout_error:
            raise e

@pristine_looped
def drive_all(coros, timeout=None, swallow_timeout_error=True, interval=0.01):
    loop = asyncio.get_event_loop()

    async def _collector():
        tasks = []

        for coro in coros:
            tasks.append(loop.create_task(coro))
            # Loosely enforce ordering using sleep.
            # XXX: This is a FUCKING fragile test.
            await asyncio.sleep(interval)

        results = []
        for task in asyncio.as_completed(tasks):
            results.append(await task)
        return results

    return loop.run_until_complete(_collector())

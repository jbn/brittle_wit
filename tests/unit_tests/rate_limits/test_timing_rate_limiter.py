from brittle_wit.rate_limit import TimingRateLimiter


def test_timing_rate_limiter():
    limiter = TimingRateLimiter(60)
    assert limiter.can_proceed()
    assert not limiter.can_proceed()

    limiter._start_time -= 61
    assert limiter.can_proceed()

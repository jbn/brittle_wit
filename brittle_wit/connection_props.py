import aiohttp


# ============================================================================

TCP_CONN_REST = {}

# I think this is nessessary. If you are streaming and don't
# properly disconnect, Twitter may think you have two IPs open.
# > Some ssl servers do not properly complete ssl shutdown process,
# > in that case asyncio leaks ssl connections. If this parameter is
# > set to True, aiohttp additionally aborts underlining transport
# > after 2 seconds. It is off by default.
TCP_CONN_REST['enable_cleanup_closed'] = True

# ============================================================================

TCP_CONN_STREAMING = TCP_CONN_REST.copy()

TCP_CONN_STREAMING['enable_cleanup_closed'] = True

# From: https://dev.twitter.com/streaming/public
#
# > Each account may create only one standing connection to the public
# > endpoints, and connecting to a public stream more than once with the
# > same account credentials will cause the oldest connection to be
# > disconnected.  Clients which make excessive connection attempts
# > (both successful and unsuccessful) run the risk of having their IP
# > automatically banned.
#
# So, this forces close to ensure only ONE standing connection.
TCP_CONN_STREAMING['force_close'] = True

# TODO: Does this mean you can only stream from one APP or CLIENT per IP?
#
# I think the latter.
#
# As per: https://dev.twitter.com/streaming/userstreams
# > Minimize the number of connections your application makes to User
# > Streams. Each Twitter account is limited to only a few simultaneous
# > User Streams connections per OAuth application, regardless of IP.
# TCP_CONN_STREAMING['limit_per_host'] = 1

# ============================================================================

SESSION_OPTS = {}

# Twitter does not need any cookie processing for it's API.
SESSION_OPTS['cookie_jar'] = aiohttp.DummyCookieJar()

# From: https://dev.twitter.com/streaming/overview/connecting
# > Set a timer, either a 90 second TCP level socket timeout, or a
# > 90 second application level timer on the receipt of new data. If
# > 90 seconds pass with no data received, including newlines,
# > disconnect and reconnect immediately according to the backoff
# > strategies in the next section. The Streaming API will send a
# > keep-alive newline every 30 seconds to prevent your application
# > from timing out the connection. You should wait at least 3 cycles
# > to prevent spurious reconnects in the event of network congestion,
# > local CPU starvation, local GC pauses, etc.
SESSION_OPTS['conn_timeout'] = 90
SESSION_OPTS['read_timeout'] = None

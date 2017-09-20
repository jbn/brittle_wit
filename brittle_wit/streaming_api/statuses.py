###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def filter(*, follow=_ELIDE, track=_ELIDE, locations=_ELIDE,
           delimited=_ELIDE, stall_warnings=_ELIDE):
    """
    Returns public statuses that match one or more filter predicates. Multiple
    parameters may be specified which allows most clients to use a single
    connection to the Streaming API. Both GET and POST requests are supported,
    but GET requests with too many parameters may cause the request to be
    rejected for excessive URL length. Use a POST request to avoid long URLs.

    :param follow: A comma separated list of user IDs, indicating the users to
        return statuses for in the stream. See follow for more information.

    :param track: Keywords to track. Phrases of keywords are specified by a
        comma-separated list. See track for more information.

    :param locations: Specifies a set of bounding boxes to track. See locations
        for more information.

    :param delimited: Specifies whether messages should be length-delimited.
        See delimited for more information.

    :param stall_warnings: Specifies whether stall warnings should be
        delivered. See stall_warnings for more information.
    """
    binding = {'follow': follow, 'track': track, 'locations': locations,
               'delimited': delimited, 'stall_warnings': stall_warnings}
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    return _TwitterRequest('POST',
                           url,
                           'streaming:statuses',
                           'post-statuses-filter',
                           binding)


def sample(*, delimited=_ELIDE, stall_warnings=_ELIDE):
    """
    Returns a small random sample of all public statuses. The Tweets returned
    by the default access level are the same, so if two different clients
    connect to this endpoint, they will see the same Tweets.

    :param delimited: Specifies whether messages should be length-delimited.
        See delimited or more information.

    :param stall_warnings: Specifies whether stall warnings should be
        delivered. See stall_warnings for more information.
    """
    binding = {'delimited': delimited, 'stall_warnings': stall_warnings}
    url = 'https://stream.twitter.com/1.1/statuses/sample.json'
    return _TwitterRequest('GET',
                           url,
                           'streaming:statuses',
                           'get-statuses-sample',
                           binding)


_TwitterRequest.DOC_URLS['https://stream.twitter.com/1.1/statuses/filter.json'] = 'https://dev.twitter.com/streaming/reference/post/statuses/filter'
_TwitterRequest.DOC_URLS['https://stream.twitter.com/1.1/statuses/sample.json'] = 'https://dev.twitter.com/streaming/reference/get/statuses/sample'

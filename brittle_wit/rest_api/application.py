###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def rate_limit_status(*, resources=_ELIDE):
    """
    Returns the current rate limits for methods belonging to the specified
    resource families.

    :param resources: A comma-separated list of resource families you want to
        know the current rate limit disposition for. For best performance, only
        specify the resource families pertinent to your application. See API
        Rate Limiting for more information.
    """
    binding = {'resources': resources}
    url = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:application',
                           'get-application-rate-limit-status',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/application/rate_limit_status.json'] = 'https://dev.twitter.com/rest/reference/get/application/rate_limit_status'

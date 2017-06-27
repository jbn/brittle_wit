###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, IGNORE


def rate_limit_status(*, resources=IGNORE):
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
    return TwitterRequest('GET',
                          url,
                          'rest:application',
                          'get-application-rate-limit-status',
                          binding)



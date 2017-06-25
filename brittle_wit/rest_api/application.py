###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def rate_limit_status(*, resources=IGNORE):
    """
    Returns the current rate limits for methods belonging to the specified
    resource families.
    
    :param resources: A comma-separated list of resource families you want to k
        now the current rate limit disposition for. For best performance, only
        specify the resource families pertinent to your application. See API
        Rate Limiting for more information. (False)
    """
    url = "https://api.twitter.com/1.1/application/rate_limit_status.json"
    return TwitterRequest('GET',
                          url,
                          'REST:APPLICATION',
                          'GET-APPLICATION-RATE-LIMIT-STATUS',
                          resources=resources)



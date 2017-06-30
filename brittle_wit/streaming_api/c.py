###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def info_by_stream_id(stream_id):
    """
    Retrieves information about the established stream represented by the
    """
    binding = {'stream_id': stream_id}
    url = 'https://sitestream.twitter.com/2b/site/c/01_225167_334389048B872A533002B34D73F8C29FD09EFC50/info.json'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'streaming:c',
                          'get-c-stream-id-info',
                          binding)



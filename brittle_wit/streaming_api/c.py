###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def info_by_stream_id(stream_id):
    """
    Retrieves information about the established stream represented by the
    """
    url = "https://sitestream.twitter.com/2b/site/c/01_225167_334389048B872A533002B34D73F8C29FD09EFC50/info.json"
    url = url.format(stream_id=stream_id)
    return TwitterRequest('GET',
                          url,
                          'STREAMING:C',
                          'GET-C-STREAM-ID-INFO',
                          stream_id=stream_id)



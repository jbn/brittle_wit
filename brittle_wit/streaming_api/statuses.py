###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def filter(*, follow=IGNORE, track=IGNORE, locations=IGNORE, delimited=IGNORE, stall_warnings=IGNORE):
    """
    Returns public statuses that match one or more filter predicates. Multiple
    parameters may be specified which allows most clients to use a single
    connection to the Streaming API. Both GET and POST requests are supported,
    but GET requests with too many parameters may cause the request to be
    rejected for excessive URL length. Use a POST request to avoid long URLs.
    
    :param follow: A comma separated list of user IDs, indicating the users to 
        return statuses for in the stream. See follow for more information.
        (False)
    
    
    :param track: Keywords to track. Phrases of keywords are specified by a com
        ma-separated list. See track for more information. (False)
    
    
    :param locations: Specifies a set of bounding boxes to track. See locations
        for more information. (False)
    
    
    :param delimited: Specifies whether messages should be length-delimited. Se
        e delimited for more information. (False)
    
    
    :param stall_warnings: Specifies whether stall warnings should be delivered
        . See stall_warnings for more information. (False)
    """
    url = "https://stream.twitter.com/1.1/statuses/filter.json"
    return TwitterRequest('POST',
                          url,
                          'STREAMING:STATUSES',
                          'POST-STATUSES-FILTER',
                          follow=follow
                          track=track
                          locations=locations
                          delimited=delimited
                          stall_warnings=stall_warnings)


def sample(*, delimited=IGNORE, stall_warnings=IGNORE):
    """
    Returns a small random sample of all public statuses. The Tweets returned
    by the default access level are the same, so if two different clients
    connect to this endpoint, they will see the same Tweets.
    
    :param delimited: Specifies whether messages should be length-delimited. Se
        e delimited or more information. (False)
    
    
    :param stall_warnings: Specifies whether stall warnings should be delivered
        . See stall_warnings for more information. (False)
    """
    url = "https://stream.twitter.com/1.1/statuses/sample.json"
    return TwitterRequest('GET',
                          url,
                          'STREAMING:STATUSES',
                          'GET-STATUSES-SAMPLE',
                          delimited=delimited
                          stall_warnings=stall_warnings)



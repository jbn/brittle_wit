###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def available():
    """
    Returns the locations that Twitter has trending topic information for.
    """
    url = "https://api.twitter.com/1.1/trends/available.json"
    return TwitterRequest('GET',
                          url,
                          'REST:TRENDS',
                          'GET-TRENDS-AVAILABLE')


def closest(lat, long):
    """
    Returns the locations that Twitter has trending topic information for,
    closest to a specified location.
    
    :param lat: If provided with a long parameter the available trend locations
        will be sorted by distance, nearest to furthest, to the co-ordinate
        pair. The valid ranges for longitude is -180.0 to +180.0 (West is
        negative, East is positive) inclusive. (True)
    
    
    :param long: If provided with a lat parameter the available trend locations
        will be sorted by distance, nearest to furthest, to the co-ordinate
        pair. The valid ranges for longitude is -180.0 to +180.0 (West is
        negative, East is positive) inclusive. (True)
    """
    url = "https://api.twitter.com/1.1/trends/closest.json"
    return TwitterRequest('GET',
                          url,
                          'REST:TRENDS',
                          'GET-TRENDS-CLOSEST',
                          lat=lat
                          long=long)


def place(id, *, exclude=IGNORE):
    """
    Returns the top 50 trending topics for a specific
    
    :param id: The Yahoo! Where On Earth ID of the location to return trending 
        information for. Global information is available by using 1 as the
        WOEID. (True)
    
    
    :param exclude: Setting this equal to hashtags will remove all hashtags fro
        m the trends list. (False)
    """
    url = "https://api.twitter.com/1.1/trends/place.json"
    return TwitterRequest('GET',
                          url,
                          'REST:TRENDS',
                          'GET-TRENDS-PLACE',
                          id=id
                          exclude=exclude)



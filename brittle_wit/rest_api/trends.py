###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def available():
    """
    Returns the locations that Twitter has trending topic information for.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/trends/available.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:trends',
                           'get-trends-available',
                           binding)


def closest(lat, long):
    """
    Returns the locations that Twitter has trending topic information for,
    closest to a specified location.

    :param lat: If provided with a long parameter the available trend locations
        will be sorted by distance, nearest to furthest, to the co-ordinate
        pair. The valid ranges for longitude is -180.0 to +180.0 (West is
        negative, East is positive) inclusive.

    :param long: If provided with a lat parameter the available trend locations
        will be sorted by distance, nearest to furthest, to the co-ordinate
        pair. The valid ranges for longitude is -180.0 to +180.0 (West is
        negative, East is positive) inclusive.
    """
    binding = {'lat': lat, 'long': long}
    url = 'https://api.twitter.com/1.1/trends/closest.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:trends',
                           'get-trends-closest',
                           binding)


def place(id, *, exclude=_ELIDE):
    """
    Returns the top 50 trending topics for a specific

    :param id: The Yahoo! Where On Earth ID of the location to return trending
        information for. Global information is available by using 1 as the
        WOEID.

    :param exclude: Setting this equal to hashtags will remove all hashtags
        from the trends list.
    """
    binding = {'id': id, 'exclude': exclude}
    url = 'https://api.twitter.com/1.1/trends/place.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:trends',
                           'get-trends-place',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/trends/available.json'] = 'https://dev.twitter.com/rest/reference/get/trends/available'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/trends/closest.json'] = 'https://dev.twitter.com/rest/reference/get/trends/closest'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/trends/place.json'] = 'https://dev.twitter.com/rest/reference/get/trends/place'

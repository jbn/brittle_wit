###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def id_by_place_id(place_id):
    """
    Returns all the information about a known
    
    :param place_id: A place in the world. These IDs can be retrieved from geo/
        reverse_geocode. (True)
    """
    url = "https://api.twitter.com/1.1/geo/id/{place_id}.json"
    url = url.format(place_id=place_id)
    return TwitterRequest('GET',
                          url,
                          'REST:GEO',
                          'GET-GEO-ID-PLACE-ID',
                          place_id=place_id)


def reverse_code(lat, long, *, accuracy=IGNORE, granularity=IGNORE, max_results=IGNORE, callback=IGNORE):
    """
    Given a latitude and a longitude, searches for up to 20 places that can be
    used as a
    
    :param lat: The latitude to search around. This parameter will be ignored u
        nless it is inside the range -90.0 to +90.0 (North is positive)
        inclusive. It will also be ignored if there isn't a corresponding long
        parameter. (True)
    
    
    :param long: The longitude to search around. The valid ranges for longitude
        is -180.0 to +180.0 (East is positive) inclusive. This parameter will
        be ignored if outside that range, if it is not a number, if geo_enabled
        is disabled, or if there not a corresponding lat parameter. (True)
    
    
    :param accuracy: A hint on the “region” in which to search. If a number, th
        en this is a radius in meters, but it can also take a string that is
        suffixed with ft to specify feet. If this is not passed in, then it is
        assumed to be 0m. If coming from a device, in practice, this value is
        whatever accuracy the device has measuring its location (whether it be
        coming from a GPS, WiFi triangulation, etc.). (False)
    
    
    :param granularity: This is the minimal granularity of place types to retur
        n and must be one of: poi, neighborhood, city, admin or country. If no
        granularity is provided for the request neighborhood is assumed.
        Setting this to city, for example, will find places which have a type
        of city, admin or country. (False)
    
    
    :param max_results: A hint as to the number of results to return. This does
        not guarantee that the number of results returned will equal
        max_results, but instead informs how many “nearby” results to return.
        Ideally, only pass in the number of places you intend to display to the
        user here. (False)
    
    
    :param callback: If supplied, the response will use the JSONP format with a
        callback of the given name. (False)
    """
    url = "https://api.twitter.com/1.1/geo/reverse_geocode.json"
    return TwitterRequest('GET',
                          url,
                          'REST:GEO',
                          'GET-GEO-REVERSE-GEOCODE',
                          lat=lat
                          long=long
                          accuracy=accuracy
                          granularity=granularity
                          max_results=max_results
                          callback=callback)


def search(*, lat=IGNORE, long=IGNORE, query=IGNORE, ip=IGNORE, granularity=IGNORE, accuracy=IGNORE, max_results=IGNORE, contained_within=IGNORE, attribute:street_address=IGNORE, callback=IGNORE):
    """
    Search for places that can be attached to a statuses/update. Given a
    latitude and a longitude pair, an IP address, or a name, this request will
    return a list of all the valid places that can be used as the
    
    :param lat: The latitude to search around. This parameter will be ignored u
        nless it is inside the range -90.0 to +90.0 (North is positive)
        inclusive. It will also be ignored if there isn't a corresponding long
        parameter. (False)
    
    
    :param long: The longitude to search around. The valid ranges for longitude
        is -180.0 to +180.0 (East is positive) inclusive. This parameter will
        be ignored if outside that range, if it is not a number, if geo_enabled
        is disabled, or if there not a corresponding lat parameter. (False)
    
    
    :param query: Free-form text to match against while executing a geo-based q
        uery, best suited for finding nearby locations by name. Remember to URL
        encode the query. (False)
    
    
    :param ip: An IP address. Used when attempting to fix geolocation based off
        of the user's IP address. (False)
    
    
    :param granularity: This is the minimal granularity of place types to retur
        n and must be one of: poi, neighborhood, city, admin or country. If no
        granularity is provided for the request neighborhood is assumed.
        Setting this to city, for example, will find places which have a type
        of city, admin or country. (False)
    
    
    :param accuracy: A hint on the “region” in which to search. If a number, th
        en this is a radius in meters, but it can also take a string that is
        suffixed with ft to specify feet. If this is not passed in, then it is
        assumed to be 0m. If coming from a device, in practice, this value is
        whatever accuracy the device has measuring its location (whether it be
        coming from a GPS, WiFi triangulation, etc.). (False)
    
    
    :param max_results: A hint as to the number of results to return. This does
        not guarantee that the number of results returned will equal
        max_results, but instead informs how many “nearby” results to return.
        Ideally, only pass in the number of places you intend to display to the
        user here. (False)
    
    
    :param contained_within: This is the place_id which you would like to restr
        ict the search results to. Setting this value means only places within
        the given place_id will be found. Specify a place_id. For example, to
        scope all results to places within “San Francisco, CA USA”, you would
        specify a place_id of “5a110d312052166f” (False)
    
    
    :param attribute:street_address: This parameter searches for places which h
        ave this given street address. There are other well-known, and
        application specific attributes available. Custom attributes are also
        permitted. Learn more about [node:208, title=”Place Attributes”].
        (False)
    
    
    :param callback: If supplied, the response will use the JSONP format with a
        callback of the given name. (False)
    """
    url = "https://api.twitter.com/1.1/geo/search.json"
    return TwitterRequest('GET',
                          url,
                          'REST:GEO',
                          'GET-GEO-SEARCH',
                          lat=lat
                          long=long
                          query=query
                          ip=ip
                          granularity=granularity
                          accuracy=accuracy
                          max_results=max_results
                          contained_within=contained_within
                          attribute:street_address=attribute:street_address
                          callback=callback)


def place(name, contained_within, token, lat, long, *, attribute:street_address=IGNORE, callback=IGNORE):
    """
    As of December 2nd, 2013, this endpoint
    
    :param name: The name a place is known as. (True)
    
    :param contained_within: The place_id within which the new place can be fou
        nd. Try and be as close as possible with the containing place. For
        example, for a room in a building, set the contained_within as the
        building place_id. (True)
    
    
    :param token: The token found in the response from geo/similar_places. (Tru
        e)
    
    
    :param lat: The latitude the place is located at. This parameter will be ig
        nored unless it is inside the range -90.0 to +90.0 (North is positive)
        inclusive. It will also be ignored if there isn't a corresponding long
        parameter. (True)
    
    
    :param long: The longitude the place is located at. The valid ranges for lo
        ngitude is -180.0 to +180.0 (East is positive) inclusive. This
        parameter will be ignored if outside that range, if it is not a number,
        if geo_enabled is disabled, or if there not a corresponding lat
        parameter. (True)
    
    
    :param attribute:street_address: This parameter searches for places which h
        ave this given street address. There are other well-known, and
        application specific attributes available. Custom attributes are also
        permitted. Learn more here. (False)
    
    
    :param callback: If supplied, the response will use the JSONP format with a
        callback of the given name. (False)
    """
    url = "https://api.twitter.com/1.1/geo/place.json"
    return TwitterRequest('POST',
                          url,
                          'REST:GEO',
                          'POST-GEO-PLACE',
                          name=name
                          contained_within=contained_within
                          token=token
                          lat=lat
                          long=long
                          attribute:street_address=attribute:street_address
                          callback=callback)



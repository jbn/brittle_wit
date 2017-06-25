###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def app_store_categories(*, store=IGNORE, q=IGNORE):
    """
    Discover available app store category-based targeting criteria for Promoted
    Products. App store categories are available for the iOS App Store and the
    Google Play store only.
    
    :param store: Scope the results by a specific app store. Possible values: I
        OS_APP_STORE, GOOGLE_PLAY (False)
    
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/app_store_categories"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-APP-STORE-CATEGORIES',
                          store=store
                          q=q)


def behavior_taxonomies(*, behavior_taxonomy_ids=IGNORE, parent_behavior_taxonomy_ids=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    This endpoint is used to list the full (or partial) structure of behavior
    taxonomy trees.
    
    :param behavior_taxonomy_ids: A comma-separated string of behavior taxonomy
        identifiers by which to filter the response. (False)
    
    
    :param parent_behavior_taxonomy_ids: A comma-separated string of behavior t
        axonomy identifiers of parent nodes in the tree structures. Specifying
        parents will only return children nodes of the taxonomy. If you specify
        null we return the root (top level category) of every taxonomy tree.
        (False)
    
    
    :param count: Specifies the maximum number of behaviors to return, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of behaviors. See pa
        gination for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/behavior_taxonomies"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-BEHAVIOR-TAXONOMIES',
                          behavior_taxonomy_ids=behavior_taxonomy_ids
                          parent_behavior_taxonomy_ids=parent_behavior_taxonomy_ids
                          count=count
                          cursor=cursor)


def behaviors(*, behavior_ids=IGNORE, country_code=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE):
    """
    Retrieves all valid behaviors defined by partner audiences that can be
    targeted by an advertiser.
    
    :param behavior_ids: A comma-separated string of behavior identifiers by wh
        ich to filter the response. (False)
    
    
    :param country_code: Specifies the ISO-3166-1 country code for which to req
        uest partner audiences. Only one country code can be specified. Note:
        If this parameter is not specified only partner audiences for the
        United States are returned. Valid Values: GB, US Default Value: US
        Default Value: US (False)
    
    
    :param count: Specifies the maximum number of behaviors to return, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of behaviors. See pa
        gination for more information. (False)
    
    
    :param sort_by: String Valid values: created_at, updated_at, deleted, name 
        Note : You must append -asc or -desc to these values as per our Sorting
        docs. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/behaviors"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-BEHAVIORS',
                          behavior_ids=behavior_ids
                          country_code=country_code
                          count=count
                          cursor=cursor
                          sort_by=sort_by)


def devices(*, q=IGNORE):
    """
    Discover available device-based targeting criteria for Promoted Products.
    Device targeting is available for Promoted Tweets. Examples of devices
    include
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/devices"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-DEVICES',
                          q=q)


def events(*, ids=IGNORE, event_types=IGNORE, country_codes=IGNORE, start_time=IGNORE, end_time=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Discover available event-based targeting criteria for Promoted Products.
    Only one event can be targeted per line item.
    
    :param ids: A comma separated list of event ids to get event targeting deta
        ils for (False)
    
    
    :param event_types: An optional query to scope to certain event types. Poss
        ible values are SPORTS, MUSIC_AND_ENTERTAINMENT, HOLIDAY, CONFERENCE,
        and OTHER (False)
    
    
    :param country_codes: An optional query to scope a targeting criteria searc
        h to a specific country with the 2 letters ISO country code. Omit this
        parameter to retrieve results for all countries. (False)
    
    
    :param start_time: Scopes the retrieved events to events occurring in the w
        indow of time between start_time and end_time. Expressed in ISO 8601.
        Defaults to the current date and time. (False)
    
    
    :param end_time: Scopes the retrieved events to events occurring in the win
        dow of time between start_time and end_time. Expressed in ISO 8601.
        (False)
    
    
    :param count: Specifies the maximum number of events to return, up to a max
        imum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of events. See pagin
        ation for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/events"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-EVENTS',
                          ids=ids
                          event_types=event_types
                          country_codes=country_codes
                          start_time=start_time
                          end_time=end_time
                          count=count
                          cursor=cursor)


def interests(*, q=IGNORE, lang=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Discover available interest-based targeting criteria for Promoted Products.
    Interests change infrequently, however we suggest you refresh this list at
    least once weekly.
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    
    
    :param lang: An ISO-639-1 language code. When passed, an additional localiz
        ed_name attribute will be returned in the response. (False)
    
    
    :param count: Specifies the number of locations to try and retrieve, up to 
        a maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of interests. See pa
        gination for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/interests"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-INTERESTS',
                          q=q
                          lang=lang
                          count=count
                          cursor=cursor)


def languages(*, q=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Discover languages available for targeting.
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/languages"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-LANGUAGES',
                          q=q
                          count=count
                          cursor=cursor)


def locations(*, location_type=IGNORE, q=IGNORE, country_code=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Discover available location-based targeting criteria for Promoted Products.
    Geo-targeting is available for Promoted Accounts and Promoted Tweets at the
    country level, state/region level, city level and postal code level. In the
    United States, the cities are Designated Market Areas (DMA). Postal code
    targeting must be used if you wish to retrieve analytics at the postal code
    level.
    
    :param location_type: Scope the results by a specific kind of location. Acc
        eptable values include: COUNTRY, REGION, CITY, and POSTAL_CODE. More
        granular targeting than COUNTRY may not be available in all locations.
        (False)
    
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    
    
    :param country_code: An optional query to scope a targeting criteria search
        to a specific country with the 2 letters ISO country code. Omit this
        parameter to retrieve results for all countries. (False)
    
    
    :param count: Specifies the number of locations to try and retrieve, up to 
        a maximum of 1,000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of locations. See pa
        gination for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/locations"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-LOCATIONS',
                          location_type=location_type
                          q=q
                          country_code=country_code
                          count=count
                          cursor=cursor)


def network_operators(*, country_code=IGNORE, q=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Target users based on mobile carrier (AT&T, Verizon, Sprint, T-Mobile, etc)
    in multiple countries. This endpoint enables you to lookup targetable
    carriers available for targeting with the
    
    :param country_code: An optional parameter that specifies the country_code 
        to query for from available network operators. (False)
    
    
    :param q: An optional query to scope a search. Omit this parameter to retri
        eve all results. (False)
    
    
    :param count: Specifies the number of locations to try and retrieve, up to 
        a maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of locations. See Pa
        gination for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/network_operators"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-NETWORK-OPERATORS',
                          country_code=country_code
                          q=q
                          count=count
                          cursor=cursor)


def platform_versions(*, q=IGNORE):
    """
    Discover available mobile-OS-version-based targeting criteria for Promoted
    Products. Platform version targeting is available for Promoted Accounts and
    Promoted Tweets. This allows targeting down to the point release of a
    mobile operating system version, for example iOS 7.1, Android 4.4
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/platform_versions"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-PLATFORM-VERSIONS',
                          q=q)


def platforms(*, q=IGNORE, lang=IGNORE):
    """
    Discover available platform-based targeting criteria for Promoted Products.
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    
    
    :param lang: An ISO-639-1 language code. When passed, an additional localiz
        ed_name attribute will be returned in the response. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/platforms"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-PLATFORMS',
                          q=q
                          lang=lang)


def tv_markets():
    """
    Discover available TV markets where TV shows can be targeted. Returns
    markets by locale that can used to query the
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/tv_markets"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-TV-MARKETS')


def tv_shows(tv_market_locale, *, q=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Discover available TV show targeting criteria for Promoted Products. TV
    show targeting is available for Promoted Tweets in certain markets. See
    
    :param tv_market_locale: A required parameter that specifies the tv_market_
        locale to query for available TV shows. TV markets are queried based on
        locale returned from the GET targeting_criteria/tv_markets endpoint.
        (True)
    
    
    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. (False)
    
    
    :param count: Specifies the number of TV shows to try and retrieve, up to a
        maximum of 50 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/targeting_criteria/tv_shows"
    return TwitterRequest('GET',
                          url,
                          'ADS:TARGETING_CRITERIA',
                          'GET-TARGETING-CRITERIA-TV-SHOWS',
                          tv_market_locale=tv_market_locale
                          q=q
                          count=count
                          cursor=cursor)



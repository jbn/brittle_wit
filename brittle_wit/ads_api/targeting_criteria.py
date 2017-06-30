###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def app_store_categories(*, store=ELIDE, q=ELIDE):
    """
    Discover available app store category-based targeting criteria for Promoted
    Products. App store categories are available for the iOS App Store and the
    Google Play store only.

    :param store: Scope the results by a specific app store. Possible values:
        IOS_APP_STORE, GOOGLE_PLAY

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.
    """
    binding = {'store': store, 'q': q}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/app_store_categories'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-app-store-categories',
                          binding)


def behavior_taxonomies(*, behavior_taxonomy_ids=ELIDE,
                        parent_behavior_taxonomy_ids=ELIDE, count=ELIDE,
                        cursor=ELIDE):
    """
    This endpoint is used to list the full (or partial) structure of behavior
    taxonomy trees.

    :param behavior_taxonomy_ids: A comma-separated string of behavior taxonomy
        identifiers by which to filter the response.

    :param parent_behavior_taxonomy_ids: A comma-separated string of behavior
        taxonomy identifiers of parent nodes in the tree structures. Specifying
        parents will only return children nodes of the taxonomy. If you specify
        null we return the root (top level category) of every taxonomy tree.

    :param count: Specifies the maximum number of behaviors to return, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of behaviors. See
        pagination for more information.
    """
    binding = {'behavior_taxonomy_ids': behavior_taxonomy_ids,
               'parent_behavior_taxonomy_ids': parent_behavior_taxonomy_ids,
               'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/behavior_taxonomies'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-behavior-taxonomies',
                          binding)


def behaviors(*, behavior_ids=ELIDE, country_code=ELIDE, count=ELIDE,
              cursor=ELIDE, sort_by=ELIDE):
    """
    Retrieves all valid behaviors defined by partner audiences that can be
    targeted by an advertiser.

    :param behavior_ids: A comma-separated string of behavior identifiers by
        which to filter the response.

    :param country_code: Specifies the ISO-3166-1 country code for which to
        request partner audiences. Only one country code can be specified.
        Note: If this parameter is not specified only partner audiences for the
        United States are returned. Valid Values: GB, US Default Value: US
        Default Value: US

    :param count: Specifies the maximum number of behaviors to return, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of behaviors. See
        pagination for more information.

    :param sort_by: String Valid values: created_at, updated_at, deleted, name
        Note : You must append -asc or -desc to these values as per our Sorting
        docs.
    """
    binding = {'behavior_ids': behavior_ids, 'country_code': country_code,
               'count': count, 'cursor': cursor, 'sort_by': sort_by}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/behaviors'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-behaviors',
                          binding)


def devices(*, q=ELIDE):
    """
    Discover available device-based targeting criteria for Promoted Products.
    Device targeting is available for Promoted Tweets. Examples of devices
    include

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.
    """
    binding = {'q': q}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/devices'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-devices',
                          binding)


def events(*, ids=ELIDE, event_types=ELIDE, country_codes=ELIDE,
           start_time=ELIDE, end_time=ELIDE, count=ELIDE, cursor=ELIDE):
    """
    Discover available event-based targeting criteria for Promoted Products.
    Only one event can be targeted per line item.

    :param ids: A comma separated list of event ids to get event targeting
        details for

    :param event_types: An optional query to scope to certain event types.
        Possible values are SPORTS, MUSIC_AND_ENTERTAINMENT, HOLIDAY,
        CONFERENCE, and OTHER

    :param country_codes: An optional query to scope a targeting criteria
        search to a specific country with the 2 letters ISO country code. Omit
        this parameter to retrieve results for all countries.

    :param start_time: Scopes the retrieved events to events occurring in the
        window of time between start_time and end_time. Expressed in ISO 8601.
        Defaults to the current date and time.

    :param end_time: Scopes the retrieved events to events occurring in the
        window of time between start_time and end_time. Expressed in ISO 8601.

    :param count: Specifies the maximum number of events to return, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of events. See
        pagination for more information.
    """
    binding = {'ids': ids, 'event_types': event_types, 'country_codes':
               country_codes, 'start_time': start_time, 'end_time': end_time,
               'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/events'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-events',
                          binding)


def interests(*, q=ELIDE, lang=ELIDE, count=ELIDE, cursor=ELIDE):
    """
    Discover available interest-based targeting criteria for Promoted Products.
    Interests change infrequently, however we suggest you refresh this list at
    least once weekly.

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.

    :param lang: An ISO-639-1 language code. When passed, an additional
        localized_name attribute will be returned in the response.

    :param count: Specifies the number of locations to try and retrieve, up to
        a maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of interests. See
        pagination for more information.
    """
    binding = {'q': q, 'lang': lang, 'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/interests'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-interests',
                          binding)


def languages(*, q=ELIDE, count=ELIDE, cursor=ELIDE):
    """
    Discover languages available for targeting.

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.
    """
    binding = {'q': q, 'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/languages'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-languages',
                          binding)


def locations(*, location_type=ELIDE, q=ELIDE, country_code=ELIDE,
              count=ELIDE, cursor=ELIDE):
    """
    Discover available location-based targeting criteria for Promoted Products.
    Geo-targeting is available for Promoted Accounts and Promoted Tweets at the
    country level, state/region level, city level and postal code level. In the
    United States, the cities are Designated Market Areas (DMA). Postal code
    targeting must be used if you wish to retrieve analytics at the postal code
    level.

    :param location_type: Scope the results by a specific kind of location.
        Acceptable values include: COUNTRY, REGION, CITY, and POSTAL_CODE. More
        granular targeting than COUNTRY may not be available in all locations.

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.

    :param country_code: An optional query to scope a targeting criteria search
        to a specific country with the 2 letters ISO country code. Omit this
        parameter to retrieve results for all countries.

    :param count: Specifies the number of locations to try and retrieve, up to
        a maximum of 1,000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of locations. See
        pagination for more information.
    """
    binding = {'location_type': location_type, 'q': q, 'country_code':
               country_code, 'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/locations'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-locations',
                          binding)


def network_operators(*, country_code=ELIDE, q=ELIDE, count=ELIDE,
                      cursor=ELIDE):
    """
    Target users based on mobile carrier (AT&T, Verizon, Sprint, T-Mobile, etc)
    in multiple countries. This endpoint enables you to lookup targetable
    carriers available for targeting with the

    :param country_code: An optional parameter that specifies the country_code
        to query for from available network operators.

    :param q: An optional query to scope a search. Omit this parameter to
        retrieve all results.

    :param count: Specifies the number of locations to try and retrieve, up to
        a maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of locations. See
        Pagination for more information.
    """
    binding = {'country_code': country_code, 'q': q, 'count': count, 'cursor':
               cursor}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/network_operators'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-network-operators',
                          binding)


def platform_versions(*, q=ELIDE):
    """
    Discover available mobile-OS-version-based targeting criteria for Promoted
    Products. Platform version targeting is available for Promoted Accounts and
    Promoted Tweets. This allows targeting down to the point release of a
    mobile operating system version, for example iOS 7.1, Android 4.4

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.
    """
    binding = {'q': q}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/platform_versions'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-platform-versions',
                          binding)


def platforms(*, q=ELIDE, lang=ELIDE):
    """
    Discover available platform-based targeting criteria for Promoted Products.

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.

    :param lang: An ISO-639-1 language code. When passed, an additional
        localized_name attribute will be returned in the response.
    """
    binding = {'q': q, 'lang': lang}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/platforms'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-platforms',
                          binding)


def tv_markets():
    """
    Discover available TV markets where TV shows can be targeted. Returns
    markets by locale that can used to query the
    """
    binding = {}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/tv_markets'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-tv-markets',
                          binding)


def tv_shows(tv_market_locale, *, q=ELIDE, count=ELIDE, cursor=ELIDE):
    """
    Discover available TV show targeting criteria for Promoted Products. TV
    show targeting is available for Promoted Tweets in certain markets. See

    :param tv_market_locale: A required parameter that specifies the
        tv_market_locale to query for available TV shows. TV markets are
        queried based on locale returned from the GET
        targeting_criteria/tv_markets endpoint.

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.

    :param count: Specifies the number of TV shows to try and retrieve, up to a
        maximum of 50 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.
    """
    binding = {'tv_market_locale': tv_market_locale, 'q': q, 'count': count,
               'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/targeting_criteria/tv_shows'
    return TwitterRequest('GET',
                          url,
                          'ads:targeting_criteria',
                          'get-targeting-criteria-tv-shows',
                          binding)



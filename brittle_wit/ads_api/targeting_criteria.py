###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def app_store_categories(*, q=_ELIDE, store=_ELIDE):
    """
    Discover available app store category-based targeting criteria for Promoted
    Products. App store categories are available for the iOS App Store and the
    Google Play store only.

    :param q: An optional query to scope a targeting criteria. Omit this
        parameter to retrive all. Type: string Example: music

    :param store: Scope the results by a specific app store. Type: enum
        Possible values: GOOGLE_PLAY, IOS_APP_STORE
    """
    binding = {'q': q, 'store': store}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/app_store_categories'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-app-store-categories',
                           binding)


def behavior_taxonomies(*, behavior_taxonomy_ids=_ELIDE, count=_ELIDE,
                        cursor=_ELIDE, parent_behavior_taxonomy_ids=_ELIDE,
                        sort_by=_ELIDE, with_total_count=_ELIDE):
    """
    This endpoint is used to list the full (or partial) structure of behavior
    taxonomy trees.

    :param behavior_taxonomy_ids: Scope the response to just the desired
        behavior taxonomies by specifying a comma-separated list of
        identifiers. Up to 200 IDs may be provided. Type: string Example: 5e

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param parent_behavior_taxonomy_ids: Scope the response to just the
        behavior taxonomies under specific parent nodes by specifying a comma-
        separated list of identifiers. Up to 200 IDs may be provided Type:
        string Example: 2e

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'behavior_taxonomy_ids': behavior_taxonomy_ids, 'count': count,
               'cursor': cursor, 'parent_behavior_taxonomy_ids':
               parent_behavior_taxonomy_ids, 'sort_by': sort_by,
               'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/behavior_taxonomies'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-behavior-taxonomies',
                           binding)


def behaviors(*, behavior_ids=_ELIDE, count=_ELIDE, country_code=_ELIDE,
              cursor=_ELIDE, sort_by=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieves all valid behaviors defined by partner audiences that can be
    targeted by an advertiser.

    :param behavior_ids: Scope the response to just the desired behaviors by
        specifying a comma-separated list of identifiers. Up to 200 IDs may be
        provided. Type: string Example: lfrt

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param country_code: An optional query to scope a targeting criteria search
        to a specific country with the 2 letter ISO country code. If this
        parameter is not specified only partner audiences for the United States
        are returned. Type: string Default: US

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'behavior_ids': behavior_ids, 'count': count, 'country_code':
               country_code, 'cursor': cursor, 'sort_by': sort_by,
               'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/behaviors'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-behaviors',
                           binding)


def devices(*, count=_ELIDE, q=_ELIDE):
    """
    Discover available device-based targeting criteria for Promoted Products.
    Device targeting is available for Promoted Tweets.

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param q: An optional query to scope a targeting criteria. Omit this
        parameter to retrive all. Type: string Example: apple
    """
    binding = {'count': count, 'q': q}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/devices'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-devices',
                           binding)


def events(event_types, *, count=_ELIDE, country_code=_ELIDE, cursor=_ELIDE,
           end_time=_ELIDE, ids=_ELIDE, start_time=_ELIDE):
    """
    Discover available event-based targeting criteria for Promoted Products.
    Only one event can be targeted per line item.

    :param event_types: An optional query to scope to certain event types.
        Type: enum Possible values: CONFERENCE, HOLIDAY,
        MUSIC_AND_ENTERTAINMENT, OTHER, SPORTS

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param country_code: An optional query to scope a targeting criteria search
        to a specific country with the 2 letter ISO country code. If this
        parameter is not specified only partner audiences for the United States
        are returned. Type: string Default: US

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param end_time: The time, expressed in ISO 8601, that the campaign will
        end. Type: string Example: 2017-10-05T00:00:00Z

    :param ids: Scope the response to just the desired events by specifying a
        comma-separated list of identifiers. Up to 200 IDs may be provided.
        Type: string Example: lex

    :param start_time: The time, expressed in ISO 8601, that the line item will
        begin serving. Note: Defaults to the current time. Type: string
        Example: 2017-07-05T00:00:00Z
    """
    binding = {'event_types': event_types, 'count': count, 'country_code':
               country_code, 'cursor': cursor, 'end_time': end_time, 'ids':
               ids, 'start_time': start_time}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/events'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-events',
                           binding)


def interests():
    """
    Discover available interest-based targeting criteria for Promoted Products.
    Interests change infrequently, however we suggest you refresh this list at
    least once weekly.
    """
    binding = {}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/interests'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-interests',
                           binding)


def languages(*, count=_ELIDE, cursor=_ELIDE, q=_ELIDE):
    """
    Discover languages available for targeting.

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param q: An optional query to scope a targeting criteria. Omit this
        parameter to retrive all. Type: string Example: english
    """
    binding = {'count': count, 'cursor': cursor, 'q': q}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/languages'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-languages',
                           binding)


def locations(*, count=_ELIDE, country_code=_ELIDE, cursor=_ELIDE,
              location_type=_ELIDE, q=_ELIDE):
    """
    Discover available location-based targeting criteria for Promoted Products.
    Geo-targeting is available for Promoted Accounts and Promoted Tweets at the
    country level, state/region level, city level, and postal code level.
    Postal code targeting must be used if you wish to retrieve analytics at the
    postal code level.

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param country_code: An optional query to scope a targeting criteria search
        to a specific country with the 2 letter ISO country code. Omit this
        parameter to retrieve results for all countries. Type: string Example:
        JP

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param location_type: Scope the results by a specific kind of location.
        More granular targeting than COUNTRIES may not be available in all
        locations. Type: enum Possible values: COUNTRIES, REGIONS, METROS,
        CITIES, POSTAL_CODES

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results. Type: string Example: New York
    """
    binding = {'count': count, 'country_code': country_code, 'cursor': cursor,
               'location_type': location_type, 'q': q}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/locations'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-locations',
                           binding)


def network_operators(*, country_code=_ELIDE, q=_ELIDE, count=_ELIDE,
                      cursor=_ELIDE):
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
    url = 'https://ads-api.twitter.com/2/targeting_criteria/network_operators'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-network-operators',
                           binding)


def platform_versions(*, q=_ELIDE):
    """
    Discover available mobile-OS-version-based targeting criteria for Promoted
    Products. Platform version targeting is available for Promoted Accounts and
    Promoted Tweets. This allows targeting down to the point release of a
    mobile operating system version, for example iOS 7.1, Android 4.4

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to retrieve all results.
    """
    binding = {'q': q}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/platform_versions'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-platform-versions',
                           binding)


def platforms(*, count=_ELIDE, q=_ELIDE, lang=_ELIDE):
    """
    Discover available platform-based targeting criteria for Promoted Products.

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param q: An optional query to scope a targeting criteria search. Omit this
        parameter to this parameter to retrieve all results. Type: string
        Examples: ios, blackberry

    :param lang: Using a ISO-639-1 language code. When passed, an additional
        localized_name attribute will be returned in the response. Type: int,
        string Example: fr
    """
    binding = {'count': count, 'q': q, 'lang': lang}
    url = 'https://ads-api.twitter.com/2/targeting_criteria/platforms'
    return _TwitterRequest('GET',
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
    url = 'https://ads-api.twitter.com/2/targeting_criteria/tv_markets'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-tv-markets',
                           binding)


def tv_shows(tv_market_locale, *, q=_ELIDE, count=_ELIDE, cursor=_ELIDE):
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
    url = 'https://ads-api.twitter.com/2/targeting_criteria/tv_shows'
    return _TwitterRequest('GET',
                           url,
                           'ads:targeting_criteria',
                           'get-targeting-criteria-tv-shows',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/app_store_categories'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/app_store_categories'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/behavior_taxonomies'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/behavior_taxonomies'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/behaviors'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/behaviors'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/devices'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/devices'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/events'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/events'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/interests'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/interests'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/languages'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/languages'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/locations'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/locations'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/network_operators'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/network_operators'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/platform_versions'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/platform_versions'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/platforms'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/platforms'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/tv_markets'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/tv_markets'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/targeting_criteria/tv_shows'] = 'https://dev.twitter.com/ads/reference/get/targeting_criteria/tv_shows'

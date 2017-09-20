###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def accounts_account_id(account_id, audience_type, *, audience_values=_ELIDE,
                        interaction_type=_ELIDE):
    """
    Retrieve insights for specific account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param audience_type: The audience or set of people you’d like more
        insights on. See Ads Enumerations for more information. Type: enum
        Possible Values: ALL_ON_TWITTER, APP, CAMPAIGN, ORGANIC

    :param audience_values: The identifier (ID) of the available audience set
        requested. Availability depends on the audience_type. Required for
        ORGANIC. Type: string Example: 702

    :param interaction_type: The type of interaction captured for the available
        audience set requested. on the audience_type. Required for ORGANIC.
        Type: enum Possible Values: CONVERSION, ENGAGEMENT, IMPRESSION
    """
    binding = {'account_id': account_id, 'audience_type': audience_type,
               'audience_values': audience_values, 'interaction_type':
               interaction_type}
    url = 'https://ads-api.twitter.com/2/insights/accounts/:account_id'
    return _TwitterRequest('GET',
                           url,
                           'ads:insights',
                           'get-insights-accounts-account-id',
                           binding)


def accounts_available_audiences_by_account_id(account_id):
    """
    Retrieve available audiences for this account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t
    """
    binding = {'account_id': account_id}
    url = 'https://ads-api.twitter.com/2/insights/accounts/{account_id}/available_audiences'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:insights',
                           'get-insights-accounts-account-id-available-audiences',
                           binding)


def keywords_search(end_time, granularity, start_time, *, keywords=_ELIDE,
                    location=_ELIDE, negative_keywords=_ELIDE):
    """
    Given a group of keywords, get the associated tweet volume for up to 7
    days.

    :param end_time: Scopes the retrieved data to data collected in the window
        of time between start_time and end_time. If not set, this defaults to
        the time of the request. Expressed in ISO 8601. Type: string Example:
        2015-07-06T07:59:00Z

    :param granularity: Specifies the granularity of the data returned for the
        time range denoted by start_time and end_time. For instance, when set
        to HOUR, you will be presented with a datapoint for each hour between
        start_time and end_time. request. Type: enum Possible values: DAY, HOUR

    :param start_time: Scopes the retrieved data to data collected in the
        window of time between start_time and end_time. Expressed in ISO 8601.
        Type: string Example: 2015-07-06T07:59:00Z

    :param keywords: A comma-separated string of keywords to narrow search by.
        All keywords are OR’ed with one another. A maximum of 10 keywords and
        negative_keywords (combined) may be used. Type: string Example: good
        happy shiny

    :param location: A targeting value you would get from the GET
        targeting_criteria/_locations endpoint to narrow results in terms of
        where the user of the account is located. Note that at present only
        country level locations are supported. Type: string Example:
        0ce8b9a7b2742f7e

    :param negative_keywords: A comma-separated string of keywords to exclude
        (black list). All negative keywords are OR’ed with one another. A
        maximum of 10 keywords and negative_keywords (combined) may be used.
        Type: string Example: horrible bad
    """
    binding = {'end_time': end_time, 'granularity': granularity, 'start_time':
               start_time, 'keywords': keywords, 'location': location,
               'negative_keywords': negative_keywords}
    url = 'https://ads-api.twitter.com/2/insights/keywords/search'
    return _TwitterRequest('GET',
                           url,
                           'ads:insights',
                           'get-insights-keywords-search',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/insights/accounts/:account_id'] = 'https://dev.twitter.com/ads/reference/get/insights/accounts/account_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/insights/accounts/{account_id}/available_audiences'] = 'https://dev.twitter.com/ads/reference/get/insights/accounts/account_id/available_audiences'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/insights/keywords/search'] = 'https://dev.twitter.com/ads/reference/get/insights/keywords/search'

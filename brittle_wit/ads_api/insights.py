###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def accounts_account_id(account_id, audience_type, audience_valuesometimes,
                        interaction_typesometimes):
    """
    Retrieve insights for specific account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param audience_type: Example Values : ALL_ON_TWITTER

    :param audience_valuesometimes: The identifier (ID) of the available
        audience set requested. Availability depends on the audience_type.
        Required for ORGANIC.

    :param interaction_typesometimes: The type of interaction captured for the
        available audience set requested. Required for ORGANIC. See Ads
        Enumerations for possible values.
    """
    binding = {'account_id': account_id, 'audience_type': audience_type,
               'audience_valuesometimes': audience_valuesometimes,
               'interaction_typesometimes': interaction_typesometimes}
    url = 'https://ads-api.twitter.com/1/insights/accounts/:account_id'
    return TwitterRequest('GET',
                          url,
                          'ads:insights',
                          'get-insights-accounts-account-id',
                          binding)


def accounts_available_audiences_by_account_id(account_id):
    """
    Retrieve available audiences for this account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.
    """
    binding = {'account_id': account_id}
    url = 'https://ads-api.twitter.com/1/insights/accounts/{account_id}/available_audiences'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:insights',
                          'get-insights-accounts-account-id-available-audiences',
                          binding)


def keywords_search(granularity, start_time, *, end_time=ELIDE,
                    keywords=ELIDE, negative_keywords=ELIDE, location=ELIDE):
    """
    Given a group of keywords, get the associated tweet volume for up to 7
    days.

    :param granularity: Specifies the granularity of the data returned for the
        time range denoted by start_time and end_time. For instance, when set
        to HOUR, you will be presented with a datapoint for each hour between
        start_time and end_time. Possible values include: DAY, HOUR.

    :param start_time: Scopes the retrieved data to data collected in the
        window of time between start_time and end_time. Expressed in ISO 8601.

    :param end_time: Scopes the retrieved data to data collected in the window
        of time between start_time and end_time. If not set, this defaults to
        the time of the request. Expressed in ISO 8601.

    :param keywords: A comma-separated string of keywords to narrow search by.
        All keywords are OR’ed with one another. A maximum of 10 keywords and
        negative_keywords (combined) may be used.

    :param negative_keywords: A comma-separated string of keywords to exclude
        (black list). All negative keywords are OR’ed with one another. A
        maximum of 10 keywords and negative_keywords (combined) may be used.

    :param location: A targeting value you would get from the GET
        targeting_criteria/locations endpoint to narrow results in terms of
        where the user of the account is located. Note that at present only
        country level locations are supported.
    """
    binding = {'granularity': granularity, 'start_time': start_time,
               'end_time': end_time, 'keywords': keywords,
               'negative_keywords': negative_keywords, 'location': location}
    url = 'https://ads-api.twitter.com/1/insights/keywords/search'
    return TwitterRequest('GET',
                          url,
                          'ads:insights',
                          'get-insights-keywords-search',
                          binding)



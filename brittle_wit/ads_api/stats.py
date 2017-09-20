###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def accounts_by_account_id(account_id, end_time, entity, entity_ids,
                           granularity, metric_groups, placement, start_time):
    """
    Retrieve synchronous analytics for the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param end_time: Scopes the retrieved data to the specified end time,
        expressed in ISO 8601. Note: Must be expressed in whole hours (0
        minutes and 0 seconds). Type: string Example: 2017-05-26T07:00:00Z

    :param entity: The entity type to retrieve data for. Type: enum Possible
        values: ACCOUNT, CAMPAIGN, FUNDING_INSTRUMENT, LINE_ITEM,
        ORGANIC_TWEET, PROMOTED_TWEET

    :param entity_ids: The specific entities to retrieve data for. Specify a
        comma-separated list of entity IDs. Note: Up to 20 entity IDs may be
        provided. Type: string Example: 8u94t

    :param granularity: Specify how granular the retrieved data should be.
        Type: enum Possible values: DAY, HOUR, TOTAL

    :param metric_groups: The specific metrics that should be returned. Specify
        a comma-separated list of metric groups. For more information see
        Metrics and Segmentation. Note: MOBILE_CONVERSION data should be
        requested separately. Type: enum Possible values: BILLING, ENGAGEMENT,
        LIFE_TIME_VALUE_MOBILE_CONVERSION, MEDIA, MOBILE_CONVERSION, VIDEO,
        WEB_CONVERSION

    :param placement: Scopes the retrieved data to a particular placement.
        Note: Only a single value accepted per request. For entities with both
        Twitter and Twitter Audience Platform placement, separate requests are
        required, one for each placement value. Type: enum Possible values:
        ALL_ON_TWITTER, PUBLISHER_NETWORK

    :param start_time: Scopes the retrieved data to the specified start time,
        expressed in ISO 8601. Note: Must be expressed in whole hours (0
        minutes and 0 seconds). Type: string Example: 2017-05-19T07:00:00Z
    """
    binding = {'account_id': account_id, 'end_time': end_time, 'entity':
               entity, 'entity_ids': entity_ids, 'granularity': granularity,
               'metric_groups': metric_groups, 'placement': placement,
               'start_time': start_time}
    url = 'https://ads-api.twitter.com/2/stats/accounts/{account_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:stats',
                           'get-stats-accounts-account-id',
                           binding)


def accounts_reach_campaigns_by_account_id(account_id, campaign_ids,
                                           end_time, start_time):
    """
    Retrieve reach and average frequency analytics for specified campaigns.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param campaign_ids: Scope the response to just the desired campaigns by
        specifying a comma-separated list of identifiers. Up to 20 IDs may be
        provided. Note: Up to 20 campaign IDs may be provided. Type: string
        Example: 8fgzf

    :param end_time: Scopes the retrieved data to the specified end time,
        expressed in ISO 8601. Note: Must be expressed in whole hours (0
        minutes and 0 seconds). Type: string Example: 2017-05-26T07:00:00Z

    :param start_time: Scopes the retrieved data to the specified start time,
        expressed in ISO 8601. Note: Must be expressed in whole hours (0
        minutes and 0 seconds). Type: string Example: 2017-05-19T07:00:00Z
    """
    binding = {'account_id': account_id, 'campaign_ids': campaign_ids,
               'end_time': end_time, 'start_time': start_time}
    url = 'https://ads-api.twitter.com/stats/accounts/{account_id}/reach/campaigns'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:stats',
                           'get-stats-accounts-account-id-reach-campaigns',
                           binding)


def accounts_reach_funding_instruments_by_account_id(account_id,
                                                     funding_instrument_ids,
                                                     end_time, start_time):
    """
    Retrieve reach and average frequency analytics for specified funding
    instruments.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param funding_instrument_ids: Scope the response to just the desired
        funding instruments by specifying a comma-separated list of
        identifiers. Up to 20 IDs may be provided. Note: Up to 20 funding
        instrument IDs may be provided. Type: string Example: lygyi

    :param end_time: Scopes the retrieved data to the specified end time,
        expressed in ISO 8601. Note: Must be expressed in whole hours (0
        minutes and 0 seconds). Type: string Example: 2017-05-26T07:00:00Z

    :param start_time: Scopes the retrieved data to the specified start time,
        expressed in ISO 8601. Note: Must be expressed in whole hours (0
        minutes and 0 seconds). Type: string Example: 2017-05-19T07:00:00Z
    """
    binding = {'account_id': account_id, 'funding_instrument_ids':
               funding_instrument_ids, 'end_time': end_time, 'start_time':
               start_time}
    url = 'https://ads-api.twitter.com/stats/accounts/{account_id}/reach/funding_instruments'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:stats',
                           'get-stats-accounts-account-id-reach-funding-instruments',
                           binding)


def jobs_accounts_by_account_id(account_id, *, count=_ELIDE, cursor=_ELIDE,
                                job_ids=_ELIDE):
    """
    Retrieve details for some or all asynchronous analytics job for the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param job_ids: Scope the response to just the desired jobs by specifying a
        comma-separated list of identifiers. Up to 200 IDs may be provided.
        Type: long Example: 883787505404747776
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'job_ids': job_ids}
    url = 'https://ads-api.twitter.com/2/stats/jobs/accounts/{account_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:stats',
                           'get-stats-jobs-accounts-account-id',
                           binding)


def jobs_summaries(*, count=_ELIDE, cursor=_ELIDE):
    """
    Retrieve a summary of each existing asynchronous analytics job associated
    with the client app ID making the request. This endpoint is meant for
    internal / debugging purposes only.

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example:
        885662364120399872_4503599658438113
    """
    binding = {'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/2/stats/jobs/summaries'
    return _TwitterRequest('GET',
                           url,
                           'ads:stats',
                           'get-stats-jobs-summaries',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/stats/accounts/{account_id}'] = 'https://dev.twitter.com/ads/reference/get/stats/accounts/account_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/stats/accounts/{account_id}/reach/campaigns'] = 'https://dev.twitter.com/ads/reference/get/stats/accounts/account_id/reach/campaigns'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/stats/accounts/{account_id}/reach/funding_instruments'] = 'https://dev.twitter.com/ads/reference/get/stats/accounts/account_id/reach/funding_instruments'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/stats/jobs/accounts/{account_id}'] = 'https://dev.twitter.com/ads/reference/get/stats/jobs/accounts/account_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/stats/jobs/summaries'] = 'https://dev.twitter.com/ads/reference/get/stats/jobs/summaries'

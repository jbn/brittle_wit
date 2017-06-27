###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, ELIDE


def accounts_reach_campaigns_by_account_id(account_id, campaign_ids,
                                           start_time, *, end_time=ELIDE):
    """
    Retrieve summary about reach and average frequency of specified campaigns
    during a specified time period.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param campaign_ids: The comma-separated list of up to 20 identifiers for
        campaigns associated with the current account.

    :param start_time: Scopes the retrieved data to data collected in the
        window of time between start_time and end_time. Expressed in ISO 8601.

    :param end_time: Scopes the retrieved data to data collected in the window
        of time between start_time and end_time. Expressed in ISO 8601.
    """
    binding = {'account_id': account_id, 'campaign_ids': campaign_ids,
               'start_time': start_time, 'end_time': end_time}
    url = 'https://ads-api.twitter.com/stats/accounts/{account_id}/reach/campaigns'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:stats',
                          'get-stats-accounts-account-id-reach-campaigns',
                          binding)


def accounts_reach_funding_instruments_by_account_id(account_id,
                                                     funding_instrument_ids,
                                                     start_time, *,
                                                     end_time=ELIDE):
    """
    Retrieve summary about reach and average frequency of specified funding
    instruments during a specified time period.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param funding_instrument_ids: The comma-separated list of up to 20
        identifiers for funding instruments associated with the current
        account.

    :param start_time: Scopes the retrieved data to data collected in the
        window of time between start_time and end_time. Expressed in ISO 8601.

    :param end_time: Scopes the retrieved data to data collected in the window
        of time between start_time and end_time. Expressed in ISO 8601.
    """
    binding = {'account_id': account_id, 'funding_instrument_ids':
               funding_instrument_ids, 'start_time': start_time, 'end_time':
               end_time}
    url = 'https://ads-api.twitter.com/stats/accounts/{account_id}/reach/funding_instruments'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:stats',
                          'get-stats-accounts-account-id-reach-funding-instruments',
                          binding)


def accounts_by_account_id(account_id, entity, entity_ids, start_time,
                           end_time, metric_groups, placement, *,
                           granularity=ELIDE):
    """
    Retrieve synchronous summary analytics about any

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param entity: The entity to query. For the possible values, see
        enumerations (look under Analytics - v1)

    :param entity_ids: A comma-separated list of entity ids for the entity, up
        to a maximum of 20.

    :param start_time: Scopes the retrieved data to data collected in the
        window of time between start_time and end_time. Expressed in ISO 8601.
        Must be expressed in whole hours (0 minutes and 0 seconds).

    :param end_time: Scopes the retrieved data to data collected in the window
        of time between start_time and end_time. Expressed in ISO 8601. Must be
        expressed in whole hours (0 minutes and 0 seconds).

    :param granularity: Determines how granular the data points will be
        returned for each data point type within the time range specified by
        start_time and end_time. For instance, when set to HOUR, you will be
        presented with a datapoint for each hour between start_time and
        end_time. Possible values include: TOTAL, DAY, HOUR. Defaults to HOUR.

    :param metric_groups: A comma-separated list of the metric groups you want
        to get back. For the possible values, see enumerations

    :param placement: The placement - for the possible values, see enumerations
    """
    binding = {'account_id': account_id, 'entity': entity, 'entity_ids':
               entity_ids, 'start_time': start_time, 'end_time': end_time,
               'granularity': granularity, 'metric_groups': metric_groups,
               'placement': placement}
    url = 'https://ads-api.twitter.com/1/stats/accounts/{account_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:stats',
                          'get-1-stats-accounts-account-id',
                          binding)


def jobs_accounts_by_account_id(account_id, *, count=ELIDE, cursor=ELIDE,
                                job_ids=ELIDE):
    """
    Retrieve details of asynchronous analytics query jobs.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param job_ids: Scope the response to just the desired jobs by specifying a
        comma-separated list of job identifiers.
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'job_ids': job_ids}
    url = 'https://ads-api.twitter.com/1/stats/jobs/accounts/{account_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:stats',
                          'get-1-stats-jobs-accounts-account-id',
                          binding)


def jobs_accounts_by_account_id(placement, metric_groups, start_time, entity,
                                end_time, granularity, *, account_id=ELIDE,
                                country=ELIDE, platform=ELIDE,
                                entity_ids=ELIDE, segmentation_type=ELIDE):
    """
    Create an asynchronous analytics job for a given ads account. A

    :param placement:  (enum)

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param metric_groups:  (enum)

    :param country:  (GeoId)

    :param start_time:  (Time)

    :param entity:  (enum)

    :param platform:  (an id)

    :param end_time:  (Time)

    :param granularity:  (enum)

    :param entity_ids:  (String)

    :param segmentation_type:  (enum)
    """
    binding = {'placement': placement, 'account_id': account_id,
               'metric_groups': metric_groups, 'country': country,
               'start_time': start_time, 'entity': entity, 'platform':
               platform, 'end_time': end_time, 'granularity': granularity,
               'entity_ids': entity_ids, 'segmentation_type':
               segmentation_type}
    url = 'https://ads-api.twitter.com/1/stats/jobs/accounts/{account_id}'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:stats',
                          'post-1-stats-jobs-accounts-account-id',
                          binding)


def jobs_accounts_by_job_id_and_account_id(job_id, account_id):
    """
    Cancel an asynchronous analytics job for a given ads account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param job_id: A reference to the job you are operating with in the
        request.
    """
    binding = {'account_id': account_id, 'job_id': job_id}
    url = 'https://ads-api.twitter.com/1/stats/jobs/accounts/{account_id}/{job_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:stats',
                          'delete-1-stats-jobs-accounts-account-id-job-id',
                          binding)



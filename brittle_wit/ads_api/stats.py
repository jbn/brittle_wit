###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def accounts_reach_campaigns_by_account_id(account_id, campaign_ids, start_time, *, end_time=IGNORE):
    """
    Retrieve summary about reach and average frequency of specified campaigns
    during a specified time period.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param campaign_ids: The comma-separated list of up to 20 identifiers for c
        ampaigns associated with the current account. (True)
    
    
    :param start_time: Scopes the retrieved data to data collected in the windo
        w of time between start_time and end_time. Expressed in ISO 8601.
        (True)
    
    
    :param end_time: Scopes the retrieved data to data collected in the window 
        of time between start_time and end_time. Expressed in ISO 8601. (False)
    """
    url = "https://ads-api.twitter.com/stats/accounts/{account_id}/reach/campaigns"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:STATS',
                          'GET-STATS-ACCOUNTS-ACCOUNT-ID-REACH-CAMPAIGNS',
                          account_id=account_id
                          campaign_ids=campaign_ids
                          start_time=start_time
                          end_time=end_time)


def accounts_reach_funding_instruments_by_account_id(account_id, funding_instrument_ids, start_time, *, end_time=IGNORE):
    """
    Retrieve summary about reach and average frequency of specified funding
    instruments during a specified time period.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param funding_instrument_ids: The comma-separated list of up to 20 identif
        iers for funding instruments associated with the current account.
        (True)
    
    
    :param start_time: Scopes the retrieved data to data collected in the windo
        w of time between start_time and end_time. Expressed in ISO 8601.
        (True)
    
    
    :param end_time: Scopes the retrieved data to data collected in the window 
        of time between start_time and end_time. Expressed in ISO 8601. (False)
    """
    url = "https://ads-api.twitter.com/stats/accounts/{account_id}/reach/funding_instruments"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:STATS',
                          'GET-STATS-ACCOUNTS-ACCOUNT-ID-REACH-FUNDING-INSTRUMENTS',
                          account_id=account_id
                          funding_instrument_ids=funding_instrument_ids
                          start_time=start_time
                          end_time=end_time)


def accounts_by_account_id(account_id, entity, entity_ids, start_time, end_time, metric_groups, placement, *, granularity=IGNORE):
    """
    Retrieve synchronous summary analytics about any
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param entity: The entity to query. For the possible values, see enumeratio
        ns (look under Analytics - v1) (True)
    
    
    :param entity_ids: A comma-separated list of entity ids for the entity, up 
        to a maximum of 20. (True)
    
    
    :param start_time: Scopes the retrieved data to data collected in the windo
        w of time between start_time and end_time. Expressed in ISO 8601. Must
        be expressed in whole hours (0 minutes and 0 seconds). (True)
    
    
    :param end_time: Scopes the retrieved data to data collected in the window 
        of time between start_time and end_time. Expressed in ISO 8601. Must be
        expressed in whole hours (0 minutes and 0 seconds). (True)
    
    
    :param granularity: Determines how granular the data points will be returne
        d for each data point type within the time range specified by
        start_time and end_time. For instance, when set to HOUR, you will be
        presented with a datapoint for each hour between start_time and
        end_time. Possible values include: TOTAL, DAY, HOUR. Defaults to HOUR.
        (False)
    
    
    :param metric_groups: A comma-separated list of the metric groups you want 
        to get back. For the possible values, see enumerations (True)
    
    
    :param placement: The placement - for the possible values, see enumerations
        (True)
    """
    url = "https://ads-api.twitter.com/1/stats/accounts/{account_id}"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:STATS',
                          'GET-1-STATS-ACCOUNTS-ACCOUNT-ID',
                          account_id=account_id
                          entity=entity
                          entity_ids=entity_ids
                          start_time=start_time
                          end_time=end_time
                          granularity=granularity
                          metric_groups=metric_groups
                          placement=placement)


def jobs_accounts_by_account_id(account_id, *, count=IGNORE, cursor=IGNORE, job_ids=IGNORE):
    """
    Retrieve details of asynchronous analytics query jobs.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param job_ids: Scope the response to just the desired jobs by specifying a
        comma-separated list of job identifiers. (False)
    """
    url = "https://ads-api.twitter.com/1/stats/jobs/accounts/{account_id}"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:STATS',
                          'GET-1-STATS-JOBS-ACCOUNTS-ACCOUNT-ID',
                          account_id=account_id
                          count=count
                          cursor=cursor
                          job_ids=job_ids)


def jobs_accounts_by_account_id(placement, metric_groups, start_time, entity, end_time, granularity, *, account_id=IGNORE, country=IGNORE, platform=IGNORE, entity_ids=IGNORE, segmentation_type=IGNORE):
    """
    Create an asynchronous analytics job for a given ads account. A
    
    :param placement:  (True)
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (False)
    
    
    :param metric_groups:  (True)
    
    :param country:  (False)
    
    :param start_time:  (True)
    
    :param entity:  (True)
    
    :param platform:  (False)
    
    :param end_time:  (True)
    
    :param granularity:  (True)
    
    :param entity_ids:  (False)
    
    :param segmentation_type:  (False)
    """
    url = "https://ads-api.twitter.com/1/stats/jobs/accounts/{account_id}"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:STATS',
                          'POST-1-STATS-JOBS-ACCOUNTS-ACCOUNT-ID',
                          placement=placement
                          account_id=account_id
                          metric_groups=metric_groups
                          country=country
                          start_time=start_time
                          entity=entity
                          platform=platform
                          end_time=end_time
                          granularity=granularity
                          entity_ids=entity_ids
                          segmentation_type=segmentation_type)


def jobs_accounts_by_job_id_and_account_id(job_id, account_id):
    """
    Cancel an asynchronous analytics job for a given ads account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param job_id: A reference to the job you are operating with in the request
        . (True)
    """
    url = "https://ads-api.twitter.com/1/stats/jobs/accounts/{account_id}/{job_id}"
    url = url.format(job_id=job_id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:STATS',
                          'DELETE-1-STATS-JOBS-ACCOUNTS-ACCOUNT-ID-JOB-ID',
                          account_id=account_id
                          job_id=job_id)



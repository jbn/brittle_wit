###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def accounts_campaigns_by_account_id(account_id):
    """
    Allows the batch creation of new
    """
    url = "https://ads-api.twitter.com/1/batch/accounts/{account_id}/campaigns"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:BATCH',
                          'POST-BATCH-ACCOUNTS-ACCOUNT-ID-CAMPAIGNS',
                          account_id=account_id)


def accounts_line_items_by_account_id(account_id):
    """
    Allows the batch creation of new
    """
    url = "https://ads-api.twitter.com/1/batch/accounts/{account_id}/line_items"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:BATCH',
                          'POST-BATCH-ACCOUNTS-ACCOUNT-ID-LINE-ITEMS',
                          account_id=account_id)


def accounts_tailored_audiences_by_account_id(account_id, operation_type, params, name, audience_type, child_segments, boolean_operatorsometimes, tailored_audience_idsometimes, lookback_windowsometimes, *, segments=IGNORE, frequency=IGNORE, frequency_comparator=IGNORE, negate=IGNORE):
    """
    Allows for batch creation of tailored audiences. See the
    
    :param operation_type: The per item operation type being performed. (True)
    
    :param params: A JSON object containing all params for the Campaign object.
        Please see here for a list of required an optional Campaign
        parameters. (True)
    
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The display name for this audience. (True)
    
    :param audience_type: The type of audience to create. Currently, only audie
        nces of type FLEXIBLE can be created through this endpoint (True)
    
    
    :param segments: An array containing a boolean_operator and objects which d
        efine the subset of a tailored audience's members that you would like
        to target (each containing tailored_audience_id, frequency,
        frequency_comparator, lookback_window, negate and child_segments
        parameters as necessary). Only required if audience_type is set to
        FLEXIBLE. (False)
    
    
    :param child_segments: An array containing a boolean_operator and objects w
        hich define the subset of a tailored audience's members that you would
        like to target (each containing tailored_audience_id, frequency,
        frequency_comparator, lookback_window, negate and child_segments
        parameters as necessary). (True)
    
    
    :param boolean_operatorsometimes: The boolean relationship between the chil
        d segments in its parent (containing) object. Required if
        child_segments is non-empty for the parent object. (True)
    
    
    :param tailored_audience_idsometimes: The id of the tailored audience to us
        e as a child segment (True)
    
    
    :param lookback_windowsometimes: An integer value specifying the range of d
        ays within which the user has taken the specific action and qualified
        for the given tailored audience. Currently, only lookback windows
        values of 1, 7, 14, 30 are supported. (True)
    
    
    :param frequency: An integer value specifying the frequency within the look
        back window that the user has taken the specific action and qualified
        for the given tailored audience. Defaults to 1. (False)
    
    
    :param frequency_comparator: The comparison to make to the frequency passed
        in. Defaults to NUM_GTE (number greater than or equal). Possible
        values include: NUM_GT, NUM_GTE, NUM_EQ, NUM_LTE, NUM_LT (False)
    
    
    :param negate: Whether this segment should be negated and thus excluded in 
        the combination. Defaults to false (False)
    """
    url = "https://ads-api.twitter.com/1/batch/accounts/{account_id}/tailored_audiences"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:BATCH',
                          'POST-BATCH-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES',
                          operation_type=operation_type
                          params=params
                          account_id=account_id
                          name=name
                          audience_type=audience_type
                          segments=segments
                          child_segments=child_segments
                          boolean_operatorsometimes=boolean_operatorsometimes
                          tailored_audience_idsometimes=tailored_audience_idsometimes
                          lookback_windowsometimes=lookback_windowsometimes
                          frequency=frequency
                          frequency_comparator=frequency_comparator
                          negate=negate)


def accounts_targeting_criteria_by_account_id(account_id, operation_type, params):
    """
    Allows the batch creation of new
    
    :param operation_type: The per item operation type being performed. (True)
    
    :param params: A JSON object containing all params for the Targeting Criter
        ia object. Please see here for a list of required an optional Targeting
        Criteria parameters. (True)
    """
    url = "https://ads-api.twitter.com/1/batch/accounts/{account_id}/targeting_criteria"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:BATCH',
                          'POST-BATCH-ACCOUNTS-ACCOUNT-ID-TARGETING-CRITERIA',
                          operation_type=operation_type
                          params=params
                          account_id=account_id)



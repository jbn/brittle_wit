###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def accounts(*, with_deleted=IGNORE, sort_by=IGNORE):
    """
    Retrieve all of the advertising-enabled accounts the authenticating user
    has access to.
    
    :param with_deleted: Include deleted results for your request. Defaults to 
        false. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See sorting for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts"
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS',
                          with_deleted=with_deleted
                          sort_by=sort_by)


def by_account_id(account_id, *, with_deleted=IGNORE):
    """
    Retrieve detailed information on the specified account that the
    authenticating user has access to.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID',
                          account_id=account_id
                          with_deleted=with_deleted)


def account_media_by_account_id(account_id, *, count=IGNORE, sort_by=IGNORE, cursor=IGNORE, with_deleted=IGNORE, account_media_ids=IGNORE):
    """
    Retrieve account media for the specified ads account.
    
    :param count:  (False)
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param sort_by:  (False)
    
    :param cursor:  (False)
    
    :param with_deleted:  (False)
    
    :param account_media_ids:  (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/account_media"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-ACCOUNT-MEDIA',
                          count=count
                          account_id=account_id
                          sort_by=sort_by
                          cursor=cursor
                          with_deleted=with_deleted
                          account_media_ids=account_media_ids)


def account_media_by_id_and_account_id(id, account_id, *, count=IGNORE, sort_by=IGNORE, cursor=IGNORE, with_deleted=IGNORE, account_media_ids=IGNORE):
    """
    Retrieves details for specified account media associated to current ads
    account.
    
    :param count:  (False)
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param sort_by:  (False)
    
    :param cursor:  (False)
    
    :param with_deleted:  (False)
    
    :param account_media_ids:  (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/account_media/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-ACCOUNT-MEDIA-ID',
                          count=count
                          account_id=account_id
                          sort_by=sort_by
                          cursor=cursor
                          with_deleted=with_deleted
                          account_media_ids=account_media_ids
                          id=id)


def app_event_provider_configurations_by_account_id(account_id, *, with_deleted=IGNORE):
    """
    Retrieve all application event provider configurations associated with the
    current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_event_provider_configurations"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-APP-EVENT-PROVIDER-CONFIGURATIONS',
                          account_id=account_id
                          with_deleted=with_deleted)


def app_event_tags_by_account_id(account_id, *, with_deleted=IGNORE, sort_by=IGNORE):
    """
    Retrieve all application event tags associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-APP-EVENT-TAGS',
                          account_id=account_id
                          with_deleted=with_deleted
                          sort_by=sort_by)


def app_event_tags_by_id_and_account_id(id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve a specific application event tag associated with the current
    account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier for the application event tag. (True)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-APP-EVENT-TAGS-ID',
                          account_id=account_id
                          id=id
                          with_deleted=with_deleted)


def app_lists_by_account_id(account_id):
    """
    Retrieve details for all the app_lists associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_lists"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-APP-LISTS',
                          account_id=account_id)


def app_lists_by_app_list_id_and_account_id(app_list_id, account_id):
    """
    Retrieve details for an
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param app_list_id: Scope the response to just the desired app_list by spec
        ifying an identifier. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_lists/{app_list_id}"
    url = url.format(account_id=account_id,
                     app_list_id=app_list_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-APP-LISTS-APP-LIST-ID',
                          account_id=account_id
                          app_list_id=app_list_id)


def auction_insights_by_account_id(account_id, line_item_ids, start_time, end_time, granularity, placement):
    """
    Retrieve auction insights for specific line items belonging to the current
    account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_ids: Scope the response to just the desired line items by 
        specifying a comma-separated list of identifiers. Up to 50 ids may be
        provided. (True)
    
    
    :param start_time: Scopes the retrieved data to data collected in the windo
        w of time between start_time and end_time. Expressed in ISO 8601. This
        value must be aligned to midnight in the account's timezone. If no
        timestamp or offset is specified, the date will default to this
        timezone automatically. (True)
    
    
    :param end_time: Scopes the retrieved data to data collected in the window 
        of time between start_time and end_time. Expressed in ISO 8601. This
        value must be aligned to midnight in the account's timezone. If no
        timestamp or offset is specified, the date will default to this
        timezone automatically. (True)
    
    
    :param granularity: Determines how granular the data points will be returne
        d for each data point type within the time range specified by
        start_time and end_time. Possible values include: DAY, TOTAL. (True)
    
    
    :param placement: The placement - for the possible values, see enumerations
        (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/auction_insights"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-AUCTION-INSIGHTS',
                          account_id=account_id
                          line_item_ids=line_item_ids
                          start_time=start_time
                          end_time=end_time
                          granularity=granularity
                          placement=placement)


def authenticated_user_access_by_account_id(account_id):
    """
    Retrieve the permissions of the currently authenticated user (access_token)
    as they relate to this ads account.
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/authenticated_user_access"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-AUTHENTICATED-USER-ACCESS',
                          account_id=account_id)


def campaigns_by_account_id(account_id, *, campaign_ids=IGNORE, funding_instrument_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE, draft_only=IGNORE):
    """
    Retrieve details for some or all campaigns associated with the current
    account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param campaign_ids: Scope the response to just the desired campaigns by sp
        ecifying a comma-separated list of identifiers. Up to 50 ids may be
        provided. (False)
    
    
    :param funding_instrument_ids: Scope the response to just the desired fundi
        ng instruments by specifying a comma-separated list of identifiers. Up
        to 50 ids may be provided. (False)
    
    
    :param with_deleted: Include deleted results for your request. (False)
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See sorting for more information. (False)
    
    
    :param draft_only: Scope the response to just draft campaigns. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/campaigns"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CAMPAIGNS',
                          account_id=account_id
                          campaign_ids=campaign_ids
                          funding_instrument_ids=funding_instrument_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by
                          draft_only=draft_only)


def campaigns_by_campaign_id_and_account_id(campaign_id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve details for a specific campaign associated with the current
    account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param campaign_id: The identifier for a campaign associated with the curre
        nt account. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/campaigns/{campaign_id}"
    url = url.format(account_id=account_id,
                     campaign_id=campaign_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CAMPAIGNS-CAMPAIGN-ID',
                          account_id=account_id
                          campaign_id=campaign_id
                          with_deleted=with_deleted)


def cards_app_download_by_account_id(account_id, *, card_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE):
    """
    Retrieve card information about app download cards for a given account.
    This card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_ids: Include specific cards in your request. (False)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See Pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-APP-DOWNLOAD',
                          account_id=account_id
                          card_ids=card_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by)


def cards_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve card information about a given app download card. This card is
    part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-APP-DOWNLOAD-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_image_app_download_by_account_id(account_id, *, card_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE):
    """
    Retrieve card information about image app download cards for a given
    account. This card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_ids: Include specific cards in your request. (False)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See Pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-APP-DOWNLOAD',
                          account_id=account_id
                          card_ids=card_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by)


def cards_image_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve card information about a given image app download card. This card
    is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-APP-DOWNLOAD-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_image_conversation_by_account_id(account_id, *, card_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE):
    """
    Retrieve information about image conversation cards for a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_ids: Include specific cards in your request. (False)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See Pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-CONVERSATION',
                          account_id=account_id
                          card_ids=card_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by)


def cards_image_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve information about a given image conversation card.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-CONVERSATION-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_video_app_download_by_account_id(account_id, *, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Retrieve card information about all Video App Download Cards for the
    specified account. This card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param count: Specifies the number of Video App Download Card items to try 
        and retrieve. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of Video App Downloa
        d Cards. See Pagination for more information. (False)
    """
    url = "GET accounts/{account_id}/cards/video_app_download"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-APP-DOWNLOAD',
                          account_id=account_id
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor)


def cards_video_app_download_by_id_and_account_id(id, account_id):
    """
    Retrieve card information about a given Video App Download Card. This card
    is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier of the specific Video App Download Card to be upd
        ated. (True)
    """
    url = "GET accounts/{account_id}/cards/video_app_download/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-APP-DOWNLOAD-ID',
                          account_id=account_id
                          id=id)


def cards_video_conversation_by_account_id(account_id, *, card_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE):
    """
    Retrieve information about video conversation cards for a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_ids: Include specific cards in your request. (False)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See Pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-CONVERSATION',
                          account_id=account_id
                          card_ids=card_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by)


def cards_video_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve information about a given video conversation card.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-CONVERSATION-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_website_by_account_id(account_id, *, card_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE):
    """
    Retrieve card information about website cards for a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_ids: Include specific cards in your request. (False)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See Pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    """
    url = "GET accounts/{account_id}/cards/website"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-WEBSITE',
                          account_id=account_id
                          card_ids=card_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by)


def cards_website_by_card_id_and_account_id(account_id, *, card_id=IGNORE):
    """
    Retrieve card information about a given website card.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param card_id: The identifier for the specific card. (False)
    """
    url = "GET accounts/{account_id}/cards/website/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-CARDS-WEBSITE-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def features_by_account_id(account_id, *, feature_keys=IGNORE):
    """
    Retrieve the collection of whitelisted features accessible by this ads
    account. Features are indicated by a descriptive feature key and are only
    exposed on this endpoint if they are introduced in beta or an otherwise
    limited release and are available in the API. Features that do not meet
    this criteria will not be exposed on this endpoint.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param feature_keys: An optional parameter that enables querying for a spec
        ific feature key. Requests may include multiple comma-separated keys.
        Only the features that are accessible by this account will be included
        in the response. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/features"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-FEATURES',
                          account_id=account_id
                          feature_keys=feature_keys)


def funding_instruments_by_account_id(account_id, *, funding_instrument_ids=IGNORE, with_deleted=IGNORE, sort_by=IGNORE):
    """
    Retrieve some or all funding instruments associated with the account
    specified in the path.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param funding_instrument_ids: Scope the response to just the desired fundi
        ng instruments by specifying a comma-separated list of identifiers. Up
        to 50 ids may be provided. (False)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/funding_instruments"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-FUNDING-INSTRUMENTS',
                          account_id=account_id
                          funding_instrument_ids=funding_instrument_ids
                          with_deleted=with_deleted
                          sort_by=sort_by)


def funding_instruments_by_id_and_account_id(id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve a specific funding instrument associated with the account
    specified in the path.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier for a funding instrument associated with the curr
        ent account. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/funding_instruments/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-FUNDING-INSTRUMENTS-ID',
                          account_id=account_id
                          id=id
                          with_deleted=with_deleted)


def line_item_apps_by_account_id(account_id, *, line_item_id=IGNORE, line_item_app_ids=IGNORE, count=IGNORE, cursor=IGNORE, with_deleted=IGNORE):
    """
    Retrieve line item to mobile app associations
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_id: Scope response to a specific line item by providing it
        s identifier. (False)
    
    
    :param line_item_app_ids: Scope response to a set of line item apps (False)
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param with_deleted: Include deleted results for your request. Defaults to 
        false. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-LINE-ITEM-APPS',
                          account_id=account_id
                          line_item_id=line_item_id
                          line_item_app_ids=line_item_app_ids
                          count=count
                          cursor=cursor
                          with_deleted=with_deleted)


def line_item_apps_by_line_item_app_id_and_account_id(line_item_app_id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve a specific line item to mobile app association.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_app_id: The identifier for a line item app associated with
        the current account. (True)
    
    
    :param with_deleted: Include deleted results for your request. Defaults to 
        false. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps/{line_item_app_id}"
    url = url.format(account_id=account_id,
                     line_item_app_id=line_item_app_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-LINE-ITEM-APPS-LINE-ITEM-APP-ID',
                          account_id=account_id
                          line_item_app_id=line_item_app_id
                          with_deleted=with_deleted)


def line_items_by_account_id(account_id, *, campaign_ids=IGNORE, line_item_ids=IGNORE, funding_instrument_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE, draft_only=IGNORE):
    """
    Retrieve the line items associated with a specific campaign belonging to
    the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param campaign_ids: Scope the response to just the desired campaigns by sp
        ecifying a comma-separated list of identifiers. Up to 50 ids may be
        provided. (False)
    
    
    :param line_item_ids: Scope the response to just the desired line items by 
        specifying a comma-separated list of identifiers. Up to 50 ids may be
        provided. (False)
    
    
    :param funding_instrument_ids: Scope the response to just the desired fundi
        ng instruments by specifying a comma-separated list of identifiers. Up
        to 50 ids may be provided. (False)
    
    
    :param with_deleted: Include deleted results for your request. (False)
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See sorting for more information. (False)
    
    
    :param draft_only: Scope the response to just draft line items. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_items"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-LINE-ITEMS',
                          account_id=account_id
                          campaign_ids=campaign_ids
                          line_item_ids=line_item_ids
                          funding_instrument_ids=funding_instrument_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by
                          draft_only=draft_only)


def line_items_by_line_item_id_and_account_id(line_item_id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve a specific line item associated with a campaign belonging to the
    current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_id: A reference to the line item you are operating with in
        the request. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_items/{line_item_id}"
    url = url.format(account_id=account_id,
                     line_item_id=line_item_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-LINE-ITEMS-LINE-ITEM-ID',
                          account_id=account_id
                          line_item_id=line_item_id
                          with_deleted=with_deleted)


def media_creatives_by_account_id(account_id, *, draft_only=IGNORE):
    """
    Retrieve details for all the media_creatives associated with the current
    account.
    
    :param draft_only: Scope the response to media creatives under draft campai
        gns. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-MEDIA-CREATIVES',
                          draft_only=draft_only
                          account_id=account_id)


def media_creatives_by_id_and_account_id(id, account_id):
    """
    Retrieves details for a specific media creative associated with the current
    account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier for a media_creative associated with the current 
        account. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-MEDIA-CREATIVES-ID',
                          account_id=account_id
                          id=id)


def preroll_call_to_actions_by_account_id(account_id, line_item_id, *, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, draft_only=IGNORE):
    """
    Get the Call-to-Actions (CTAs) associated with line items on this account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_id: Filter results to a specific line_item_id. (True)
    
    :param with_deleted: Include deleted results for your request. (False)
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param draft_only: Scope the response to CTAs associated with line items un
        der draft campaigns. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-PREROLL-CALL-TO-ACTIONS',
                          account_id=account_id
                          line_item_id=line_item_id
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          draft_only=draft_only)


def preroll_call_to_actions_preroll_call_to_action_id_by_account_id(account_id, line_item_id, *, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Retrieve a specific Call-to-Action (CTAs) associated with this account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_id: Filter results to a specific line_item_id. (True)
    
    :param with_deleted: Include deleted results for your request. Defaults to 
        false. (False)
    
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions/:preroll_call_to_action_id"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-PREROLL-CALL-TO-ACTIONS-PREROLL-CALL-TO-ACTION-ID',
                          account_id=account_id
                          line_item_id=line_item_id
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor)


def promotable_users_by_account_id(account_id, *, with_deleted=IGNORE):
    """
    Returns the collection of promotable_users associated with an account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/promotable_users"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-PROMOTABLE-USERS',
                          account_id=account_id
                          with_deleted=with_deleted)


def promoted__by_account_id(account_id, *, line_item_id=IGNORE, promoted_account_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE, draft_only=IGNORE):
    """
    Retrieve references to the Promoted Accounts associated with one or more
    line items.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_id: A reference to the line item you are operating with in
        the request. Omitting the line_item_id will return all promoted
        accounts across all campaigns. (False)
    
    
    :param promoted_account_ids: Scope the response to the specified, comma-sep
        arated list of promoted account IDs. These identifiers refer to a
        associated Promoted Account with a line item. This comes from the id
        field from a response item to GET
        accounts/:account_id/promoted_accounts. Supplied within the resource's
        path. (False)
    
    
    :param with_deleted: Include deleted results in your request. (False)
    
    :param count: Specifies the number of Promoted Accounts to try to retrieve,
        up to a maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of Promoted Accounts
        . See Pagination for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See Sorting for more information. (False)
    
    
    :param draft_only: Scope the response to Promoted Accounts under draft camp
        aigns. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/promoted_accounts"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-PROMOTED-ACCOUNTS',
                          account_id=account_id
                          line_item_id=line_item_id
                          promoted_account_ids=promoted_account_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by
                          draft_only=draft_only)


def promoted_tweets_by_account_id(account_id, *, line_item_ids=IGNORE, line_item_id=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE, sort_by=IGNORE, draft_only=IGNORE):
    """
    Retrieve references to the Promoted Tweets associated with one or more line
    items.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_ids: Scope the response to just the desired line items by 
        specifying a comma-separated list of identifiers. Up to 200 ids may be
        provided. (False)
    
    
    :param line_item_id: Specify an identifier for a single line item by specif
        ying its line item identifier. (False)
    
    
    :param with_deleted: Include deleted results for your request. Defaults to 
        false. (False)
    
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param sort_by: Sorts by supported attribute in ascending or descending ord
        er. See sorting for more information. (False)
    
    
    :param draft_only: Scope the response to Promoted Tweets under draft campai
        gns. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/promoted_tweets"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-PROMOTED-TWEETS',
                          account_id=account_id
                          line_item_ids=line_item_ids
                          line_item_id=line_item_id
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor
                          sort_by=sort_by
                          draft_only=draft_only)


def recommendations_by_account_id(account_id):
    """
    Status:
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/recommendations"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-RECOMMENDATIONS',
                          account_id=account_id)


def recommendations_by_recommendation_id_and_account_id(recommendation_id, account_id):
    """
    Status:
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param recommendation_id: A specific recommendation_id to retrieve details 
        for. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/recommendations/{recommendation_id}"
    url = url.format(account_id=account_id,
                     recommendation_id=recommendation_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-RECOMMENDATIONS-RECOMMENDATION-ID',
                          account_id=account_id
                          recommendation_id=recommendation_id)


def scoped_timeline_by_account_id(account_id, *, user_id=IGNORE, user_ids=IGNORE, scoped_to=IGNORE, objective=IGNORE, trim_user=IGNORE, count=IGNORE, cursor=IGNORE, tweet_mode=IGNORE):
    """
    Retrieve up to 200 of the most recent promotable Tweets created by the
    specified Twitter user. This user may be any account for which the current
    account has account access. This endpoint works for any user with access to
    an Ads Account, not only the Twitter @handle which authors the promotable
    Tweets.
    
    :param user_id: Specifies the user to scope Tweets to. Defaults to the FULL
        promotable user on the account when not set. (False)
    
    
    :param user_ids: Limits tweets to the specified users. Comma-separated list
        of user ids. The requesting user must have full promotable access to
        the specified list of accounts. (False)
    
    
    :param scoped_to: followers to find Tweets in the account's timeline or non
        e to find Promoted-Only Tweets (False)
    
    
    :param objective: Filter the results to only those Tweets appropriate for t
        he given objective. See note above (top of page) about how filtering by
        objective affects result paging. (False)
    
    
    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param count: Specifies the number of tweets to try and retrieve, up to a m
        aximum of 200 per distinct request. The value of count is best thought
        of as a limit to the number of tweets to return because suspended or
        deleted content is removed after the count has been applied. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of tweets. See Pagin
        ation for more information. (False)
    
    
    :param tweet_mode: Value for the type of tweet being created. See Enums for
        more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/scoped_timeline"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-SCOPED-TIMELINE',
                          user_id=user_id
                          user_ids=user_ids
                          scoped_to=scoped_to
                          objective=objective
                          trim_user=trim_user
                          count=count
                          cursor=cursor
                          tweet_mode=tweet_mode
                          account_id=account_id)


def tailored_audience_changes_by_account_id(account_id, *, count=IGNORE, cursor=IGNORE):
    """
    Retrieve all audience changes submitted.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See Pagi
        nation for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audience_changes"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCE-CHANGES',
                          account_id=account_id
                          count=count
                          cursor=cursor)


def tailored_audience_changes_by_id_and_account_id(id, account_id):
    """
    Retrieve a specific tailored audience change record.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier for this tailored audience change record. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audience_changes/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCE-CHANGES-ID',
                          account_id=account_id
                          id=id)


def tailored_audiences_by_account_id(account_id, *, count=IGNORE, cursor=IGNORE, with_deleted=IGNORE):
    """
    Retrieve tailored audiences associated with a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES',
                          account_id=account_id
                          count=count
                          cursor=cursor
                          with_deleted=with_deleted)


def tailored_audiences_by_id_and_account_id(id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve specific tailored audience associated with a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier for a tailored audience associated with the curre
        nt account. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES-ID',
                          account_id=account_id
                          id=id
                          with_deleted=with_deleted)


def targeting_criteria_by_account_id(account_id, line_item_id, *, lang=IGNORE, with_deleted=IGNORE, draft_only=IGNORE):
    """
    Retrieve the targeting criteria associated with line items owned by the
    current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_id: Scope targeting criteria to a specific line item by pr
        oviding its identifier. (True)
    
    
    :param lang: An ISO-639-1 language code. When passed, an additional localiz
        ed_name attribute will be returned in the response for objects where a
        localized name is available. (False)
    
    
    :param with_deleted: Include deleted results for your request. (False)
    
    :param draft_only: Scope the response to targeting criteria associated with
        line items under draft campaigns. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TARGETING-CRITERIA',
                          account_id=account_id
                          line_item_id=line_item_id
                          lang=lang
                          with_deleted=with_deleted
                          draft_only=draft_only)


def targeting_criteria_by_id_and_account_id(id, account_id, targeting_criterion_id, *, lang=IGNORE, with_deleted=IGNORE):
    """
    Retrieve detailed information on a targeting criterion associated with a
    specific line item.
    
    :param lang:  (False)
    
    :param targeting_criterion_id:  (True)
    
    :param with_deleted:  (False)
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TARGETING-CRITERIA-ID',
                          lang=lang
                          targeting_criterion_id=targeting_criterion_id
                          with_deleted=with_deleted
                          account_id=account_id
                          id=id)


def targeting_suggestions_by_account_id(account_id, suggestion_type, targeting_values, *, count=IGNORE):
    """
    Get up to 50 targeting suggestion for HANDLES or KEYWORDS to complement
    your initial selection.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param suggestion_type: You can either receive KEYWORD or USER_ID suggestio
        ns. (True)
    
    
    :param targeting_values: A comma separated collection of either KEYWORD or 
        USER_ID to seed the the suggestions. These two types of suggestions can
        not be mixed, you can either send KEYWORD s and get KEYWORD s back or
        send USER_ID s to get some USER_ID s in return. (True)
    
    
    :param count: The total number of suggestions returned by this endpoint. De
        fault is 30. Minimum is 1 and Maximum is 50. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/targeting_suggestions"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TARGETING-SUGGESTIONS',
                          account_id=account_id
                          suggestion_type=suggestion_type
                          targeting_values=targeting_values
                          count=count)


def tweet_preview__by_account_id(account_id, status, *, as_user_id=IGNORE, media_ids=IGNORE, card_id=IGNORE, preview_target=IGNORE):
    """
    Preview a Tweet that does not already exist as it would appear across a
    variety of different platforms; iPhone, Android and Web. You can preview a
    Tweet both for how it will look like on Twitter or on the
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param status: The text of your status update, typically up to 140 characte
        rs. URL encode as necessary. t.co link wrapping may affect character
        counts. (True)
    
    
    :param as_user_id: The user ID of the advertiser on behalf of whom you are 
        posting the Tweet The advertiser must grant your handle (or handles)
        access to their ads account via the Twitter UI at ads.twitter.com. This
        permission allows you to call the API using the OAuth tokens of your
        own handle rather than the advertiser's. (False)
    
    
    :param media_ids: A list of up to four media ids to associate with the Twee
        t. See Uploading Media for further details on uploading media. Please
        note that we currently only support image media_ids. (False)
    
    
    :param card_id: The ID of the revenue card embedded in the Tweet. (False)
    
    :param preview_target: The target to render the Tweet preview for. You can 
        preview a Tweet both for how it will look like on Twitter (
        TWITTER_TIMELINE ) or on the Twitter Audience Platform (
        PUBLISHER_NETWORK ). When using the PUBLISHER_NETWORK value for the
        preview_target parameter you should not use a card_id and you must
        specify media_ids. Defaults to TWITTER_TIMELINE. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tweet/preview/"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TWEET-PREVIEW',
                          account_id=account_id
                          status=status
                          as_user_id=as_user_id
                          media_ids=media_ids
                          card_id=card_id
                          preview_target=preview_target)


def tweet_preview_by_tweet_id_and_account_id(tweet_id, account_id, *, as_user_id=IGNORE, preview_target=IGNORE):
    """
    Preview an existing Tweet as it would appear across a variety of different
    platforms; iPhone, Android and Web. You can preview a Tweet both for how it
    will look like on Twitter or on the
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param tweet_id: The unique identifier referring to a Tweet (True)
    
    :param as_user_id: The user ID of the advertiser on behalf of whom you are 
        posting the Tweet The advertiser must grant your handle (or handles)
        access to their ads account via the Twitter UI at ads.twitter.com. This
        permission allows you to call the API using the OAuth tokens of your
        own handle rather than the advertiser's. (False)
    
    
    :param preview_target: The target to render the Tweet preview for. You can 
        preview a Tweet both for how it will look like on Twitter (
        TWITTER_TIMELINES ) or on the Twitter Audience Platform (
        PUBLISHER_NETWORKS ). When using the PUBLISHER_NETWORKS value for the
        preview_target parameter you must not use a Tweet with a card_id and
        the Tweet must specify media_ids. Defaults to TWITTER_TIMELINES.
        (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tweet/preview/{tweet_id}"
    url = url.format(tweet_id=tweet_id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TWEET-PREVIEW-TWEET-ID',
                          account_id=account_id
                          tweet_id=tweet_id
                          as_user_id=as_user_id
                          preview_target=preview_target)


def videos_by_account_id(account_id, *, video_ids=IGNORE, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Retrieve all video objects associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param video_ids: An optional comma separated list of video IDs to filter t
        he response to. (False)
    
    
    :param with_deleted: Include deleted results for your request. (False)
    
    :param count: Specifies the number of videos to try and retrieve, up to a m
        aximum of 1,000. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of video objects. Se
        e Pagination for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/videos"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-VIDEOS',
                          account_id=account_id
                          video_ids=video_ids
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor)


def videos_by_id_and_account_id(id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve a specific video object belonging to the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The UUID identifier of the video object to be retrieved. (True)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/videos/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-VIDEOS-ID',
                          account_id=account_id
                          id=id
                          with_deleted=with_deleted)


def web_event_tags_by_account_id(account_id, *, with_deleted=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Retrieve all web event tags associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param with_deleted: Include deleted results for your request. Defaults to 
        false. (False)
    
    
    :param count: Specifies the number of results to try to return per response
        , up to a maximum of 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-WEB-EVENT-TAGS',
                          account_id=account_id
                          with_deleted=with_deleted
                          count=count
                          cursor=cursor)


def web_event_tags_by_id_and_account_id(id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve a specific web event tag associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier for the web event tag. (True)
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-WEB-EVENT-TAGS-ID',
                          account_id=account_id
                          id=id
                          with_deleted=with_deleted)


def reach_estimate_by_account_id(account_id, product_type, objective, bid_amount_local_micro, currency, campaign_daily_budget_amount_local_micro, *, bid_type=IGNORE, followers_of_users=IGNORE, similar_to_followers_of_users=IGNORE, locations=IGNORE, interests=IGNORE, gender=IGNORE, platforms=IGNORE, tailored_audiences=IGNORE, tailored_audiences_expanded=IGNORE, languages=IGNORE, platform_versions=IGNORE, devices=IGNORE, behaviors=IGNORE, behaviors_expanded=IGNORE, campaign_engagement=IGNORE, user_engagement=IGNORE, engagement_type=IGNORE, network_operators=IGNORE, app_store_categories=IGNORE, app_store_categories_expanded=IGNORE, exact_keywords=IGNORE, broad_keywords=IGNORE, phrase_keywords=IGNORE, age_buckets=IGNORE, wifi_only=IGNORE):
    """
    Determine the approximate reach of your campaigns.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param product_type: Reach estimates are available for two product types: P
        ROMOTED_ACCOUNT or PROMOTED_TWEETS. (True)
    
    
    :param objective: The campaign objective for this line item. For details on
        objectives and all possible values, see Objective-based Campaigns.
        (True)
    
    
    :param bid_amount_local_micro: Bid in specified currency micros. (True)
    
    :param currency: The type of currency for bid_amount_local_micro. Identifie
        d using ISO-4217. This is a three-letter string such as “USD” or “EUR”.
        (True)
    
    
    :param campaign_daily_budget_amount_local_micro: The daily budget for the c
        ampaign in micros. (True)
    
    
    :param bid_type: Sets the bidding mechanism. If set to AUTO, bid_amount_loc
        al_micro must be NULL. MAX sets the maximum allowable bid. AUTO
        automatically optimizes bidding based on daily budget and campaign
        flight dates. TARGET (available when objective is set to
        WEBSITE_CLICKS, WEBSITE_CONVERSIONS or LEAD_GENERATION) attempts to
        make daily bid averages hit within 20% of the specified
        bid_amount_local_micro (False)
    
    
    :param followers_of_users: Include the followers of the specified comma-sep
        arated list of user_id s in reach estimate. The user must be one of the
        promotable users on the advertiser account. Limit of 100 handles.
        (False)
    
    
    :param similar_to_followers_of_users: Include users that are similar to a c
        omma-separated list of user_id. Limit of 100 handles. (False)
    
    
    :param locations: A comma-separated string of location identifiers to scope
        targeting to on this line item. Up to 250 locations may be associated
        with a line item. (False)
    
    
    :param interests: A comma-separated string of interest identifiers to scope
        targeting to on this line item. Limited to 100 interests. (False)
    
    
    :param gender: A comma-separated string of gender identifiers to scope targ
        eting to on this line item. Use `` 1 `` to limit to males, or `` 2 ``
        to limit to females. Omit for all. (False)
    
    
    :param platforms: A comma-separated string of Platform identifiers to scope
        targeting to on this line item. (False)
    
    
    :param tailored_audiences: A comma-separated string of tailored audience id
        entifiers. (False)
    
    
    :param tailored_audiences_expanded: A comma-separated string of tailored au
        dience identifiers that should be expanded for look-a-likes. (False)
    
    
    :param languages: A comma-separated string of language identifiers. (False)
    
    :param platform_versions: A comma-separated string of platform version iden
        tifiers. (False)
    
    
    :param devices: A comma-separated string of device identifiers. (False)
    
    :param behaviors: A comma-separated string of behavior identifiers. (False)
    
    :param behaviors_expanded: A comma-separated string of behavior identifiers
        . that should be expanded for look-a-likes. (False)
    
    
    :param campaign_engagement: The campaign idenifier for use with Tweet Engag
        er Retargeting. (False)
    
    
    :param user_engagement: The promotable user_id for use with Tweet Engager R
        etargeting. (False)
    
    
    :param engagement_type: The engagement type for use with Tweet Engager Reta
        rgeting. Valid values include IMPRESSION or ENGAGEMENT. (False)
    
    
    :param network_operators: A comma-separated string of network operators to 
        target. (False)
    
    
    :param app_store_categories: A comma-separated string of app store categori
        es to target. (False)
    
    
    :param app_store_categories_expanded: A comma-separated string of app store
        categories to target with look-a-like expansion. (False)
    
    
    :param exact_keywords: A comma-separated string of “exact match” keywords t
        o target. (False)
    
    
    :param broad_keywords: A comma-separated string of “broad” keywords to targ
        et. (False)
    
    
    :param phrase_keywords: A comma-separated string of “phrase” keywords to ta
        rget. (False)
    
    
    :param age_buckets: A comma-separated string of age_buckets to target. (Fal
        se)
    
    
    :param wifi_only: If true, will only target users of mobile devices using w
        ifi connections. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/reach_estimate"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-1-ACCOUNTS-ACCOUNT-ID-REACH-ESTIMATE',
                          account_id=account_id
                          product_type=product_type
                          objective=objective
                          bid_amount_local_micro=bid_amount_local_micro
                          currency=currency
                          campaign_daily_budget_amount_local_micro=campaign_daily_budget_amount_local_micro
                          bid_type=bid_type
                          followers_of_users=followers_of_users
                          similar_to_followers_of_users=similar_to_followers_of_users
                          locations=locations
                          interests=interests
                          gender=gender
                          platforms=platforms
                          tailored_audiences=tailored_audiences
                          tailored_audiences_expanded=tailored_audiences_expanded
                          languages=languages
                          platform_versions=platform_versions
                          devices=devices
                          behaviors=behaviors
                          behaviors_expanded=behaviors_expanded
                          campaign_engagement=campaign_engagement
                          user_engagement=user_engagement
                          engagement_type=engagement_type
                          network_operators=network_operators
                          app_store_categories=app_store_categories
                          app_store_categories_expanded=app_store_categories_expanded
                          exact_keywords=exact_keywords
                          broad_keywords=broad_keywords
                          phrase_keywords=phrase_keywords
                          age_buckets=age_buckets
                          wifi_only=wifi_only)


def tailored_audiences_by_account_id(account_id, with_deleted, *, permission_scope=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Retrieve tailored audiences associated with a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t (True)
    
    
    :param permission_scope: Allows filtering the response to lists you own or 
        lists that have been shared with you. By default, without specifying
        this parameter you will only see audiences you own. Type: enum Default:
        OWNER Possible values: OWNER, SHARED (False)
    
    
    :param count: Specifies the number of records to try and retrieve per disti
        nct request. Type: int Default: 200 Min, Max: 1, 1000 (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. Type: string Example: gc-ddf4a (False)
    
    
    :param with_deleted: Include deleted results in your request. Type: enum De
        fault: false Possible values: true, false (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences"
    url = url.format(account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-1-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES',
                          account_id=account_id
                          permission_scope=permission_scope
                          count=count
                          cursor=cursor
                          with_deleted=with_deleted)


def tailored_audiences_by_id_and_account_id(id, account_id, *, with_deleted=IGNORE):
    """
    Retrieve specific tailored audience associated with a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES-ID',
                          account_id=account_id
                          id=id
                          with_deleted=with_deleted)


def tailored_audiences_permissions_by_id_and_account_id(id, account_id, *, granted_account_ids=IGNORE, count=IGNORE, cursor=IGNORE, with_deleted=IGNORE):
    """
    Displays all current permissions objects associated with a given tailored
    audience.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param granted_account_ids: An optional, comma separated list of account ID
        s to filter the API response to. (False)
    
    
    :param count: Specifies the number of records to try and retrieve, up to a 
        maximum of 1000 per distinct request. (False)
    
    
    :param cursor: Specifies a cursor to get the next page of results. See pagi
        nation for more information. (False)
    
    
    :param with_deleted: Include deleted results in your request. Defaults to f
        alse. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}/permissions"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('GET',
                          url,
                          'ADS:ACCOUNTS',
                          'GET-1-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES-ID-PERMISSIONS',
                          account_id=account_id
                          granted_account_ids=granted_account_ids
                          count=count
                          cursor=cursor
                          with_deleted=with_deleted
                          id=id)


def account_media_by_account_id(account_id, media_id, video_id, creative_type):
    """
    Creates a new account media associated to the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param media_id: The identifier of the media uploaded. (True)
    
    :param video_id: The identifier of the video to be used. (True)
    
    :param creative_type: The type of creative for this media. See Ads Enumerat
        ions for more information. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/account_media"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-ACCOUNT-MEDIA',
                          account_id=account_id
                          media_id=media_id
                          video_id=video_id
                          creative_type=creative_type)


def app_event_provider_configurations_by_account_id(account_id, provider_advertiser_id):
    """
    Create a new application event provider configuration associated with the
    current account. Only one MACT provider can be associated with a particular
    ads account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param provider_advertiser_id: The advertiser's identifier (string) from th
        e provider's site. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_event_provider_configurations"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-APP-EVENT-PROVIDER-CONFIGURATIONS',
                          account_id=account_id
                          provider_advertiser_id=provider_advertiser_id)


def app_event_tags_by_account_id(account_id, app_store_identifier, os_type, conversion_type, provider_app_event_id, provider_app_event_name, *, post_engagement_attribution_window=IGNORE, post_view_attribution_window=IGNORE, deep_link_scheme=IGNORE, retargeting_enabled=IGNORE):
    """
    Create a new application event tag associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param app_store_identifier: The app store string identifier such as 12345 
        or com.foobar.andriod.prod (True)
    
    
    :param os_type: The OS type. Possible values include IOS and ANDRIOD. (True
        )
    
    
    :param conversion_type: The type of conversion event. Possible values are P
        URCHASE, SIGN_UP, INSTALL, RE_ENGAGE, UPDATE, TUTORIAL_COMPLETE,
        RESERVATION, ADD_TO_CART, ADD_TO_WISHLIST, LOGIN, CHECKOUT_INITIATED,
        SEARCH, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, CONTENT_VIEW, SHARE,
        INVITE, ADDED_PAYMENT_INFO, SPENT_CREDITS, RATED. (True)
    
    
    :param provider_app_event_id: The ID of the conversion tag on the provider'
        s site. (True)
    
    
    :param provider_app_event_name: The name of the conversion tag on the provi
        der's site. (True)
    
    
    :param post_engagement_attribution_window: The post-engagement attribution 
        window for these events. Possible values are 1, 7, 14 or 30. (False)
    
    
    :param post_view_attribution_window: The post-view attribution window for t
        hese events. Possible values are 0, 1, 7, 14 or 30. (False)
    
    
    :param deep_link_scheme: String. Specify the deep link URI for the app asso
        ciated to this tag. (False)
    
    
    :param retargeting_enabled: Boolean indicating if retargeting should be ena
        bled for this app event tag. Possible values are true, 1, false, 0.
        (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-APP-EVENT-TAGS',
                          account_id=account_id
                          app_store_identifier=app_store_identifier
                          os_type=os_type
                          conversion_type=conversion_type
                          provider_app_event_id=provider_app_event_id
                          provider_app_event_name=provider_app_event_name
                          post_engagement_attribution_window=post_engagement_attribution_window
                          post_view_attribution_window=post_view_attribution_window
                          deep_link_scheme=deep_link_scheme
                          retargeting_enabled=retargeting_enabled)


def app_lists_by_account_id(account_id, name, app_store_identifiers):
    """
    Create an
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name you will assign to the app_list. (True)
    
    :param app_store_identifiers: The app_store_identifier``s to include in thi
        s ``app_list. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_lists"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-APP-LISTS',
                          account_id=account_id
                          name=name
                          app_store_identifiers=app_store_identifiers)


def campaigns_by_account_id(account_id, name, funding_instrument_id, start_time, daily_budget_amount_local_micro, *, end_time=IGNORE, paused=IGNORE, standard_delivery=IGNORE, frequency_cap=IGNORE, duration_in_days=IGNORE, total_budget_amount_local_micro=IGNORE):
    """
    Create a new campaign associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name you will assign to the campaign. (True)
    
    :param funding_instrument_id: The identifier for a funding instrument to be
        associated with this campaign. (True)
    
    
    :param start_time: The UTC time that the campaign will begin. Must be more 
        recent than the current time. Expressed in ISO 8601. (True)
    
    
    :param end_time: The UTC time that the campaign will end. If specified, mus
        t be more recent than the campaign's start_time. Expressed in ISO 8601.
        (False)
    
    
    :param paused: A boolean indicating whether this campaign is currently paus
        ed (AKA “inactive”). Defaults to false. (False)
    
    
    :param standard_delivery: A boolean indicating whether this campaign should
        use standard delivery rather than accelerated delivery.
        standard_delivery defaults to true. See Budget Pacing for more
        information on standard versus accelerated delivery. (False)
    
    
    :param frequency_cap: An integer representing the number of times for which
        one user could be delivered an ad to. (False)
    
    
    :param duration_in_days: An integer representing the time period within whi
        ch the frequency_cap frequency is achieved. Only supports values of: 1,
        7 and 30. (False)
    
    
    :param total_budget_amount_local_micro: An integer representing the total b
        udget amount to be allocated to the campaign. The currency associated
        with the specified funding instrument will be used. For USD, $37.50 is
        encoded as 37.50*1e6, or 37,500,000. (False)
    
    
    :param daily_budget_amount_local_micro: An integer representing the daily b
        udget amount to be allocated to the campaign. This amount should be
        less than or equal to the total_budget_amount_local_micro. The currency
        associated with the specified funding instrument will be used. For USD,
        $5.50 is encoded as 5.50*1e6, or 5,500,000. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/campaigns"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-CAMPAIGNS',
                          account_id=account_id
                          name=name
                          funding_instrument_id=funding_instrument_id
                          start_time=start_time
                          end_time=end_time
                          paused=paused
                          standard_delivery=standard_delivery
                          frequency_cap=frequency_cap
                          duration_in_days=duration_in_days
                          total_budget_amount_local_micro=total_budget_amount_local_micro
                          daily_budget_amount_local_micro=daily_budget_amount_local_micro)


def cards_app_download_by_account_id(account_id, name, app_country_code, *, iphone_app_id=IGNORE, ipad_app_id=IGNORE, googleplay_app_id=IGNORE, app_cta=IGNORE, iphone_deep_link=IGNORE, ipad_deep_link=IGNORE, googleplay_deep_link=IGNORE, custom_icon_media_id=IGNORE, custom_app_description=IGNORE):
    """
    Creates a new app download card associated to a given account. This card is
    part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name identifier for card. Maximum length: 80 characters. (
        True)
    
    
    :param app_country_code: 2 letter ISO code for the country where the App is
        sold. (True)
    
    
    :param iphone_app_id: This is usually numeric and available in your App Sto
        re URL. For example, 333903271 is the id for Twitter. You can retrieve
        the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPHONE_APP_ID> (False)
    
    
    :param ipad_app_id: This is usually numeric and available in your App Store
        URL. For example, 333903271 is the id for Twitter. You can retrieve
        the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPAD_APP_ID> (False)
    
    
    :param googleplay_app_id: This ID is Google Play's application package name
        . For example, Twitter's Google Play app id is com.twitter.android.
        (False)
    
    
    :param app_cta: The Call-to-Action (CTA) text for the card button. See our 
        enums for possible values. (False)
    
    
    :param iphone_deep_link: This is your app's deep link. (False)
    
    :param ipad_deep_link: This is your app's deep link. (False)
    
    :param googleplay_deep_link: This is your app's deep link. (False)
    
    :param custom_icon_media_id: A media_id of a custom image which will be use
        d instead of the app store's icon. This is a write-only field. In
        response, the API will provide a Twitter URL for this image, that can
        be reused. This needs to be minimum of 144px wide/height with the
        aspect ratio 1:1. (False)
    
    
    :param custom_app_description: This is a custom description of the app. If 
        supplied, it will be used instead of the description from the app
        store. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-CARDS-APP-DOWNLOAD',
                          account_id=account_id
                          name=name
                          app_country_code=app_country_code
                          iphone_app_id=iphone_app_id
                          ipad_app_id=ipad_app_id
                          googleplay_app_id=googleplay_app_id
                          app_cta=app_cta
                          iphone_deep_link=iphone_deep_link
                          ipad_deep_link=ipad_deep_link
                          googleplay_deep_link=googleplay_deep_link
                          custom_icon_media_id=custom_icon_media_id
                          custom_app_description=custom_app_description)


def cards_image_app_download_by_account_id(account_id, name, app_country_code, wide_app_image_media_id, *, iphone_app_id=IGNORE, ipad_app_id=IGNORE, googleplay_app_id=IGNORE, app_cta=IGNORE, iphone_deep_link=IGNORE, ipad_deep_link=IGNORE, googleplay_deep_link=IGNORE):
    """
    Creates a new image app download card associated to a given account. This
    card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name identifier for card. Maximum length: 80 characters. (
        True)
    
    
    :param app_country_code: 2 letter ISO code for the country where the App is
        sold. (True)
    
    
    :param iphone_app_id: This is usually numeric and available in your App Sto
        re URL. For example, 333903271 is the id for Twitter. You can retrieve
        the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPHONE_APP_ID> (False)
    
    
    :param ipad_app_id: This is usually numeric and available in your App Store
        URL. For example, 333903271 is the id for Twitter. You can retrieve
        the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPAD_APP_ID> (False)
    
    
    :param googleplay_app_id: This ID is Google Play's application package name
        . For example, Twitter's Google Play app id is com.twitter.android.
        (False)
    
    
    :param app_cta: The Call-to-Action (CTA) text for the card button. See our 
        enums for possible values. (False)
    
    
    :param iphone_deep_link: This is your app's deep link. (False)
    
    :param ipad_deep_link: This is your app's deep link. (False)
    
    :param googleplay_deep_link: This is your app's deep link. (False)
    
    :param wide_app_image_media_id: A media_id of an image which will be used i
        nstead of the app store's icon. This is a write-only field. In
        response, the API will provide a Twitter URL for this image, that can
        be reused. Minimum width of 800px, maximum size of 1MB and width:height
        with the aspect ratio 5:2. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-APP-DOWNLOAD',
                          account_id=account_id
                          name=name
                          app_country_code=app_country_code
                          iphone_app_id=iphone_app_id
                          ipad_app_id=ipad_app_id
                          googleplay_app_id=googleplay_app_id
                          app_cta=app_cta
                          iphone_deep_link=iphone_deep_link
                          ipad_deep_link=ipad_deep_link
                          googleplay_deep_link=googleplay_deep_link
                          wide_app_image_media_id=wide_app_image_media_id)


def cards_image_conversation_by_account_id(account_id, name, title, first_cta, first_cta_tweet, thank_you_text, image_media_id, *, second_cta=IGNORE, second_cta_tweet=IGNORE, third_cta=IGNORE, third_cta_tweet=IGNORE, fourth_cta=IGNORE, fourth_cta_tweet=IGNORE, thank_you_url=IGNORE, cover_image_id=IGNORE):
    """
    Creates a new image conversation card associated to a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name identifier for card (not user-facing). Maximum length
        : 80 characters. (True)
    
    
    :param title: The title text for the card, used when only first CTA is spec
        ified. Maximum length: 23 characters. (True)
    
    
    :param first_cta: The call-to-action hashtag for the first option. Maximum 
        length: 20 characters (not counting the # character). (True)
    
    
    :param first_cta_tweet: The Tweet text to be used when the first call-to-ac
        tion is clicked. Maximum length: 116 characters. (True)
    
    
    :param second_cta: The call-to-action text for the second option. Maximum l
        ength: 20 characters. (not counting the # character). (False)
    
    
    :param second_cta_tweet: The Tweet text to be used when the second call-to-
        action is clicked. Maximum length: 116 characters. (False)
    
    
    :param third_cta: The call-to-action text for the third option. Maximum len
        gth: 20 characters. (not counting the # character). (False)
    
    
    :param third_cta_tweet: The Tweet text to be used when the third call-to-ac
        tion is clicked. Maximum length: 116 characters. (False)
    
    
    :param fourth_cta: The call-to-action text for the fourth option. Maximum l
        ength: 20 characters. (not counting the # character). (False)
    
    
    :param fourth_cta_tweet: The Tweet text to be used when the fourth call-to-
        action is clicked. Maximum length: 116 characters. (False)
    
    
    :param thank_you_text: The text to be displayed after the call-to-action is
        clicked. (True)
    
    
    :param thank_you_url: The URL to be displayed with the thank you text. (Fal
        se)
    
    
    :param image_media_id: A media_id of an image which will be used in this ca
        rd. This is a write-only field. In response, the API will provide a
        Twitter URL for this image, that can be reused. Minimum width of 800px,
        maximum size of 1MB and width:height with the aspect ratio 5:2. (True)
    
    
    :param cover_image_id: A media_id of an image which will be used in the ins
        tant unlock scenario. This is a write-only field. In response, the API
        will provide a Twitter URL for this image, that can be reused. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-CONVERSATION',
                          account_id=account_id
                          name=name
                          title=title
                          first_cta=first_cta
                          first_cta_tweet=first_cta_tweet
                          second_cta=second_cta
                          second_cta_tweet=second_cta_tweet
                          third_cta=third_cta
                          third_cta_tweet=third_cta_tweet
                          fourth_cta=fourth_cta
                          fourth_cta_tweet=fourth_cta_tweet
                          thank_you_text=thank_you_text
                          thank_you_url=thank_you_url
                          image_media_id=image_media_id
                          cover_image_id=cover_image_id)


def cards_video_app_download_by_account_id(account_id, name, app_country_code, video_id, *, iphone_app_id=IGNORE, ipad_app_id=IGNORE, googleplay_app_id=IGNORE, app_cta=IGNORE, iphone_deep_link=IGNORE, ipad_deep_link=IGNORE, googleplay_deep_link=IGNORE, image_media_id=IGNORE):
    """
    Creates a new Video App Download Card associated to the specified account.
    This card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name identifier for card. Maximum length: 80 characters. (
        True)
    
    
    :param app_country_code: 2 letter ISO code for the country where the App is
        sold. (True)
    
    
    :param iphone_app_id: This is usually numeric and available in your App Sto
        re URL. For example, 333903271 is the id for Twitter. You can retrieve
        the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPHONE_APP_ID> (False)
    
    
    :param ipad_app_id: This is usually numeric and available in your App Store
        URL. For example, 333903271 is the id for Twitter. You can retrieve
        the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPAD_APP_ID> (False)
    
    
    :param googleplay_app_id: This ID is Google Play's application package name
        . For example, Twitter's Google Play app id is com.twitter.android.
        (False)
    
    
    :param app_cta: The Call-to-Action (CTA) text for the card button. See our 
        enums for possible values. (False)
    
    
    :param iphone_deep_link: This is your app's deep link. (False)
    
    :param ipad_deep_link: This is your app's deep link. (False)
    
    :param googleplay_deep_link: This is your app's deep link. (False)
    
    :param image_media_id: The media_id for the uploaded video poster image. Th
        ere are no size or aspect ratio restrictions on this image, it will
        simply be converted to fit the dimensions of the player. (False)
    
    
    :param video_id: The UUID of the uploaded video from GET accounts/:account_
        id/videos endpoint to be included in the card. (True)
    """
    url = "POST"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-APP-DOWNLOAD',
                          account_id=account_id
                          name=name
                          app_country_code=app_country_code
                          iphone_app_id=iphone_app_id
                          ipad_app_id=ipad_app_id
                          googleplay_app_id=googleplay_app_id
                          app_cta=app_cta
                          iphone_deep_link=iphone_deep_link
                          ipad_deep_link=ipad_deep_link
                          googleplay_deep_link=googleplay_deep_link
                          image_media_id=image_media_id
                          video_id=video_id)


def cards_video_conversation_by_account_id(account_id, name, title, first_cta, first_cta_tweet, thank_you_text, image_media_id, video_id, *, second_cta=IGNORE, second_cta_tweet=IGNORE, third_cta=IGNORE, third_cta_tweet=IGNORE, fourth_cta=IGNORE, fourth_cta_tweet=IGNORE, thank_you_url=IGNORE, cover_video_id=IGNORE):
    """
    Creates a new video conversation card associated to a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name identifier for card (not user-facing). Maximum length
        : 80 characters. (True)
    
    
    :param title: The title text for the card, used when only first CTA is spec
        ified. Maximum length: 23 characters. (True)
    
    
    :param first_cta: The call-to-action hashtag for the first option. Maximum 
        length: 20 characters (not counting the # character). (True)
    
    
    :param first_cta_tweet: The Tweet text to be used when the first call-to-ac
        tion is clicked. Maximum length: 116 characters. (True)
    
    
    :param second_cta: The call-to-action text for the second option. Maximum l
        ength: 20 characters. (not counting the # character). (False)
    
    
    :param second_cta_tweet: The Tweet text to be used when the second call-to-
        action is clicked. Maximum length: 116 characters. (False)
    
    
    :param third_cta: The call-to-action text for the third option. Maximum len
        gth: 20 characters. (not counting the # character). (False)
    
    
    :param third_cta_tweet: The Tweet text to be used when the third call-to-ac
        tion is clicked. Maximum length: 116 characters. (False)
    
    
    :param fourth_cta: The call-to-action text for the fourth option. Maximum l
        ength: 20 characters. (not counting the # character). (False)
    
    
    :param fourth_cta_tweet: The Tweet text to be used when the fourth call-to-
        action is clicked. Maximum length: 116 characters. (False)
    
    
    :param thank_you_text: The text to be displayed after the call-to-action is
        clicked. (True)
    
    
    :param thank_you_url: The URL to be displayed with the thank you text. (Fal
        se)
    
    
    :param image_media_id: A media_id of an image which will be used as the pos
        ter image in this card. This is a write-only field. In response, the
        API will provide a Twitter URL for this image, that can be reused.
        Minimum width of 800px, maximum size of 1MB and width:height with the
        aspect ratio 5:2. (True)
    
    
    :param video_id: A media_id of a video which will be used in this card. Thi
        s is a write-only field. (True)
    
    
    :param cover_video_id: A media_id of a video which will be used in the inst
        ant unlock scenario. This is a write-only field. In response, the API
        will provide a Twitter URL for this image, that can be reused. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-CONVERSATION',
                          account_id=account_id
                          name=name
                          title=title
                          first_cta=first_cta
                          first_cta_tweet=first_cta_tweet
                          second_cta=second_cta
                          second_cta_tweet=second_cta_tweet
                          third_cta=third_cta
                          third_cta_tweet=third_cta_tweet
                          fourth_cta=fourth_cta
                          fourth_cta_tweet=fourth_cta_tweet
                          thank_you_text=thank_you_text
                          thank_you_url=thank_you_url
                          image_media_id=image_media_id
                          video_id=video_id
                          cover_video_id=cover_video_id)


def cards_website_by_account_id(account_id, name, website_title, website_url, image_media_id):
    """
    Creates a new website card associated to a given account. Our advertiser
    help center has
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name identifier for card. Maximum length: 80 characters. (
        True)
    
    
    :param website_title: The title of the website card. Maximum length: 70 cha
        racters. (True)
    
    
    :param website_url: The URL of the website to redirect a user to. Maximum l
        ength: 200 characters. (True)
    
    
    :param image_media_id: A media_id of an image which will be used in this ca
        rd. This is a write-only field. In response, the API will provide a
        Twitter URL for this image, that can be reused. The image must have: a
        minimum width of 800px, a maximum size of 1 MB, and a width:height
        aspect ratio of either 5:2 or 1.91:1. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/website"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-CARDS-WEBSITE',
                          account_id=account_id
                          name=name
                          website_title=website_title
                          website_url=website_url
                          image_media_id=image_media_id)


def line_item_apps_by_account_id(account_id, line_item_id, app_store_identifier, os_type):
    """
    Create an association between a mobile app and a line item to enable mobile
    app promotion on the Twitter Audience Platform.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_id: The line item to associate the app to. (True)
    
    :param app_store_identifier: The app store string identifier, such as `` 12
        345 `` or com.foobar.android.prod (True)
    
    
    :param os_type: The OS type. Possible values include IOS and ANDRIOD. (True
        )
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-LINE-ITEM-APPS',
                          account_id=account_id
                          line_item_id=line_item_id
                          app_store_identifier=app_store_identifier
                          os_type=os_type)


def line_items_by_account_id(account_id, campaign_id, product_type, placements, objective, *, bid_amount_local_micro=IGNORE, name=IGNORE, bid_type=IGNORE, automatically_select_bid=IGNORE, paused=IGNORE, include_sentiment=IGNORE, total_budget_amount_local_micro=IGNORE, start_time=IGNORE, end_time=IGNORE, primary_web_event_tag=IGNORE, optimization=IGNORE, bid_unit=IGNORE, charge_by=IGNORE, advertiser_domain=IGNORE, categories=IGNORE, tracking_tags=IGNORE, advertiser_user_id=IGNORE, target_cpa_local_micro=IGNORE):
    """
    Create a line item associated with the specified campaign belonging to the
    current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param campaign_id: The identifier for a campaign associated with the curre
        nt account. (True)
    
    
    :param bid_amount_local_micro: Required if bid_type is set to either MAX or
        TARGET or if automatically_set_bid is false. An integer representing
        the bid amount to be associated with this line item. The currency
        associated with the specified funding instrument will be used. For USD,
        $1.50 is encoded as 1.50*1e6, or 1,500,000. This value cannot be set to
        0 and only positive integers are accepted. (False)
    
    
    :param name: A name assigned to the line item. If left blank, the name will
        default to ‘Untitled.' (False)
    
    
    :param bid_type: Sets the bidding mechanism. If set to AUTO, bid_amount_loc
        al_micro is not required and should not be set. Cannot be set in the
        same request as automatically_set_bid. (False)
    
    
    :param automatically_select_bid: This boolean parameter when set to true wi
        ll automatically optimize bidding based on daily budget and campaign
        flight dates. If set to true, bid_amount_local_micro is not required
        and should not be set, and bid_type will be set to AUTO. Cannot be set
        in the same request as bid_type. (False)
    
    
    :param product_type: The type of promoted product that this line item will 
        contain. See our enums for possible values. (True)
    
    
    :param placements: The comma-separated list of placement locations for this
        line item to display in. See our enums for possible values. (True)
    
    
    :param objective: The campaign objective for this line item. For details on
        objectives and all possible values, see Objective-based Campaigns.
        (True)
    
    
    :param paused: A boolean indicating whether this line item is currently pau
        sed (AKA “inactive”). (False)
    
    
    :param include_sentiment: Allows the line item to be targeted to Tweets wit
        h both positive or negative sentiment. A tweet is said to have positive
        or negative sentiment if the tone of the Tweet is positive (“I love it!
        #newcamero”) or negative (“I hate it! #newcamero”). Note, only valid
        for product_type of PROMOTED_TWEETS and with either placements of
        ALL_ON_TWITTER or TWITTER_TIMELINES. Available options: POSITIVE_ONLY
        (default) targets only Tweets with positive sentiment, ALL targets all
        Tweets, including those with negative sentiment. (False)
    
    
    :param total_budget_amount_local_micro: An integer representing the total b
        udget amount to be allocated to the line item. The currency associated
        with the specified funding instrument and campaign will be used. For
        USD, $37.50 is encoded as 37.50*1e6, or 37,500,000. (False)
    
    
    :param start_time: The UTC time that the line item will begin serving. Must
        be more recent than the current time. Expressed in ISO 8601. (False)
    
    
    :param end_time: The UTC time that the line item will stop serving. If spec
        ified, must be more recent than the line item's start_time. Expressed
        in ISO 8601. (False)
    
    
    :param primary_web_event_tag: The identifier of the primary web event tag. 
        Allows more accurate tracking of engagements for the campaign
        pertaining to this line item. See GET
        accounts/:account_id/web_event_tags. Must be specified when objective
        is set to WEBSITE_CONVERSIONS. (False)
    
    
    :param optimization: The optimization setting to use on this ad group (line
        item). For possible values, see our enumerations page. (False)
    
    
    :param bid_unit: This setting is available for line items using the APP_INS
        TALLS or VIDEO_VIEWS objectives. See Objective-based Campaigns.
        Defaults to bid unit based on objective. For possible values, see Ads
        Enumerations. (False)
    
    
    :param charge_by: This setting is available for line items using the APP_IN
        STALLS objective. See Objective-based Campaigns. Defaults to charging
        by bid unit except for line items with bid unit APP_INSTALLS, where it
        defaults to charging by app-clicks. For all possible values, see Ads
        Enumerations. (False)
    
    
    :param advertiser_domain: The website domain for this advertiser, without p
        rotocol specification. This setting is available for line items using
        the Twitter Audience Platform (TAP). (False)
    
    
    :param categories: The relevant IAB categories for this advertiser. This se
        tting is available for line items using the Twitter Audience Platform
        (TAP). For possible values, see GET /1/iab_categories. (False)
    
    
    :param tracking_tags: The tracking partner enum and the tracking tag url pr
        ovided by the tracking partner, separated by a dash. For possible
        tracking partner enums, see Ads Enumerations. (False)
    
    
    :param advertiser_user_id: The Twitter user identifier for the handle promo
        ting a VIDEO_VIEWS_PREROLL ad. Use of this parameter is restricted to
        whitelisted developers only. (False)
    
    
    :param target_cpa_local_micro: An integer representing the target CPA amoun
        t to be allocated to the line item. The currency associated with the
        specified funding instrument and campaign will be used. For USD, $5.50
        is encoded as 5.50*1e6, or 5,500,000. Must be specified when objective
        is set to WEBSITE_CONVERSIONS. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_items"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-LINE-ITEMS',
                          account_id=account_id
                          campaign_id=campaign_id
                          bid_amount_local_micro=bid_amount_local_micro
                          name=name
                          bid_type=bid_type
                          automatically_select_bid=automatically_select_bid
                          product_type=product_type
                          placements=placements
                          objective=objective
                          paused=paused
                          include_sentiment=include_sentiment
                          total_budget_amount_local_micro=total_budget_amount_local_micro
                          start_time=start_time
                          end_time=end_time
                          primary_web_event_tag=primary_web_event_tag
                          optimization=optimization
                          bid_unit=bid_unit
                          charge_by=charge_by
                          advertiser_domain=advertiser_domain
                          categories=categories
                          tracking_tags=tracking_tags
                          advertiser_user_id=advertiser_user_id
                          target_cpa_local_micro=target_cpa_local_micro)


def media_creatives_by_account_id(account_id, line_item_id, account_media_id, *, landing_url=IGNORE):
    """
    Creates a new media creative associated to the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_id: A reference to the line item you are operating with in
        the request. (True)
    
    
    :param account_media_id: The identifier of the account media for this accou
        nt. (True)
    
    
    :param landing_url: URL for the media creative. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-MEDIA-CREATIVES',
                          account_id=account_id
                          line_item_id=line_item_id
                          account_media_id=account_media_id
                          landing_url=landing_url)


def preroll_call_to_actions_by_account_id(account_id, line_item_id, call_to_action, call_to_action_url):
    """
    Set the optional Call-to-Action (CTA) for a
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_id: The line item to associate this CTA to. (True)
    
    :param call_to_action: The Call-to-Action (CTA) text for the displayed butt
        on. Possible values are available on the enums page. (True)
    
    
    :param call_to_action_url: The URL to redirect the user to when they click 
        on the CTA button. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-PREROLL-CALL-TO-ACTIONS',
                          account_id=account_id
                          line_item_id=line_item_id
                          call_to_action=call_to_action
                          call_to_action_url=call_to_action_url)


def promoted__by_account_id(account_id, line_item_id, user_id):
    """
    Associate a Promoted Account to the specified line item.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_id: A reference to the line item you are operating with in
        the request. (True)
    
    
    :param user_id: A reference to a Twitter User Account by user ID. Use GET u
        sers/lookup to retrieve a user_id for a screen_name. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/promoted_accounts"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-PROMOTED-ACCOUNTS',
                          account_id=account_id
                          line_item_id=line_item_id
                          user_id=user_id)


def promoted_tweets_by_account_id(account_id, line_item_id, tweet_ids):
    """
    Associate one or more Promoted Tweets to the specified line item. Not all
    Tweets are appropriate for Tweet promotion, depending on the campaign
    objective. Please see
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_id: A reference to the line item you are operating with in
        the request. (True)
    
    
    :param tweet_ids: A comma-separated list of identifiers corresponding to sp
        ecific Tweets. Up to 50 ids may be provided. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/promoted_tweets"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-PROMOTED-TWEETS',
                          account_id=account_id
                          line_item_id=line_item_id
                          tweet_ids=tweet_ids)


def tailored_audience_changes_by_account_id(account_id, tailored_audience_id, input_file_path, operation):
    """
    Submit a change to a tailored audience.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t (True)
    
    
    :param tailored_audience_id: The identifier for the tailored audience. Type
        : string Example: c3po (True)
    
    
    :param input_file_path: The file path returned by the TON API endpoint. Typ
        e: string Example: /1.1/ton/data/ta_partner/1877861928/Axbsh2.csv
        (True)
    
    
    :param operation: The operation to take on this audience with the uploaded 
        list. Type: enum Possible values: ADD, REMOVE, REPLACE (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audience_changes"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCE-CHANGES',
                          account_id=account_id
                          tailored_audience_id=tailored_audience_id
                          input_file_path=input_file_path
                          operation=operation)


def tailored_audiences_by_account_id(account_id, name, list_type):
    """
    Create a new tailored audience to which many files can be uploaded.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The display name for this audience. (True)
    
    :param list_type: The type of list for this audience. Possible values inclu
        de EMAIL, DEVICE_ID, TWITTER_ID, HANDLE, PHONE_NUMBER. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES',
                          account_id=account_id
                          name=name
                          list_type=list_type)


def targeting_criteria_by_account_id(account_id, line_item_id, targeting_type, targeting_value, *, tailored_audience_expansion=IGNORE, tailored_audience_type=IGNORE):
    """
    Use the following endpoints to locate the correct
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param line_item_id: A reference to the line item you are operating with in
        the request. (True)
    
    
    :param targeting_type: The type of targeting that will be applied to this l
        ine item. Possible non-keyword-based values include: AGE,
        FOLLOWERS_OF_USER, SIMILAR_TO_FOLLOWERS_OF_USER, INTEREST, LOCATION,
        EVENT, PLATFORM, PLATFORM_VERSION, DEVICE, WIFI_ONLY, GENDER, TV_SHOW,
        NETWORK_OPERATOR, NETWORK_ACTIVATION_DURATION_LT, and
        NETWORK_ACTIVATION_DURATION_GTE. Possible keyword-based values include:
        BROAD_KEYWORD, UNORDERED_KEYWORD, PHRASE_KEYWORD,
        NEGATIVE_PHRASE_KEYWORD, NEGATIVE_UNORDERED_KEYWORD, EXACT_KEYWORD, and
        NEGATIVE_EXACT_KEYWORD. Possible tailored audience values include:
        TAILORED_AUDIENCE and TAILORED_AUDIENCE_EXPANDED. Possible behavior
        values: BEHAVIOR, NEGATIVE_BEHAVIOR, and BEHAVIOR_EXPANDED. Possible
        installed app store category values: APP_STORE_CATEGORY and
        APP_STORE_CATEGORY_LOOKALIKE. Possible Twitter Audience Platform (TAP)
        app blacklisting values: EXCLUDE_APP_LIST. (True)
    
    
    :param targeting_value: Specify which user, which interest, which location,
        which event, which platform, which platform version, which device,
        which keyword or phrase, which gender, which tailored audience, which
        behavior, which app store category, or which exclusion of an app list
        this targeting will be applied to, depending on the selected
        targeting_type. (True)
    
    
    :param tailored_audience_expansion: A boolean value for expansion. Only ava
        ilable for Tailored Audience CRM. (False)
    
    
    :param tailored_audience_type: A value for the tailored audience type: (Fal
        se)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-TARGETING-CRITERIA',
                          account_id=account_id
                          line_item_id=line_item_id
                          targeting_type=targeting_type
                          targeting_value=targeting_value
                          tailored_audience_expansion=tailored_audience_expansion
                          tailored_audience_type=tailored_audience_type)


def tweet_by_account_id(account_id, status, *, as_user_id=IGNORE, trim_user=IGNORE, media_ids=IGNORE, video_id=IGNORE, video_title=IGNORE, video_description=IGNORE, video_cta=IGNORE, video_cta_value=IGNORE, tweet_mode=IGNORE):
    """
    Create “Promoted-Only” Tweets. The Tweets posted via this endpoint can be
    used in Promoted Tweets campaigns but will not appear on the public
    timeline and are not served to followers.
    
    :param status: The text of your status update, typically up to 140 characte
        rs. URL encode as necessary. t.co link wrapping may affect character
        counts. (True)
    
    
    :param as_user_id: The user ID of the advertiser on behalf of whom you are 
        posting the Tweet The advertiser must grant your handle (or handles)
        access to their ads account via the Twitter UI at ads.twitter.com. This
        permission allows you to call the API using the OAuth tokens of your
        own handle rather than the advertiser's. (False)
    
    
    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param media_ids: A list of media ids to associate with the Tweet. You may 
        associated up to 4 media to a Tweet. See Uploading Media for further
        details on uploading media. (False)
    
    
    :param video_id: The Video UUID to be associated with thie Tweet. Please se
        e GET /videos for a list of eligible video UUIDs. (False)
    
    
    :param video_title: An optional title to be included with the video. This v
        alue has a max length of 160. (False)
    
    
    :param video_description: An optional description to be included with the v
        ideo. This value has a max length of 160. (False)
    
    
    :param video_cta: An optional CTA value for the associated video. Please se
        e the Enum page for a list of possible values. (False)
    
    
    :param video_cta_value: The value for the corresponding CTA on the associat
        ed video. This value is required if you've specified a video_cta and
        must be a valid URL. (False)
    
    
    :param tweet_mode: Value for the type of tweet being created. See Enums for
        more information. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tweet"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-TWEET',
                          status=status
                          as_user_id=as_user_id
                          trim_user=trim_user
                          media_ids=media_ids
                          video_id=video_id
                          video_title=video_title
                          video_description=video_description
                          video_cta=video_cta
                          video_cta_value=video_cta_value
                          tweet_mode=tweet_mode
                          account_id=account_id)


def videos_by_account_id(account_id, video_media_id, *, poster_image_media_id=IGNORE, title=IGNORE, description=IGNORE):
    """
    Associate a video with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all Ads
        API requests excluding GET accounts. The specified account must be
        associated with the authenticating user. (True)
    
    
    :param video_media_id: The media_id for the uploaded video content. Please 
        see POST media/upload (chunked) for more information about uploading
        videos. (True)
    
    
    :param poster_image_media_id: Specify a poster image for the video using th
        e media_id of an uploaded image. If not specified, the first frame will
        be used. Only the owner of the video—that is, the authenticated user at
        the time of upload—can set the poster image. Poster image dimensions
        should match the video dimensions. This is a write-only field. In
        response, the API will provide a Twitter URL for this image, which can
        be reused. (False)
    
    
    :param title: A string value to populate the video title with. This value i
        s not user-facing and is only utilized for identification purposes in
        the GET accounts/:account_id/videos endpoint and the Twitter Ads UI
        video library. (False)
    
    
    :param description: A string value to populate the video description with. 
        This value is not user-facing and is only utilized for identification
        purposes in the GET accounts/:account_id/videos endpoint and the
        Twitter Ads UI video library. (False)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/videos"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-VIDEOS',
                          account_id=account_id
                          video_media_id=video_media_id
                          poster_image_media_id=poster_image_media_id
                          title=title
                          description=description)


def web_event_tags_by_account_id(account_id, name, click_window, view_through_window, type, retargeting_enabled):
    """
    Create a new web event tag associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param name: The name of the web tag. (True)
    
    :param click_window: The click window for this web tag. Possible values are
        1, 7, 14, 30, 60 or 90. (True)
    
    
    :param view_through_window: The view through window for this web tag. This 
        value must always be less than or equal to the click_window value.
        Possible values are 0, 1, 7, 14, 30, 60 or 90. (True)
    
    
    :param type: The type of web tag. Possible values are SITE_VISIT, PURCHASE,
        DOWNLOAD, SIGN_UP, CUSTOM. (True)
    
    
    :param retargeting_enabled: Boolean indicating if retargeting should be ena
        bled for this web tag. Possible values are true, 1, false, 0. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-ACCOUNTS-ACCOUNT-ID-WEB-EVENT-TAGS',
                          account_id=account_id
                          name=name
                          click_window=click_window
                          view_through_window=view_through_window
                          type=type
                          retargeting_enabled=retargeting_enabled)


def 1/accounts/():
    """
    
    """
    url = "https://ads-api-sandbox.twitter.com/1/accounts/"
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-1-ACCOUNTS')


def features__by_account_id(account_id, type):
    """
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param type: A comma separated list of account features to be added to the 
        account. (True)
    """
    url = "https://ads-api-sandbox.twitter.com/1/accounts/{account_id}/features"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-1-ACCOUNTS-ACCOUNT-ID-FEATURES',
                          account_id=account_id
                          type=type)


def funding_instruments_by_account_id(account_id, type, currency, start_time, *, funded_amount_local_micro=IGNORE, credit_limit_local_micro=IGNORE, end_time=IGNORE):
    """
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param type: The type of funding instrument to create as one of: INSERTION_
        ORDER, CREDIT_LINE, AGENCY_CREDIT_LINE, PARTNER_MANAGED, CREDIT_CARD.
        (True)
    
    
    :param currency: The type of currency to assign to funding instrument, iden
        tified using ISO-4217. This is a three-letter string like “USD” or
        “EUR”. Omit this parameter to retrieve all bidding rules. (True)
    
    
    :param funded_amount_local_micro: (Only applicable to some funding instrume
        nt types) Integer representing the total budget amount allocated in
        local micro. (False)
    
    
    :param credit_limit_local_micro: (Only applicable to some funding instrumen
        t types) Integer representing the total credit available against this
        funding instrument. (False)
    
    
    :param start_time: The date for the funding instrument to become active and
        usable. Expressed in ISO_8601. (True)
    
    
    :param end_time: The date for funding instrument to become inactive. Expres
        sed in ISO_8601. (False)
    """
    url = "https://ads-api-sandbox.twitter.com/1/accounts/{account_id}/funding_instruments"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-1-ACCOUNTS-ACCOUNT-ID-FUNDING-INSTRUMENTS',
                          account_id=account_id
                          type=type
                          currency=currency
                          funded_amount_local_micro=funded_amount_local_micro
                          credit_limit_local_micro=credit_limit_local_micro
                          start_time=start_time
                          end_time=end_time)


def tailored_audiences_by_account_id(account_id, name, list_type):
    """
    Create a new tailored audience to which many files can be uploaded.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param name: The display name for this audience. (True)
    
    :param list_type: The type of list for this audience. Possible values inclu
        de EMAIL, DEVICE_ID, TWITTER_ID, HANDLE, PHONE_NUMBER. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences"
    url = url.format(account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-1-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES',
                          account_id=account_id
                          name=name
                          list_type=list_type)


def tailored_audiences_permissions_by_id_and_account_id(id, account_id, granted_account_id, permission_level):
    """
    Creates a new permission object allowing this specific audience to be
    shared with a given account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param granted_account_id: The advertiser account ID you wish to set permis
        sions for on this tailored audiences. (True)
    
    
    :param permission_level: The permission level you want to grant for this ac
        count and tailored audience. Valid values here are READ_ONLY and
        READ_WRITE. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}/permissions"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('POST',
                          url,
                          'ADS:ACCOUNTS',
                          'POST-1-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES-ID-PERMISSIONS',
                          account_id=account_id
                          granted_account_id=granted_account_id
                          permission_level=permission_level
                          id=id)


def app_event_provider_configurations_by_id_and_account_id(id, account_id):
    """
    Disassociate a specific application event provider configuration associated
    with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param id: The identifier for the application event provider. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_event_provider_configurations/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-APP-EVENT-PROVIDER-CONFIGURATIONS-ID',
                          account_id=account_id
                          id=id)


def app_event_tags_by_id_and_account_id(id, account_id):
    """
    Disassociate a specific application event tag associated from the current
    account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param id: The identifier for the application event tag. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-APP-EVENT-TAGS-ID',
                          account_id=account_id
                          id=id)


def campaigns_by_campaign_id_and_account_id(campaign_id, account_id):
    """
    Delete an existing campaign associated with the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param campaign_id: The identifier for a campaign associated with the curre
        nt account. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/campaigns/{campaign_id}"
    url = url.format(account_id=account_id,
                     campaign_id=campaign_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-CAMPAIGNS-CAMPAIGN-ID',
                          account_id=account_id
                          campaign_id=campaign_id)


def cards_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given app download card. This card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-CARDS-APP-DOWNLOAD-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_image_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given image app download card. This card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-APP-DOWNLOAD-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_image_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given image conversation card.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-CARDS-IMAGE-CONVERSATION-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_video_app_download_by_id_and_account_id(id, account_id, card_id):
    """
    Delete a given Video App Download Card. This card is part of our
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "DELETE accounts/{account_id}/cards/video_app_download/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-APP-DOWNLOAD-ID',
                          account_id=account_id
                          card_id=card_id
                          id=id)


def cards_video_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given video conversation card.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-CARDS-VIDEO-CONVERSATION-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def cards_website_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given website card.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param card_id: The identifier for the specific card. (True)
    """
    url = "DELETE accounts/{account_id}/cards/website/{card_id}"
    url = url.format(card_id=card_id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-CARDS-WEBSITE-CARD-ID',
                          account_id=account_id
                          card_id=card_id)


def line_item_apps_by_line_item_app_id_and_account_id(line_item_app_id, account_id):
    """
    Delete a specific line item to mobile app association.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_app_id: The identifier for a line item app associated with
        the current account. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps/{line_item_app_id}"
    url = url.format(account_id=account_id,
                     line_item_app_id=line_item_app_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-LINE-ITEM-APPS-LINE-ITEM-APP-ID',
                          account_id=account_id
                          line_item_app_id=line_item_app_id)


def line_items_by_line_item_id_and_account_id(line_item_id, account_id):
    """
    Delete the specified line item belonging to the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param line_item_id: A reference to the line item you are operating with in
        the request. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/line_items/{line_item_id}"
    url = url.format(account_id=account_id,
                     line_item_id=line_item_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-LINE-ITEMS-LINE-ITEM-ID',
                          account_id=account_id
                          line_item_id=line_item_id)


def media_creatives_by_id_and_account_id(id, account_id):
    """
    Removes a media creative for the current ads account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (True)
    
    
    :param id: The identifier for the media id associated with the current acco
        unt. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-MEDIA-CREATIVES-ID',
                          account_id=account_id
                          id=id)


def preroll_call_to_actions_by_preroll_call_to_action_id_and_account_id(preroll_call_to_action_id, account_id):
    """
    Deletes a Call-to-Action (CTAs) associated with a line item on this
    account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param preroll_call_to_action_id: A reference to the prerol call to action 
        you are operating with in the request. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions/{preroll_call_to_action_id}"
    url = url.format(account_id=account_id,
                     preroll_call_to_action_id=preroll_call_to_action_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-PREROLL-CALL-TO-ACTIONS-PREROLL-CALL-TO-ACTION-ID',
                          account_id=account_id
                          preroll_call_to_action_id=preroll_call_to_action_id)


def promoted_tweets_by_id_and_account_id(id, account_id):
    """
    Disassociate a Promoted Tweet from a line item by specifying its instance
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param id: This identifier refers to the instance of a Promoted Tweet assoc
        iated with a line item. This comes from the id field from a response
        item to GET accounts/:account_id/promoted_tweets, not the tweet_id of
        the Tweet in question. Supplied within the resource's path. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/promoted_tweets/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-PROMOTED-TWEETS-ID',
                          account_id=account_id
                          id=id)


def tailored_audiences_by_id_and_account_id(id, account_id):
    """
    Delete a tailored audience from an account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param id: The identifier for the tailored audience. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES-ID',
                          account_id=account_id
                          id=id)


def targeting_criteria_by_id_and_account_id(id, account_id):
    """
    Remove a targeting criterion associated with a line item.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param id: The identifier for a targeting criteria associated with a campai
        gn's line items. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-TARGETING-CRITERIA-ID',
                          account_id=account_id
                          id=id)


def videos_by_id_and_account_id(id, account_id, video_id):
    """
    Delete the specified video belonging to the current ads account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param video_id: The UUID identifier of the video object to be deleted. (Tr
        ue)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/videos/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-VIDEOS-ID',
                          account_id=account_id
                          video_id=video_id
                          id=id)


def web_event_tags_by_id_and_account_id(id, account_id, web_event_tag_id):
    """
    Delete a specific web event tag associated to the current account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param web_event_tag_id: The identifier for the web event tag. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-ACCOUNTS-ACCOUNT-ID-WEB-EVENT-TAGS-ID',
                          account_id=account_id
                          web_event_tag_id=web_event_tag_id
                          id=id)


def by_account_id(account_id):
    """
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    """
    url = "https://ads-api-sandbox.twitter.com/1/accounts/{account_id}"
    url = url.format(account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-1-ACCOUNTS-ACCOUNT-ID',
                          account_id=account_id)


def features_by_account_id(account_id, type):
    """
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param type: A comma-separated list of account features to remove from the 
        account. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/features"
    url = url.format(account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-1-ACCOUNTS-ACCOUNT-ID-FEATURES',
                          account_id=account_id
                          type=type)


def funding_instruments_by_id_and_account_id(id, account_id, funding_instrument_id):
    """
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param funding_instrument_id: The identifier of funding instrument to delet
        e. (True)
    """
    url = "https://ads-api-sandbox.twitter.com/1/accounts/{account_id}/funding_instruments/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-1-ACCOUNTS-ACCOUNT-ID-FUNDING-INSTRUMENTS-ID',
                          account_id=account_id
                          funding_instrument_id=funding_instrument_id
                          id=id)


def tailored_audiences_by_id_and_account_id(id, account_id):
    """
    Delete a tailored audience from an account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param id: The identifier for the tailored audience. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-1-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES-ID',
                          account_id=account_id
                          id=id)


def tailored_audiences_permissions_by_id_and_account_id(id, account_id, tailored_audience_id, tailored_audience_permission_id):
    """
    Revokes permissions to a specific audience already shared with a different
    advertiser account.
    
    :param account_id: The identifier for the leveraged account. Appears within
        the resource's path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. (True)
    
    
    :param tailored_audience_id: The ID of the tailored audience. (True)
    
    :param tailored_audience_permission_id: The ID of the tailored audience per
        mission object. (True)
    """
    url = "https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}/permissions"
    url = url.format(id=id,
                     account_id=account_id)
    return TwitterRequest('DELETE',
                          url,
                          'ADS:ACCOUNTS',
                          'DELETE-1-ACCOUNTS-ACCOUNT-ID-TAILORED-AUDIENCES-ID-PERMISSIONS',
                          account_id=account_id
                          tailored_audience_id=tailored_audience_id
                          tailored_audience_permission_id=tailored_audience_permission_id
                          id=id)



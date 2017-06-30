###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def accounts(*, with_deleted=ELIDE, sort_by=ELIDE):
    """
    Retrieve all of the advertising-enabled accounts the authenticating user
    has access to.

    :param with_deleted: Include deleted results for your request. Defaults to
        false.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See sorting for more information.
    """
    binding = {'with_deleted': with_deleted, 'sort_by': sort_by}
    url = 'https://ads-api.twitter.com/1/accounts'
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts',
                          binding)


def by_account_id(account_id, *, with_deleted=ELIDE):
    """
    Retrieve detailed information on the specified account that the
    authenticating user has access to.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id',
                          binding)


def account_media_by_account_id(account_id, *, count=ELIDE, sort_by=ELIDE,
                                cursor=ELIDE, with_deleted=ELIDE,
                                account_media_ids=ELIDE):
    """
    Retrieve account media for the specified ads account.

    :param count:  (Int)

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (an account id)

    :param sort_by:  (a sortable field)

    :param cursor:  (Cursor)

    :param with_deleted:  (Boolean)

    :param account_media_ids:  (an id)
    """
    binding = {'count': count, 'account_id': account_id, 'sort_by': sort_by,
               'cursor': cursor, 'with_deleted': with_deleted,
               'account_media_ids': account_media_ids}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/account_media'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-account-media',
                          binding)


def account_media_by_id_and_account_id(id, account_id, *, count=ELIDE,
                                       sort_by=ELIDE, cursor=ELIDE,
                                       with_deleted=ELIDE,
                                       account_media_ids=ELIDE):
    """
    Retrieves details for specified account media associated to current ads
    account.

    :param count:  (Int)

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (an account id)

    :param sort_by:  (a sortable field)

    :param cursor:  (Cursor)

    :param with_deleted:  (Boolean)

    :param account_media_ids:  (an id)
    """
    binding = {'count': count, 'account_id': account_id, 'sort_by': sort_by,
               'cursor': cursor, 'with_deleted': with_deleted,
               'account_media_ids': account_media_ids, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/account_media/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-account-media-id',
                          binding)


def app_event_provider_configurations_by_account_id(account_id, *,
                                                    with_deleted=ELIDE):
    """
    Retrieve all application event provider configurations associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_event_provider_configurations'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-app-event-provider-configurations',
                          binding)


def app_event_tags_by_account_id(account_id, *, with_deleted=ELIDE,
                                 sort_by=ELIDE):
    """
    Retrieve all application event tags associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.
    """
    binding = {'account_id': account_id, 'with_deleted': with_deleted,
               'sort_by': sort_by}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-app-event-tags',
                          binding)


def app_event_tags_by_id_and_account_id(id, account_id, *, with_deleted=ELIDE):
    """
    Retrieve a specific application event tag associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier for the application event tag.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'id': id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-app-event-tags-id',
                          binding)


def app_lists_by_account_id(account_id):
    """
    Retrieve details for all the app_lists associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.
    """
    binding = {'account_id': account_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_lists'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-app-lists',
                          binding)


def app_lists_by_app_list_id_and_account_id(app_list_id, account_id):
    """
    Retrieve details for an

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param app_list_id: Scope the response to just the desired app_list by
        specifying an identifier.
    """
    binding = {'account_id': account_id, 'app_list_id': app_list_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_lists/{app_list_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-app-lists-app-list-id',
                          binding)


def auction_insights_by_account_id(account_id, line_item_ids, start_time,
                                   end_time, granularity, placement):
    """
    Retrieve auction insights for specific line items belonging to the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_ids: Scope the response to just the desired line items by
        specifying a comma-separated list of identifiers. Up to 50 ids may be
        provided.

    :param start_time: Scopes the retrieved data to data collected in the
        window of time between start_time and end_time. Expressed in ISO 8601.
        This value must be aligned to midnight in the account’s timezone. If no
        timestamp or offset is specified, the date will default to this
        timezone automatically.

    :param end_time: Scopes the retrieved data to data collected in the window
        of time between start_time and end_time. Expressed in ISO 8601. This
        value must be aligned to midnight in the account’s timezone. If no
        timestamp or offset is specified, the date will default to this
        timezone automatically.

    :param granularity: Determines how granular the data points will be
        returned for each data point type within the time range specified by
        start_time and end_time. Possible values include: DAY, TOTAL.

    :param placement: The placement - for the possible values, see enumerations
    """
    binding = {'account_id': account_id, 'line_item_ids': line_item_ids,
               'start_time': start_time, 'end_time': end_time, 'granularity':
               granularity, 'placement': placement}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/auction_insights'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-auction-insights',
                          binding)


def authenticated_user_access_by_account_id(account_id):
    """
    Retrieve the permissions of the currently authenticated user (access_token)
    as they relate to this ads account.
    """
    binding = {'account_id': account_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/authenticated_user_access'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-authenticated-user-access',
                          binding)


def campaigns_by_account_id(account_id, *, campaign_ids=ELIDE,
                            funding_instrument_ids=ELIDE, with_deleted=ELIDE,
                            count=ELIDE, cursor=ELIDE, sort_by=ELIDE,
                            draft_only=ELIDE):
    """
    Retrieve details for some or all campaigns associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param campaign_ids: Scope the response to just the desired campaigns by
        specifying a comma-separated list of identifiers. Up to 50 ids may be
        provided.

    :param funding_instrument_ids: Scope the response to just the desired
        funding instruments by specifying a comma-separated list of
        identifiers. Up to 50 ids may be provided.

    :param with_deleted: Include deleted results for your request.

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See sorting for more information.

    :param draft_only: Scope the response to just draft campaigns.
    """
    binding = {'account_id': account_id, 'campaign_ids': campaign_ids,
               'funding_instrument_ids': funding_instrument_ids,
               'with_deleted': with_deleted, 'count': count, 'cursor': cursor,
               'sort_by': sort_by, 'draft_only': draft_only}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/campaigns'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-campaigns',
                          binding)


def campaigns_by_campaign_id_and_account_id(campaign_id, account_id, *,
                                            with_deleted=ELIDE):
    """
    Retrieve details for a specific campaign associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param campaign_id: The identifier for a campaign associated with the
        current account.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'campaign_id': campaign_id,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/campaigns/{campaign_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-campaigns-campaign-id',
                          binding)


def cards_app_download_by_account_id(account_id, *, card_ids=ELIDE,
                                     with_deleted=ELIDE, count=ELIDE,
                                     cursor=ELIDE, sort_by=ELIDE):
    """
    Retrieve card information about app download cards for a given account.
    This card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_ids: Include specific cards in your request.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'with_deleted':
               with_deleted, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-app-download',
                          binding)


def cards_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve card information about a given app download card. This card is
    part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-app-download-card-id',
                          binding)


def cards_image_app_download_by_account_id(account_id, *, card_ids=ELIDE,
                                           with_deleted=ELIDE, count=ELIDE,
                                           cursor=ELIDE, sort_by=ELIDE):
    """
    Retrieve card information about image app download cards for a given
    account. This card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_ids: Include specific cards in your request.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'with_deleted':
               with_deleted, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-image-app-download',
                          binding)


def cards_image_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve card information about a given image app download card. This card
    is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-image-app-download-card-id',
                          binding)


def cards_image_conversation_by_account_id(account_id, *, card_ids=ELIDE,
                                           with_deleted=ELIDE, count=ELIDE,
                                           cursor=ELIDE, sort_by=ELIDE):
    """
    Retrieve information about image conversation cards for a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_ids: Include specific cards in your request.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'with_deleted':
               with_deleted, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-image-conversation',
                          binding)


def cards_image_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve information about a given image conversation card.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-image-conversation-card-id',
                          binding)


def cards_video_app_download_by_account_id(account_id, *, with_deleted=ELIDE,
                                           count=ELIDE, cursor=ELIDE):
    """
    Retrieve card information about all Video App Download Cards for the
    specified account. This card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param count: Specifies the number of Video App Download Card items to try
        and retrieve.

    :param cursor: Specifies a cursor to get the next page of Video App
        Download Cards. See Pagination for more information.
    """
    binding = {'account_id': account_id, 'with_deleted': with_deleted,
               'count': count, 'cursor': cursor}
    url = 'GET accounts/{account_id}/cards/video_app_download'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-video-app-download',
                          binding)


def cards_video_app_download_by_id_and_account_id(id, account_id):
    """
    Retrieve card information about a given Video App Download Card. This card
    is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier of the specific Video App Download Card to be
        updated.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'GET accounts/{account_id}/cards/video_app_download/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-video-app-download-id',
                          binding)


def cards_video_conversation_by_account_id(account_id, *, card_ids=ELIDE,
                                           with_deleted=ELIDE, count=ELIDE,
                                           cursor=ELIDE, sort_by=ELIDE):
    """
    Retrieve information about video conversation cards for a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_ids: Include specific cards in your request.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'with_deleted':
               with_deleted, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-video-conversation',
                          binding)


def cards_video_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Retrieve information about a given video conversation card.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-video-conversation-card-id',
                          binding)


def cards_website_by_account_id(account_id, *, card_ids=ELIDE,
                                with_deleted=ELIDE, count=ELIDE,
                                cursor=ELIDE, sort_by=ELIDE):
    """
    Retrieve card information about website cards for a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_ids: Include specific cards in your request.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'with_deleted':
               with_deleted, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by}
    url = 'GET accounts/{account_id}/cards/website'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-website',
                          binding)


def cards_website_by_card_id_and_account_id(account_id, *, card_id=ELIDE):
    """
    Retrieve card information about a given website card.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'GET accounts/{account_id}/cards/website/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-cards-website-card-id',
                          binding)


def features_by_account_id(account_id, *, feature_keys=ELIDE):
    """
    Retrieve the collection of whitelisted features accessible by this ads
    account. Features are indicated by a descriptive feature key and are only
    exposed on this endpoint if they are introduced in beta or an otherwise
    limited release and are available in the API. Features that do not meet
    this criteria will not be exposed on this endpoint.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param feature_keys: An optional parameter that enables querying for a
        specific feature key. Requests may include multiple comma-separated
        keys. Only the features that are accessible by this account will be
        included in the response.
    """
    binding = {'account_id': account_id, 'feature_keys': feature_keys}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/features'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-features',
                          binding)


def funding_instruments_by_account_id(account_id, *,
                                      funding_instrument_ids=ELIDE,
                                      with_deleted=ELIDE, sort_by=ELIDE):
    """
    Retrieve some or all funding instruments associated with the account
    specified in the path.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param funding_instrument_ids: Scope the response to just the desired
        funding instruments by specifying a comma-separated list of
        identifiers. Up to 50 ids may be provided.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.
    """
    binding = {'account_id': account_id, 'funding_instrument_ids':
               funding_instrument_ids, 'with_deleted': with_deleted,
               'sort_by': sort_by}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/funding_instruments'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-funding-instruments',
                          binding)


def funding_instruments_by_id_and_account_id(id, account_id, *,
                                             with_deleted=ELIDE):
    """
    Retrieve a specific funding instrument associated with the account
    specified in the path.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier for a funding instrument associated with the
        current account.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'id': id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/funding_instruments/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-funding-instruments-id',
                          binding)


def line_item_apps_by_account_id(account_id, *, line_item_id=ELIDE,
                                 line_item_app_ids=ELIDE, count=ELIDE,
                                 cursor=ELIDE, with_deleted=ELIDE):
    """
    Retrieve line item to mobile app associations

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_id: Scope response to a specific line item by providing
        its identifier.

    :param line_item_app_ids: Scope response to a set of line item apps

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param with_deleted: Include deleted results for your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'line_item_app_ids': line_item_app_ids, 'count': count,
               'cursor': cursor, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-line-item-apps',
                          binding)


def line_item_apps_by_line_item_app_id_and_account_id(line_item_app_id,
                                                      account_id, *,
                                                      with_deleted=ELIDE):
    """
    Retrieve a specific line item to mobile app association.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_app_id: The identifier for a line item app associated with
        the current account.

    :param with_deleted: Include deleted results for your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'line_item_app_id': line_item_app_id,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps/{line_item_app_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-line-item-apps-line-item-app-id',
                          binding)


def line_items_by_account_id(account_id, *, campaign_ids=ELIDE,
                             line_item_ids=ELIDE,
                             funding_instrument_ids=ELIDE,
                             with_deleted=ELIDE, count=ELIDE, cursor=ELIDE,
                             sort_by=ELIDE, draft_only=ELIDE):
    """
    Retrieve the line items associated with a specific campaign belonging to
    the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param campaign_ids: Scope the response to just the desired campaigns by
        specifying a comma-separated list of identifiers. Up to 50 ids may be
        provided.

    :param line_item_ids: Scope the response to just the desired line items by
        specifying a comma-separated list of identifiers. Up to 50 ids may be
        provided.

    :param funding_instrument_ids: Scope the response to just the desired
        funding instruments by specifying a comma-separated list of
        identifiers. Up to 50 ids may be provided.

    :param with_deleted: Include deleted results for your request.

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See sorting for more information.

    :param draft_only: Scope the response to just draft line items.
    """
    binding = {'account_id': account_id, 'campaign_ids': campaign_ids,
               'line_item_ids': line_item_ids, 'funding_instrument_ids':
               funding_instrument_ids, 'with_deleted': with_deleted, 'count':
               count, 'cursor': cursor, 'sort_by': sort_by, 'draft_only':
               draft_only}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_items'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-line-items',
                          binding)


def line_items_by_line_item_id_and_account_id(line_item_id, account_id, *,
                                              with_deleted=ELIDE):
    """
    Retrieve a specific line item associated with a campaign belonging to the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_id: A reference to the line item you are operating with in
        the request.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_items/{line_item_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-line-items-line-item-id',
                          binding)


def media_creatives_by_account_id(account_id, *, draft_only=ELIDE):
    """
    Retrieve details for all the media_creatives associated with the current
    account.

    :param draft_only: Scope the response to media creatives under draft
        campaigns.
    """
    binding = {'draft_only': draft_only, 'account_id': account_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-media-creatives',
                          binding)


def media_creatives_by_id_and_account_id(id, account_id):
    """
    Retrieves details for a specific media creative associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier for a media_creative associated with the current
        account.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-media-creatives-id',
                          binding)


def preroll_call_to_actions_by_account_id(account_id, line_item_id, *,
                                          with_deleted=ELIDE, count=ELIDE,
                                          cursor=ELIDE, draft_only=ELIDE):
    """
    Get the Call-to-Actions (CTAs) associated with line items on this account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_id: Filter results to a specific line_item_id.

    :param with_deleted: Include deleted results for your request.

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param draft_only: Scope the response to CTAs associated with line items
        under draft campaigns.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'with_deleted': with_deleted, 'count': count, 'cursor': cursor,
               'draft_only': draft_only}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-preroll-call-to-actions',
                          binding)


def preroll_call_to_actions_preroll_call_to_action_id_by_account_id(account_id,
                                                                    line_item_id,
                                                                    *,
                                                                    with_deleted=ELIDE,
                                                                    count=ELIDE,
                                                                    cursor=ELIDE):
    """
    Retrieve a specific Call-to-Action (CTAs) associated with this account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_id: Filter results to a specific line_item_id.

    :param with_deleted: Include deleted results for your request. Defaults to
        false.

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'with_deleted': with_deleted, 'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions/:preroll_call_to_action_id'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-preroll-call-to-actions-preroll-call-to-action-id',
                          binding)


def promotable_users_by_account_id(account_id, *, with_deleted=ELIDE):
    """
    Returns the collection of promotable_users associated with an account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/promotable_users'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-promotable-users',
                          binding)


def promoted__by_account_id(account_id, *, line_item_id=ELIDE,
                            promoted_account_ids=ELIDE, with_deleted=ELIDE,
                            count=ELIDE, cursor=ELIDE, sort_by=ELIDE,
                            draft_only=ELIDE):
    """
    Retrieve references to the Promoted Accounts associated with one or more
    line items.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_id: A reference to the line item you are operating with in
        the request. Omitting the line_item_id will return all promoted
        accounts across all campaigns.

    :param promoted_account_ids: Scope the response to the specified, comma-
        separated list of promoted account IDs. These identifiers refer to a
        associated Promoted Account with a line item. This comes from the id
        field from a response item to GET
        accounts/:account_id/promoted_accounts. Supplied within the resource’s
        path.

    :param with_deleted: Include deleted results in your request.

    :param count: Specifies the number of Promoted Accounts to try to retrieve,
        up to a maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of Promoted
        Accounts. See Pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information.

    :param draft_only: Scope the response to Promoted Accounts under draft
        campaigns.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'promoted_account_ids': promoted_account_ids, 'with_deleted':
               with_deleted, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by, 'draft_only': draft_only}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/promoted_accounts'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-promoted-accounts',
                          binding)


def promoted_tweets_by_account_id(account_id, *, line_item_ids=ELIDE,
                                  line_item_id=ELIDE, with_deleted=ELIDE,
                                  count=ELIDE, cursor=ELIDE, sort_by=ELIDE,
                                  draft_only=ELIDE):
    """
    Retrieve references to the Promoted Tweets associated with one or more line
    items.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_ids: Scope the response to just the desired line items by
        specifying a comma-separated list of identifiers. Up to 200 ids may be
        provided.

    :param line_item_id: Specify an identifier for a single line item by
        specifying its line item identifier.

    :param with_deleted: Include deleted results for your request. Defaults to
        false.

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See sorting for more information.

    :param draft_only: Scope the response to Promoted Tweets under draft
        campaigns.
    """
    binding = {'account_id': account_id, 'line_item_ids': line_item_ids,
               'line_item_id': line_item_id, 'with_deleted': with_deleted,
               'count': count, 'cursor': cursor, 'sort_by': sort_by,
               'draft_only': draft_only}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/promoted_tweets'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-promoted-tweets',
                          binding)


def recommendations_by_account_id(account_id):
    """
    Status:

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.
    """
    binding = {'account_id': account_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/recommendations'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-recommendations',
                          binding)


def recommendations_by_recommendation_id_and_account_id(recommendation_id,
                                                        account_id):
    """
    Status:

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param recommendation_id: A specific recommendation_id to retrieve details
        for.
    """
    binding = {'account_id': account_id, 'recommendation_id':
               recommendation_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/recommendations/{recommendation_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-recommendations-recommendation-id',
                          binding)


def scoped_timeline_by_account_id(account_id, *, user_id=ELIDE,
                                  user_ids=ELIDE, scoped_to=ELIDE,
                                  objective=ELIDE, trim_user=ELIDE,
                                  count=ELIDE, cursor=ELIDE, tweet_mode=ELIDE):
    """
    Retrieve up to 200 of the most recent promotable Tweets created by the
    specified Twitter user. This user may be any account for which the current
    account has account access. This endpoint works for any user with access to
    an Ads Account, not only the Twitter @handle which authors the promotable
    Tweets.

    :param user_id: Specifies the user to scope Tweets to. Defaults to the FULL
        promotable user on the account when not set.

    :param user_ids: Limits tweets to the specified users. Comma-separated list
        of user ids. The requesting user must have full promotable access to
        the specified list of accounts.

    :param scoped_to: followers to find Tweets in the account’s timeline or
        none to find Promoted-Only Tweets

    :param objective: Filter the results to only those Tweets appropriate for
        the given objective. See note above (top of page) about how filtering
        by objective affects result paging.

    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param count: Specifies the number of tweets to try and retrieve, up to a
        maximum of 200 per distinct request. The value of count is best thought
        of as a limit to the number of tweets to return because suspended or
        deleted content is removed after the count has been applied.

    :param cursor: Specifies a cursor to get the next page of tweets. See
        Pagination for more information.

    :param tweet_mode: Value for the type of tweet being created. See Enums for
        more information.
    """
    binding = {'user_id': user_id, 'user_ids': user_ids, 'scoped_to':
               scoped_to, 'objective': objective, 'trim_user': trim_user,
               'count': count, 'cursor': cursor, 'tweet_mode': tweet_mode,
               'account_id': account_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/scoped_timeline'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-scoped-timeline',
                          binding)


def tailored_audience_changes_by_account_id(account_id, *, count=ELIDE,
                                            cursor=ELIDE):
    """
    Retrieve all audience changes submitted.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information.
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audience_changes'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-tailored-audience-changes',
                          binding)


def tailored_audience_changes_by_id_and_account_id(id, account_id):
    """
    Retrieve a specific tailored audience change record.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier for this tailored audience change record.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audience_changes/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-tailored-audience-changes-id',
                          binding)


def tailored_audiences_by_account_id(account_id, *, count=ELIDE,
                                     cursor=ELIDE, with_deleted=ELIDE):
    """
    Retrieve tailored audiences associated with a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-tailored-audiences',
                          binding)


def tailored_audiences_by_id_and_account_id(id, account_id, *,
                                            with_deleted=ELIDE):
    """
    Retrieve specific tailored audience associated with a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier for a tailored audience associated with the
        current account.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'id': id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-tailored-audiences-id',
                          binding)


def targeting_criteria_by_account_id(account_id, line_item_id, *, lang=ELIDE,
                                     with_deleted=ELIDE, draft_only=ELIDE):
    """
    Retrieve the targeting criteria associated with line items owned by the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_id: Scope targeting criteria to a specific line item by
        providing its identifier.

    :param lang: An ISO-639-1 language code. When passed, an additional
        localized_name attribute will be returned in the response for objects
        where a localized name is available.

    :param with_deleted: Include deleted results for your request.

    :param draft_only: Scope the response to targeting criteria associated with
        line items under draft campaigns.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id, 'lang':
               lang, 'with_deleted': with_deleted, 'draft_only': draft_only}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-targeting-criteria',
                          binding)


def targeting_criteria_by_id_and_account_id(id, account_id,
                                            targeting_criterion_id, *,
                                            lang=ELIDE, with_deleted=ELIDE):
    """
    Retrieve detailed information on a targeting criterion associated with a
    specific line item.

    :param lang:  (String)

    :param targeting_criterion_id:  (an id)

    :param with_deleted:  (Boolean)

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. (an account id)
    """
    binding = {'lang': lang, 'targeting_criterion_id': targeting_criterion_id,
               'with_deleted': with_deleted, 'account_id': account_id, 'id':
               id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-targeting-criteria-id',
                          binding)


def targeting_suggestions_by_account_id(account_id, suggestion_type,
                                        targeting_values, *, count=ELIDE):
    """
    Get up to 50 targeting suggestion for HANDLES or KEYWORDS to complement
    your initial selection.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param suggestion_type: You can either receive KEYWORD or USER_ID
        suggestions.

    :param targeting_values: A comma separated collection of either KEYWORD or
        USER_ID to seed the the suggestions. These two types of suggestions can
        not be mixed, you can either send KEYWORD s and get KEYWORD s back or
        send USER_ID s to get some USER_ID s in return.

    :param count: The total number of suggestions returned by this endpoint.
        Default is 30. Minimum is 1 and Maximum is 50.
    """
    binding = {'account_id': account_id, 'suggestion_type': suggestion_type,
               'targeting_values': targeting_values, 'count': count}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/targeting_suggestions'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-targeting-suggestions',
                          binding)


def tweet_preview__by_account_id(account_id, status, *, as_user_id=ELIDE,
                                 media_ids=ELIDE, card_id=ELIDE,
                                 preview_target=ELIDE):
    """
    Preview a Tweet that does not already exist as it would appear across a
    variety of different platforms; iPhone, Android and Web. You can preview a
    Tweet both for how it will look like on Twitter or on the

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param status: The text of your status update, typically up to 140
        characters. URL encode as necessary. t.co link wrapping may affect
        character counts.

    :param as_user_id: The user ID of the advertiser on behalf of whom you are
        posting the Tweet The advertiser must grant your handle (or handles)
        access to their ads account via the Twitter UI at ads.twitter.com. This
        permission allows you to call the API using the OAuth tokens of your
        own handle rather than the advertiser’s.

    :param media_ids: A list of up to four media ids to associate with the
        Tweet. See Uploading Media for further details on uploading media.
        Please note that we currently only support image media_ids.

    :param card_id: The ID of the revenue card embedded in the Tweet.

    :param preview_target: The target to render the Tweet preview for. You can
        preview a Tweet both for how it will look like on Twitter (
        TWITTER_TIMELINE ) or on the Twitter Audience Platform (
        PUBLISHER_NETWORK ). When using the PUBLISHER_NETWORK value for the
        preview_target parameter you should not use a card_id and you must
        specify media_ids. Defaults to TWITTER_TIMELINE.
    """
    binding = {'account_id': account_id, 'status': status, 'as_user_id':
               as_user_id, 'media_ids': media_ids, 'card_id': card_id,
               'preview_target': preview_target}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tweet/preview/'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-tweet-preview',
                          binding)


def tweet_preview_by_tweet_id_and_account_id(tweet_id, account_id, *,
                                             as_user_id=ELIDE,
                                             preview_target=ELIDE):
    """
    Preview an existing Tweet as it would appear across a variety of different
    platforms; iPhone, Android and Web. You can preview a Tweet both for how it
    will look like on Twitter or on the

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param tweet_id: The unique identifier referring to a Tweet

    :param as_user_id: The user ID of the advertiser on behalf of whom you are
        posting the Tweet The advertiser must grant your handle (or handles)
        access to their ads account via the Twitter UI at ads.twitter.com. This
        permission allows you to call the API using the OAuth tokens of your
        own handle rather than the advertiser’s.

    :param preview_target: The target to render the Tweet preview for. You can
        preview a Tweet both for how it will look like on Twitter (
        TWITTER_TIMELINES ) or on the Twitter Audience Platform (
        PUBLISHER_NETWORKS ). When using the PUBLISHER_NETWORKS value for the
        preview_target parameter you must not use a Tweet with a card_id and
        the Tweet must specify media_ids. Defaults to TWITTER_TIMELINES.
    """
    binding = {'account_id': account_id, 'tweet_id': tweet_id, 'as_user_id':
               as_user_id, 'preview_target': preview_target}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tweet/preview/{tweet_id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-tweet-preview-tweet-id',
                          binding)


def videos_by_account_id(account_id, *, video_ids=ELIDE, with_deleted=ELIDE,
                         count=ELIDE, cursor=ELIDE):
    """
    Retrieve all video objects associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param video_ids: An optional comma separated list of video IDs to filter
        the response to.

    :param with_deleted: Include deleted results for your request.

    :param count: Specifies the number of videos to try and retrieve, up to a
        maximum of 1,000.

    :param cursor: Specifies a cursor to get the next page of video objects.
        See Pagination for more information.
    """
    binding = {'account_id': account_id, 'video_ids': video_ids,
               'with_deleted': with_deleted, 'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/videos'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-videos',
                          binding)


def videos_by_id_and_account_id(id, account_id, *, with_deleted=ELIDE):
    """
    Retrieve a specific video object belonging to the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The UUID identifier of the video object to be retrieved.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'id': id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/videos/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-videos-id',
                          binding)


def web_event_tags_by_account_id(account_id, *, with_deleted=ELIDE,
                                 count=ELIDE, cursor=ELIDE):
    """
    Retrieve all web event tags associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param with_deleted: Include deleted results for your request. Defaults to
        false.

    :param count: Specifies the number of results to try to return per
        response, up to a maximum of 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.
    """
    binding = {'account_id': account_id, 'with_deleted': with_deleted,
               'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-web-event-tags',
                          binding)


def web_event_tags_by_id_and_account_id(id, account_id, *, with_deleted=ELIDE):
    """
    Retrieve a specific web event tag associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier for the web event tag.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'id': id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags/{id}'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-accounts-account-id-web-event-tags-id',
                          binding)


def reach_estimate_by_account_id(account_id, product_type, objective,
                                 bid_amount_local_micro, currency,
                                 campaign_daily_budget_amount_local_micro, *,
                                 bid_type=ELIDE, followers_of_users=ELIDE,
                                 similar_to_followers_of_users=ELIDE,
                                 locations=ELIDE, interests=ELIDE,
                                 gender=ELIDE, platforms=ELIDE,
                                 tailored_audiences=ELIDE,
                                 tailored_audiences_expanded=ELIDE,
                                 languages=ELIDE, platform_versions=ELIDE,
                                 devices=ELIDE, behaviors=ELIDE,
                                 behaviors_expanded=ELIDE,
                                 campaign_engagement=ELIDE,
                                 user_engagement=ELIDE,
                                 engagement_type=ELIDE,
                                 network_operators=ELIDE,
                                 app_store_categories=ELIDE,
                                 app_store_categories_expanded=ELIDE,
                                 exact_keywords=ELIDE, broad_keywords=ELIDE,
                                 phrase_keywords=ELIDE, age_buckets=ELIDE,
                                 wifi_only=ELIDE):
    """
    Determine the approximate reach of your campaigns.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param product_type: Reach estimates are available for two product types:
        PROMOTED_ACCOUNT or PROMOTED_TWEETS.

    :param objective: The campaign objective for this line item. For details on
        objectives and all possible values, see Objective-based Campaigns.

    :param bid_amount_local_micro: Bid in specified currency micros.

    :param currency: The type of currency for bid_amount_local_micro.
        Identified using ISO-4217. This is a three-letter string such as “USD”
        or “EUR”.

    :param campaign_daily_budget_amount_local_micro: The daily budget for the
        campaign in micros.

    :param bid_type: Sets the bidding mechanism. If set to AUTO,
        bid_amount_local_micro must be NULL. MAX sets the maximum allowable
        bid. AUTO automatically optimizes bidding based on daily budget and
        campaign flight dates. TARGET (available when objective is set to
        WEBSITE_CLICKS, WEBSITE_CONVERSIONS or LEAD_GENERATION) attempts to
        make daily bid averages hit within 20% of the specified
        bid_amount_local_micro

    :param followers_of_users: Include the followers of the specified comma-
        separated list of user_id s in reach estimate. The user must be one of
        the promotable users on the advertiser account. Limit of 100 handles.

    :param similar_to_followers_of_users: Include users that are similar to a
        comma-separated list of user_id. Limit of 100 handles.

    :param locations: A comma-separated string of location identifiers to scope
        targeting to on this line item. Up to 250 locations may be associated
        with a line item.

    :param interests: A comma-separated string of interest identifiers to scope
        targeting to on this line item. Limited to 100 interests.

    :param gender: A comma-separated string of gender identifiers to scope
        targeting to on this line item. Use `` 1 `` to limit to males, or `` 2
        `` to limit to females. Omit for all.

    :param platforms: A comma-separated string of Platform identifiers to scope
        targeting to on this line item.

    :param tailored_audiences: A comma-separated string of tailored audience
        identifiers.

    :param tailored_audiences_expanded: A comma-separated string of tailored
        audience identifiers that should be expanded for look-a-likes.

    :param languages: A comma-separated string of language identifiers.

    :param platform_versions: A comma-separated string of platform version
        identifiers.

    :param devices: A comma-separated string of device identifiers.

    :param behaviors: A comma-separated string of behavior identifiers.

    :param behaviors_expanded: A comma-separated string of behavior
        identifiers. that should be expanded for look-a-likes.

    :param campaign_engagement: The campaign idenifier for use with Tweet
        Engager Retargeting.

    :param user_engagement: The promotable user_id for use with Tweet Engager
        Retargeting.

    :param engagement_type: The engagement type for use with Tweet Engager
        Retargeting. Valid values include IMPRESSION or ENGAGEMENT.

    :param network_operators: A comma-separated string of network operators to
        target.

    :param app_store_categories: A comma-separated string of app store
        categories to target.

    :param app_store_categories_expanded: A comma-separated string of app store
        categories to target with look-a-like expansion.

    :param exact_keywords: A comma-separated string of “exact match” keywords
        to target.

    :param broad_keywords: A comma-separated string of “broad” keywords to
        target.

    :param phrase_keywords: A comma-separated string of “phrase” keywords to
        target.

    :param age_buckets: A comma-separated string of age_buckets to target.

    :param wifi_only: If true, will only target users of mobile devices using
        wifi connections.
    """
    binding = {'account_id': account_id, 'product_type': product_type,
               'objective': objective, 'bid_amount_local_micro':
               bid_amount_local_micro, 'currency': currency,
               'campaign_daily_budget_amount_local_micro':
               campaign_daily_budget_amount_local_micro, 'bid_type': bid_type,
               'followers_of_users': followers_of_users,
               'similar_to_followers_of_users': similar_to_followers_of_users,
               'locations': locations, 'interests': interests, 'gender':
               gender, 'platforms': platforms, 'tailored_audiences':
               tailored_audiences, 'tailored_audiences_expanded':
               tailored_audiences_expanded, 'languages': languages,
               'platform_versions': platform_versions, 'devices': devices,
               'behaviors': behaviors, 'behaviors_expanded':
               behaviors_expanded, 'campaign_engagement': campaign_engagement,
               'user_engagement': user_engagement, 'engagement_type':
               engagement_type, 'network_operators': network_operators,
               'app_store_categories': app_store_categories,
               'app_store_categories_expanded': app_store_categories_expanded,
               'exact_keywords': exact_keywords, 'broad_keywords':
               broad_keywords, 'phrase_keywords': phrase_keywords,
               'age_buckets': age_buckets, 'wifi_only': wifi_only}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/reach_estimate'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-1-accounts-account-id-reach-estimate',
                          binding)


def tailored_audiences_permissions_by_id_and_account_id(id, account_id, *,
                                                        granted_account_ids=ELIDE,
                                                        count=ELIDE,
                                                        cursor=ELIDE,
                                                        with_deleted=ELIDE):
    """
    Displays all current permissions objects associated with a given tailored
    audience.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param granted_account_ids: An optional, comma separated list of account
        IDs to filter the API response to.

    :param count: Specifies the number of records to try and retrieve, up to a
        maximum of 1000 per distinct request.

    :param cursor: Specifies a cursor to get the next page of results. See
        pagination for more information.

    :param with_deleted: Include deleted results in your request. Defaults to
        false.
    """
    binding = {'account_id': account_id, 'granted_account_ids':
               granted_account_ids, 'count': count, 'cursor': cursor,
               'with_deleted': with_deleted, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}/permissions'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'ads:accounts',
                          'get-1-accounts-account-id-tailored-audiences-id-permissions',
                          binding)


def account_media_by_account_id(account_id, media_id, video_id, creative_type):
    """
    Creates a new account media associated to the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param media_id: The identifier of the media uploaded.

    :param video_id: The identifier of the video to be used.

    :param creative_type: The type of creative for this media. See Ads
        Enumerations for more information.
    """
    binding = {'account_id': account_id, 'media_id': media_id, 'video_id':
               video_id, 'creative_type': creative_type}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/account_media'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-account-media',
                          binding)


def app_event_provider_configurations_by_account_id(account_id,
                                                    provider_advertiser_id):
    """
    Create a new application event provider configuration associated with the
    current account. Only one MACT provider can be associated with a particular
    ads account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param provider_advertiser_id: The advertiser’s identifier (string) from
        the provider’s site.
    """
    binding = {'account_id': account_id, 'provider_advertiser_id':
               provider_advertiser_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_event_provider_configurations'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-app-event-provider-configurations',
                          binding)


def app_event_tags_by_account_id(account_id, app_store_identifier, os_type,
                                 conversion_type, provider_app_event_id,
                                 provider_app_event_name, *,
                                 post_engagement_attribution_window=ELIDE,
                                 post_view_attribution_window=ELIDE,
                                 deep_link_scheme=ELIDE,
                                 retargeting_enabled=ELIDE):
    """
    Create a new application event tag associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param app_store_identifier: The app store string identifier such as 12345
        or com.foobar.andriod.prod

    :param os_type: The OS type. Possible values include IOS and ANDRIOD.

    :param conversion_type: The type of conversion event. Possible values are
        PURCHASE, SIGN_UP, INSTALL, RE_ENGAGE, UPDATE, TUTORIAL_COMPLETE,
        RESERVATION, ADD_TO_CART, ADD_TO_WISHLIST, LOGIN, CHECKOUT_INITIATED,
        SEARCH, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, CONTENT_VIEW, SHARE,
        INVITE, ADDED_PAYMENT_INFO, SPENT_CREDITS, RATED.

    :param provider_app_event_id: The ID of the conversion tag on the
        provider’s site.

    :param provider_app_event_name: The name of the conversion tag on the
        provider’s site.

    :param post_engagement_attribution_window: The post-engagement attribution
        window for these events. Possible values are 1, 7, 14 or 30.

    :param post_view_attribution_window: The post-view attribution window for
        these events. Possible values are 0, 1, 7, 14 or 30.

    :param deep_link_scheme: String. Specify the deep link URI for the app
        associated to this tag.

    :param retargeting_enabled: Boolean indicating if retargeting should be
        enabled for this app event tag. Possible values are true, 1, false, 0.
    """
    binding = {'account_id': account_id, 'app_store_identifier':
               app_store_identifier, 'os_type': os_type, 'conversion_type':
               conversion_type, 'provider_app_event_id':
               provider_app_event_id, 'provider_app_event_name':
               provider_app_event_name, 'post_engagement_attribution_window':
               post_engagement_attribution_window,
               'post_view_attribution_window': post_view_attribution_window,
               'deep_link_scheme': deep_link_scheme, 'retargeting_enabled':
               retargeting_enabled}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-app-event-tags',
                          binding)


def app_lists_by_account_id(account_id, name, app_store_identifiers):
    """
    Create an

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name you will assign to the app_list.

    :param app_store_identifiers: The app_store_identifier``s to include in
        this ``app_list.
    """
    binding = {'account_id': account_id, 'name': name,
               'app_store_identifiers': app_store_identifiers}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_lists'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-app-lists',
                          binding)


def campaigns_by_account_id(account_id, name, funding_instrument_id,
                            start_time, daily_budget_amount_local_micro, *,
                            end_time=ELIDE, paused=ELIDE,
                            standard_delivery=ELIDE, frequency_cap=ELIDE,
                            duration_in_days=ELIDE,
                            total_budget_amount_local_micro=ELIDE):
    """
    Create a new campaign associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name you will assign to the campaign.

    :param funding_instrument_id: The identifier for a funding instrument to be
        associated with this campaign.

    :param start_time: The UTC time that the campaign will begin. Must be more
        recent than the current time. Expressed in ISO 8601.

    :param end_time: The UTC time that the campaign will end. If specified,
        must be more recent than the campaign’s start_time. Expressed in ISO
        8601.

    :param paused: A boolean indicating whether this campaign is currently
        paused (AKA “inactive”). Defaults to false.

    :param standard_delivery: A boolean indicating whether this campaign should
        use standard delivery rather than accelerated delivery.
        standard_delivery defaults to true. See Budget Pacing for more
        information on standard versus accelerated delivery.

    :param frequency_cap: An integer representing the number of times for which
        one user could be delivered an ad to.

    :param duration_in_days: An integer representing the time period within
        which the frequency_cap frequency is achieved. Only supports values of:
        1, 7 and 30.

    :param total_budget_amount_local_micro: An integer representing the total
        budget amount to be allocated to the campaign. The currency associated
        with the specified funding instrument will be used. For USD, $37.50 is
        encoded as 37.50*1e6, or 37,500,000.

    :param daily_budget_amount_local_micro: An integer representing the daily
        budget amount to be allocated to the campaign. This amount should be
        less than or equal to the total_budget_amount_local_micro. The currency
        associated with the specified funding instrument will be used. For USD,
        $5.50 is encoded as 5.50*1e6, or 5,500,000.
    """
    binding = {'account_id': account_id, 'name': name,
               'funding_instrument_id': funding_instrument_id, 'start_time':
               start_time, 'end_time': end_time, 'paused': paused,
               'standard_delivery': standard_delivery, 'frequency_cap':
               frequency_cap, 'duration_in_days': duration_in_days,
               'total_budget_amount_local_micro':
               total_budget_amount_local_micro,
               'daily_budget_amount_local_micro':
               daily_budget_amount_local_micro}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/campaigns'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-campaigns',
                          binding)


def cards_app_download_by_account_id(account_id, name, app_country_code, *,
                                     iphone_app_id=ELIDE, ipad_app_id=ELIDE,
                                     googleplay_app_id=ELIDE, app_cta=ELIDE,
                                     iphone_deep_link=ELIDE,
                                     ipad_deep_link=ELIDE,
                                     googleplay_deep_link=ELIDE,
                                     custom_icon_media_id=ELIDE,
                                     custom_app_description=ELIDE):
    """
    Creates a new app download card associated to a given account. This card is
    part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name identifier for card. Maximum length: 80 characters.

    :param app_country_code: 2 letter ISO code for the country where the App is
        sold.

    :param iphone_app_id: This is usually numeric and available in your App
        Store URL. For example, 333903271 is the id for Twitter. You can
        retrieve the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPHONE_APP_ID>

    :param ipad_app_id: This is usually numeric and available in your App Store
        URL. For example, 333903271 is the id for Twitter. You can retrieve the
        id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPAD_APP_ID>

    :param googleplay_app_id: This ID is Google Play’s application package
        name. For example, Twitter’s Google Play app id is com.twitter.android.

    :param app_cta: The Call-to-Action (CTA) text for the card button. See our
        enums for possible values.

    :param iphone_deep_link: This is your app’s deep link.

    :param ipad_deep_link: This is your app’s deep link.

    :param googleplay_deep_link: This is your app’s deep link.

    :param custom_icon_media_id: A media_id of a custom image which will be
        used instead of the app store’s icon. This is a write-only field. In
        response, the API will provide a Twitter URL for this image, that can
        be reused. This needs to be minimum of 144px wide/height with the
        aspect ratio 1:1.

    :param custom_app_description: This is a custom description of the app. If
        supplied, it will be used instead of the description from the app
        store.
    """
    binding = {'account_id': account_id, 'name': name, 'app_country_code':
               app_country_code, 'iphone_app_id': iphone_app_id,
               'ipad_app_id': ipad_app_id, 'googleplay_app_id':
               googleplay_app_id, 'app_cta': app_cta, 'iphone_deep_link':
               iphone_deep_link, 'ipad_deep_link': ipad_deep_link,
               'googleplay_deep_link': googleplay_deep_link,
               'custom_icon_media_id': custom_icon_media_id,
               'custom_app_description': custom_app_description}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-cards-app-download',
                          binding)


def cards_image_app_download_by_account_id(account_id, name,
                                           app_country_code,
                                           wide_app_image_media_id, *,
                                           iphone_app_id=ELIDE,
                                           ipad_app_id=ELIDE,
                                           googleplay_app_id=ELIDE,
                                           app_cta=ELIDE,
                                           iphone_deep_link=ELIDE,
                                           ipad_deep_link=ELIDE,
                                           googleplay_deep_link=ELIDE):
    """
    Creates a new image app download card associated to a given account. This
    card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name identifier for card. Maximum length: 80 characters.

    :param app_country_code: 2 letter ISO code for the country where the App is
        sold.

    :param iphone_app_id: This is usually numeric and available in your App
        Store URL. For example, 333903271 is the id for Twitter. You can
        retrieve the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPHONE_APP_ID>

    :param ipad_app_id: This is usually numeric and available in your App Store
        URL. For example, 333903271 is the id for Twitter. You can retrieve the
        id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPAD_APP_ID>

    :param googleplay_app_id: This ID is Google Play’s application package
        name. For example, Twitter’s Google Play app id is com.twitter.android.

    :param app_cta: The Call-to-Action (CTA) text for the card button. See our
        enums for possible values.

    :param iphone_deep_link: This is your app’s deep link.

    :param ipad_deep_link: This is your app’s deep link.

    :param googleplay_deep_link: This is your app’s deep link.

    :param wide_app_image_media_id: A media_id of an image which will be used
        instead of the app store’s icon. This is a write-only field. In
        response, the API will provide a Twitter URL for this image, that can
        be reused. Minimum width of 800px, maximum size of 1MB and width:height
        with the aspect ratio 5:2.
    """
    binding = {'account_id': account_id, 'name': name, 'app_country_code':
               app_country_code, 'iphone_app_id': iphone_app_id,
               'ipad_app_id': ipad_app_id, 'googleplay_app_id':
               googleplay_app_id, 'app_cta': app_cta, 'iphone_deep_link':
               iphone_deep_link, 'ipad_deep_link': ipad_deep_link,
               'googleplay_deep_link': googleplay_deep_link,
               'wide_app_image_media_id': wide_app_image_media_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-cards-image-app-download',
                          binding)


def cards_image_conversation_by_account_id(account_id, name, title,
                                           first_cta, first_cta_tweet,
                                           thank_you_text, image_media_id, *,
                                           second_cta=ELIDE,
                                           second_cta_tweet=ELIDE,
                                           third_cta=ELIDE,
                                           third_cta_tweet=ELIDE,
                                           fourth_cta=ELIDE,
                                           fourth_cta_tweet=ELIDE,
                                           thank_you_url=ELIDE,
                                           cover_image_id=ELIDE):
    """
    Creates a new image conversation card associated to a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name identifier for card (not user-facing). Maximum
        length: 80 characters.

    :param title: The title text for the card, used when only first CTA is
        specified. Maximum length: 23 characters.

    :param first_cta: The call-to-action hashtag for the first option. Maximum
        length: 20 characters (not counting the # character).

    :param first_cta_tweet: The Tweet text to be used when the first call-to-
        action is clicked. Maximum length: 116 characters.

    :param second_cta: The call-to-action text for the second option. Maximum
        length: 20 characters. (not counting the # character).

    :param second_cta_tweet: The Tweet text to be used when the second call-to-
        action is clicked. Maximum length: 116 characters.

    :param third_cta: The call-to-action text for the third option. Maximum
        length: 20 characters. (not counting the # character).

    :param third_cta_tweet: The Tweet text to be used when the third call-to-
        action is clicked. Maximum length: 116 characters.

    :param fourth_cta: The call-to-action text for the fourth option. Maximum
        length: 20 characters. (not counting the # character).

    :param fourth_cta_tweet: The Tweet text to be used when the fourth call-to-
        action is clicked. Maximum length: 116 characters.

    :param thank_you_text: The text to be displayed after the call-to-action is
        clicked.

    :param thank_you_url: The URL to be displayed with the thank you text.

    :param image_media_id: A media_id of an image which will be used in this
        card. This is a write-only field. In response, the API will provide a
        Twitter URL for this image, that can be reused. Minimum width of 800px,
        maximum size of 1MB and width:height with the aspect ratio 5:2.

    :param cover_image_id: A media_id of an image which will be used in the
        instant unlock scenario. This is a write-only field. In response, the
        API will provide a Twitter URL for this image, that can be reused.
    """
    binding = {'account_id': account_id, 'name': name, 'title': title,
               'first_cta': first_cta, 'first_cta_tweet': first_cta_tweet,
               'second_cta': second_cta, 'second_cta_tweet': second_cta_tweet,
               'third_cta': third_cta, 'third_cta_tweet': third_cta_tweet,
               'fourth_cta': fourth_cta, 'fourth_cta_tweet': fourth_cta_tweet,
               'thank_you_text': thank_you_text, 'thank_you_url':
               thank_you_url, 'image_media_id': image_media_id,
               'cover_image_id': cover_image_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-cards-image-conversation',
                          binding)


def cards_video_app_download_by_account_id(account_id, name,
                                           app_country_code, video_id, *,
                                           iphone_app_id=ELIDE,
                                           ipad_app_id=ELIDE,
                                           googleplay_app_id=ELIDE,
                                           app_cta=ELIDE,
                                           iphone_deep_link=ELIDE,
                                           ipad_deep_link=ELIDE,
                                           googleplay_deep_link=ELIDE,
                                           image_media_id=ELIDE):
    """
    Creates a new Video App Download Card associated to the specified account.
    This card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name identifier for card. Maximum length: 80 characters.

    :param app_country_code: 2 letter ISO code for the country where the App is
        sold.

    :param iphone_app_id: This is usually numeric and available in your App
        Store URL. For example, 333903271 is the id for Twitter. You can
        retrieve the id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPHONE_APP_ID>

    :param ipad_app_id: This is usually numeric and available in your App Store
        URL. For example, 333903271 is the id for Twitter. You can retrieve the
        id from Apple App Store URL -
        https://itunes.apple.com/us/app/twitter/id<IPAD_APP_ID>

    :param googleplay_app_id: This ID is Google Play’s application package
        name. For example, Twitter’s Google Play app id is com.twitter.android.

    :param app_cta: The Call-to-Action (CTA) text for the card button. See our
        enums for possible values.

    :param iphone_deep_link: This is your app’s deep link.

    :param ipad_deep_link: This is your app’s deep link.

    :param googleplay_deep_link: This is your app’s deep link.

    :param image_media_id: The media_id for the uploaded video poster image.
        There are no size or aspect ratio restrictions on this image, it will
        simply be converted to fit the dimensions of the player.

    :param video_id: The UUID of the uploaded video from GET
        accounts/:account_id/videos endpoint to be included in the card.
    """
    binding = {'account_id': account_id, 'name': name, 'app_country_code':
               app_country_code, 'iphone_app_id': iphone_app_id,
               'ipad_app_id': ipad_app_id, 'googleplay_app_id':
               googleplay_app_id, 'app_cta': app_cta, 'iphone_deep_link':
               iphone_deep_link, 'ipad_deep_link': ipad_deep_link,
               'googleplay_deep_link': googleplay_deep_link, 'image_media_id':
               image_media_id, 'video_id': video_id}
    url = 'POST'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-cards-video-app-download',
                          binding)


def cards_video_conversation_by_account_id(account_id, name, title,
                                           first_cta, first_cta_tweet,
                                           thank_you_text, image_media_id,
                                           video_id, *, second_cta=ELIDE,
                                           second_cta_tweet=ELIDE,
                                           third_cta=ELIDE,
                                           third_cta_tweet=ELIDE,
                                           fourth_cta=ELIDE,
                                           fourth_cta_tweet=ELIDE,
                                           thank_you_url=ELIDE,
                                           cover_video_id=ELIDE):
    """
    Creates a new video conversation card associated to a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name identifier for card (not user-facing). Maximum
        length: 80 characters.

    :param title: The title text for the card, used when only first CTA is
        specified. Maximum length: 23 characters.

    :param first_cta: The call-to-action hashtag for the first option. Maximum
        length: 20 characters (not counting the # character).

    :param first_cta_tweet: The Tweet text to be used when the first call-to-
        action is clicked. Maximum length: 116 characters.

    :param second_cta: The call-to-action text for the second option. Maximum
        length: 20 characters. (not counting the # character).

    :param second_cta_tweet: The Tweet text to be used when the second call-to-
        action is clicked. Maximum length: 116 characters.

    :param third_cta: The call-to-action text for the third option. Maximum
        length: 20 characters. (not counting the # character).

    :param third_cta_tweet: The Tweet text to be used when the third call-to-
        action is clicked. Maximum length: 116 characters.

    :param fourth_cta: The call-to-action text for the fourth option. Maximum
        length: 20 characters. (not counting the # character).

    :param fourth_cta_tweet: The Tweet text to be used when the fourth call-to-
        action is clicked. Maximum length: 116 characters.

    :param thank_you_text: The text to be displayed after the call-to-action is
        clicked.

    :param thank_you_url: The URL to be displayed with the thank you text.

    :param image_media_id: A media_id of an image which will be used as the
        poster image in this card. This is a write-only field. In response, the
        API will provide a Twitter URL for this image, that can be reused.
        Minimum width of 800px, maximum size of 1MB and width:height with the
        aspect ratio 5:2.

    :param video_id: A media_id of a video which will be used in this card.
        This is a write-only field.

    :param cover_video_id: A media_id of a video which will be used in the
        instant unlock scenario. This is a write-only field. In response, the
        API will provide a Twitter URL for this image, that can be reused.
    """
    binding = {'account_id': account_id, 'name': name, 'title': title,
               'first_cta': first_cta, 'first_cta_tweet': first_cta_tweet,
               'second_cta': second_cta, 'second_cta_tweet': second_cta_tweet,
               'third_cta': third_cta, 'third_cta_tweet': third_cta_tweet,
               'fourth_cta': fourth_cta, 'fourth_cta_tweet': fourth_cta_tweet,
               'thank_you_text': thank_you_text, 'thank_you_url':
               thank_you_url, 'image_media_id': image_media_id, 'video_id':
               video_id, 'cover_video_id': cover_video_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-cards-video-conversation',
                          binding)


def cards_website_by_account_id(account_id, name, website_title, website_url,
                                image_media_id):
    """
    Creates a new website card associated to a given account. Our advertiser
    help center has

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name identifier for card. Maximum length: 80 characters.

    :param website_title: The title of the website card. Maximum length: 70
        characters.

    :param website_url: The URL of the website to redirect a user to. Maximum
        length: 200 characters.

    :param image_media_id: A media_id of an image which will be used in this
        card. This is a write-only field. In response, the API will provide a
        Twitter URL for this image, that can be reused. The image must have: a
        minimum width of 800px, a maximum size of 1 MB, and a width:height
        aspect ratio of either 5:2 or 1.91:1.
    """
    binding = {'account_id': account_id, 'name': name, 'website_title':
               website_title, 'website_url': website_url, 'image_media_id':
               image_media_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/website'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-cards-website',
                          binding)


def line_item_apps_by_account_id(account_id, line_item_id,
                                 app_store_identifier, os_type):
    """
    Create an association between a mobile app and a line item to enable mobile
    app promotion on the Twitter Audience Platform.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_id: The line item to associate the app to.

    :param app_store_identifier: The app store string identifier, such as ``
        12345 `` or com.foobar.android.prod

    :param os_type: The OS type. Possible values include IOS and ANDRIOD.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'app_store_identifier': app_store_identifier, 'os_type':
               os_type}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-line-item-apps',
                          binding)


def line_items_by_account_id(account_id, campaign_id, product_type,
                             placements, objective, *,
                             bid_amount_local_micro=ELIDE, name=ELIDE,
                             bid_type=ELIDE, automatically_select_bid=ELIDE,
                             paused=ELIDE, include_sentiment=ELIDE,
                             total_budget_amount_local_micro=ELIDE,
                             start_time=ELIDE, end_time=ELIDE,
                             primary_web_event_tag=ELIDE, optimization=ELIDE,
                             bid_unit=ELIDE, charge_by=ELIDE,
                             advertiser_domain=ELIDE, categories=ELIDE,
                             tracking_tags=ELIDE, advertiser_user_id=ELIDE,
                             target_cpa_local_micro=ELIDE):
    """
    Create a line item associated with the specified campaign belonging to the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param campaign_id: The identifier for a campaign associated with the
        current account.

    :param bid_amount_local_micro: Required if bid_type is set to either MAX or
        TARGET or if automatically_set_bid is false. An integer representing
        the bid amount to be associated with this line item. The currency
        associated with the specified funding instrument will be used. For USD,
        $1.50 is encoded as 1.50*1e6, or 1,500,000. This value cannot be set to
        0 and only positive integers are accepted.

    :param name: A name assigned to the line item. If left blank, the name will
        default to ‘Untitled.’

    :param bid_type: Sets the bidding mechanism. If set to AUTO,
        bid_amount_local_micro is not required and should not be set. Cannot be
        set in the same request as automatically_set_bid.

    :param automatically_select_bid: This boolean parameter when set to true
        will automatically optimize bidding based on daily budget and campaign
        flight dates. If set to true, bid_amount_local_micro is not required
        and should not be set, and bid_type will be set to AUTO. Cannot be set
        in the same request as bid_type.

    :param product_type: The type of promoted product that this line item will
        contain. See our enums for possible values.

    :param placements: The comma-separated list of placement locations for this
        line item to display in. See our enums for possible values.

    :param objective: The campaign objective for this line item. For details on
        objectives and all possible values, see Objective-based Campaigns.

    :param paused: A boolean indicating whether this line item is currently
        paused (AKA “inactive”).

    :param include_sentiment: Allows the line item to be targeted to Tweets
        with both positive or negative sentiment. A tweet is said to have
        positive or negative sentiment if the tone of the Tweet is positive (“I
        love it! #newcamero”) or negative (“I hate it! #newcamero”). Note, only
        valid for product_type of PROMOTED_TWEETS and with either placements of
        ALL_ON_TWITTER or TWITTER_TIMELINES. Available options: POSITIVE_ONLY
        (default) targets only Tweets with positive sentiment, ALL targets all
        Tweets, including those with negative sentiment.

    :param total_budget_amount_local_micro: An integer representing the total
        budget amount to be allocated to the line item. The currency associated
        with the specified funding instrument and campaign will be used. For
        USD, $37.50 is encoded as 37.50*1e6, or 37,500,000.

    :param start_time: The UTC time that the line item will begin serving. Must
        be more recent than the current time. Expressed in ISO 8601.

    :param end_time: The UTC time that the line item will stop serving. If
        specified, must be more recent than the line item’s start_time.
        Expressed in ISO 8601.

    :param primary_web_event_tag: The identifier of the primary web event tag.
        Allows more accurate tracking of engagements for the campaign
        pertaining to this line item. See GET
        accounts/:account_id/web_event_tags. Must be specified when objective
        is set to WEBSITE_CONVERSIONS.

    :param optimization: The optimization setting to use on this ad group (line
        item). For possible values, see our enumerations page.

    :param bid_unit: This setting is available for line items using the
        APP_INSTALLS or VIDEO_VIEWS objectives. See Objective-based Campaigns.
        Defaults to bid unit based on objective. For possible values, see Ads
        Enumerations.

    :param charge_by: This setting is available for line items using the
        APP_INSTALLS objective. See Objective-based Campaigns. Defaults to
        charging by bid unit except for line items with bid unit APP_INSTALLS,
        where it defaults to charging by app-clicks. For all possible values,
        see Ads Enumerations.

    :param advertiser_domain: The website domain for this advertiser, without
        protocol specification. This setting is available for line items using
        the Twitter Audience Platform (TAP).

    :param categories: The relevant IAB categories for this advertiser. This
        setting is available for line items using the Twitter Audience Platform
        (TAP). For possible values, see GET /1/iab_categories.

    :param tracking_tags: The tracking partner enum and the tracking tag url
        provided by the tracking partner, separated by a dash. For possible
        tracking partner enums, see Ads Enumerations.

    :param advertiser_user_id: The Twitter user identifier for the handle
        promoting a VIDEO_VIEWS_PREROLL ad. Use of this parameter is restricted
        to whitelisted developers only.

    :param target_cpa_local_micro: An integer representing the target CPA
        amount to be allocated to the line item. The currency associated with
        the specified funding instrument and campaign will be used. For USD,
        $5.50 is encoded as 5.50*1e6, or 5,500,000. Must be specified when
        objective is set to WEBSITE_CONVERSIONS.
    """
    binding = {'account_id': account_id, 'campaign_id': campaign_id,
               'bid_amount_local_micro': bid_amount_local_micro, 'name': name,
               'bid_type': bid_type, 'automatically_select_bid':
               automatically_select_bid, 'product_type': product_type,
               'placements': placements, 'objective': objective, 'paused':
               paused, 'include_sentiment': include_sentiment,
               'total_budget_amount_local_micro':
               total_budget_amount_local_micro, 'start_time': start_time,
               'end_time': end_time, 'primary_web_event_tag':
               primary_web_event_tag, 'optimization': optimization,
               'bid_unit': bid_unit, 'charge_by': charge_by,
               'advertiser_domain': advertiser_domain, 'categories':
               categories, 'tracking_tags': tracking_tags,
               'advertiser_user_id': advertiser_user_id,
               'target_cpa_local_micro': target_cpa_local_micro}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_items'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-line-items',
                          binding)


def media_creatives_by_account_id(account_id, line_item_id, account_media_id,
                                  *, landing_url=ELIDE):
    """
    Creates a new media creative associated to the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_id: A reference to the line item you are operating with in
        the request.

    :param account_media_id: The identifier of the account media for this
        account.

    :param landing_url: URL for the media creative.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'account_media_id': account_media_id, 'landing_url':
               landing_url}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-media-creatives',
                          binding)


def preroll_call_to_actions_by_account_id(account_id, line_item_id,
                                          call_to_action, call_to_action_url):
    """
    Set the optional Call-to-Action (CTA) for a

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_id: The line item to associate this CTA to.

    :param call_to_action: The Call-to-Action (CTA) text for the displayed
        button. Possible values are available on the enums page.

    :param call_to_action_url: The URL to redirect the user to when they click
        on the CTA button.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'call_to_action': call_to_action, 'call_to_action_url':
               call_to_action_url}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-preroll-call-to-actions',
                          binding)


def promoted__by_account_id(account_id, line_item_id, user_id):
    """
    Associate a Promoted Account to the specified line item.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_id: A reference to the line item you are operating with in
        the request.

    :param user_id: A reference to a Twitter User Account by user ID. Use GET
        users/lookup to retrieve a user_id for a screen_name.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'user_id': user_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/promoted_accounts'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-promoted-accounts',
                          binding)


def promoted_tweets_by_account_id(account_id, line_item_id, tweet_ids):
    """
    Associate one or more Promoted Tweets to the specified line item. Not all
    Tweets are appropriate for Tweet promotion, depending on the campaign
    objective. Please see

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_id: A reference to the line item you are operating with in
        the request.

    :param tweet_ids: A comma-separated list of identifiers corresponding to
        specific Tweets. Up to 50 ids may be provided.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'tweet_ids': tweet_ids}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/promoted_tweets'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-promoted-tweets',
                          binding)


def tailored_audience_changes_by_account_id(account_id, tailored_audience_id,
                                            input_file_path, operation):
    """
    Submit a change to a tailored audience.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param tailored_audience_id: The identifier for the tailored audience.
        Type: string Example: c3po

    :param input_file_path: The file path returned by the TON API endpoint.
        Type: string Example: /1.1/ton/data/ta_partner/1877861928/Axbsh2.csv

    :param operation: The operation to take on this audience with the uploaded
        list. Type: enum Possible values: ADD, REMOVE, REPLACE
    """
    binding = {'account_id': account_id, 'tailored_audience_id':
               tailored_audience_id, 'input_file_path': input_file_path,
               'operation': operation}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audience_changes'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-tailored-audience-changes',
                          binding)


def tailored_audiences_by_account_id(account_id, name, list_type):
    """
    Create a new tailored audience to which many files can be uploaded.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The display name for this audience.

    :param list_type: The type of list for this audience. Possible values
        include EMAIL, DEVICE_ID, TWITTER_ID, HANDLE, PHONE_NUMBER.
    """
    binding = {'account_id': account_id, 'name': name, 'list_type': list_type}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-tailored-audiences',
                          binding)


def targeting_criteria_by_account_id(account_id, line_item_id,
                                     targeting_type, targeting_value, *,
                                     tailored_audience_expansion=ELIDE,
                                     tailored_audience_type=ELIDE):
    """
    Use the following endpoints to locate the correct

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param line_item_id: A reference to the line item you are operating with in
        the request.

    :param targeting_type: The type of targeting that will be applied to this
        line item. Possible non-keyword-based values include: AGE,
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
        app blacklisting values: EXCLUDE_APP_LIST.

    :param targeting_value: Specify which user, which interest, which location,
        which event, which platform, which platform version, which device,
        which keyword or phrase, which gender, which tailored audience, which
        behavior, which app store category, or which exclusion of an app list
        this targeting will be applied to, depending on the selected
        targeting_type.

    :param tailored_audience_expansion: A boolean value for expansion. Only
        available for Tailored Audience CRM.

    :param tailored_audience_type: A value for the tailored audience type:
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'targeting_type': targeting_type, 'targeting_value':
               targeting_value, 'tailored_audience_expansion':
               tailored_audience_expansion, 'tailored_audience_type':
               tailored_audience_type}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-targeting-criteria',
                          binding)


def tweet_by_account_id(account_id, status, *, as_user_id=ELIDE,
                        trim_user=ELIDE, media_ids=ELIDE, video_id=ELIDE,
                        video_title=ELIDE, video_description=ELIDE,
                        video_cta=ELIDE, video_cta_value=ELIDE,
                        tweet_mode=ELIDE):
    """
    Create “Promoted-Only” Tweets. The Tweets posted via this endpoint can be
    used in Promoted Tweets campaigns but will not appear on the public
    timeline and are not served to followers.

    :param status: The text of your status update, typically up to 140
        characters. URL encode as necessary. t.co link wrapping may affect
        character counts.

    :param as_user_id: The user ID of the advertiser on behalf of whom you are
        posting the Tweet The advertiser must grant your handle (or handles)
        access to their ads account via the Twitter UI at ads.twitter.com. This
        permission allows you to call the API using the OAuth tokens of your
        own handle rather than the advertiser’s.

    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param media_ids: A list of media ids to associate with the Tweet. You may
        associated up to 4 media to a Tweet. See Uploading Media for further
        details on uploading media.

    :param video_id: The Video UUID to be associated with thie Tweet. Please
        see GET /videos for a list of eligible video UUIDs.

    :param video_title: An optional title to be included with the video. This
        value has a max length of 160.

    :param video_description: An optional description to be included with the
        video. This value has a max length of 160.

    :param video_cta: An optional CTA value for the associated video. Please
        see the Enum page for a list of possible values.

    :param video_cta_value: The value for the corresponding CTA on the
        associated video. This value is required if you’ve specified a
        video_cta and must be a valid URL.

    :param tweet_mode: Value for the type of tweet being created. See Enums for
        more information.
    """
    binding = {'status': status, 'as_user_id': as_user_id, 'trim_user':
               trim_user, 'media_ids': media_ids, 'video_id': video_id,
               'video_title': video_title, 'video_description':
               video_description, 'video_cta': video_cta, 'video_cta_value':
               video_cta_value, 'tweet_mode': tweet_mode, 'account_id':
               account_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tweet'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-tweet',
                          binding)


def videos_by_account_id(account_id, video_media_id, *,
                         poster_image_media_id=ELIDE, title=ELIDE,
                         description=ELIDE):
    """
    Associate a video with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all Ads
        API requests excluding GET accounts. The specified account must be
        associated with the authenticating user.

    :param video_media_id: The media_id for the uploaded video content. Please
        see POST media/upload (chunked) for more information about uploading
        videos.

    :param poster_image_media_id: Specify a poster image for the video using
        the media_id of an uploaded image. If not specified, the first frame
        will be used. Only the owner of the video—that is, the authenticated
        user at the time of upload—can set the poster image. Poster image
        dimensions should match the video dimensions. This is a write-only
        field. In response, the API will provide a Twitter URL for this image,
        which can be reused.

    :param title: A string value to populate the video title with. This value
        is not user-facing and is only utilized for identification purposes in
        the GET accounts/:account_id/videos endpoint and the Twitter Ads UI
        video library.

    :param description: A string value to populate the video description with.
        This value is not user-facing and is only utilized for identification
        purposes in the GET accounts/:account_id/videos endpoint and the
        Twitter Ads UI video library.
    """
    binding = {'account_id': account_id, 'video_media_id': video_media_id,
               'poster_image_media_id': poster_image_media_id, 'title': title,
               'description': description}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/videos'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-videos',
                          binding)


def web_event_tags_by_account_id(account_id, name, click_window,
                                 view_through_window, type,
                                 retargeting_enabled):
    """
    Create a new web event tag associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param name: The name of the web tag.

    :param click_window: The click window for this web tag. Possible values are
        1, 7, 14, 30, 60 or 90.

    :param view_through_window: The view through window for this web tag. This
        value must always be less than or equal to the click_window value.
        Possible values are 0, 1, 7, 14, 30, 60 or 90.

    :param type: The type of web tag. Possible values are SITE_VISIT, PURCHASE,
        DOWNLOAD, SIGN_UP, CUSTOM.

    :param retargeting_enabled: Boolean indicating if retargeting should be
        enabled for this web tag. Possible values are true, 1, false, 0.
    """
    binding = {'account_id': account_id, 'name': name, 'click_window':
               click_window, 'view_through_window': view_through_window,
               'type': type, 'retargeting_enabled': retargeting_enabled}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-accounts-account-id-web-event-tags',
                          binding)


def accounts():
    """

    """
    binding = {}
    url = 'https://ads-api-sandbox.twitter.com/1/accounts/'
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-1-accounts',
                          binding)


def features__by_account_id(account_id, type):
    """


    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param type: A comma separated list of account features to be added to the
        account.
    """
    binding = {'account_id': account_id, 'type': type}
    url = 'https://ads-api-sandbox.twitter.com/1/accounts/{account_id}/features'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-1-accounts-account-id-features',
                          binding)


def funding_instruments_by_account_id(account_id, type, currency, start_time,
                                      *, funded_amount_local_micro=ELIDE,
                                      credit_limit_local_micro=ELIDE,
                                      end_time=ELIDE):
    """


    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param type: The type of funding instrument to create as one of:
        INSERTION_ORDER, CREDIT_LINE, AGENCY_CREDIT_LINE, PARTNER_MANAGED,
        CREDIT_CARD.

    :param currency: The type of currency to assign to funding instrument,
        identified using ISO-4217. This is a three-letter string like “USD” or
        “EUR”. Omit this parameter to retrieve all bidding rules.

    :param funded_amount_local_micro: (Only applicable to some funding
        instrument types) Integer representing the total budget amount
        allocated in local micro.

    :param credit_limit_local_micro: (Only applicable to some funding
        instrument types) Integer representing the total credit available
        against this funding instrument.

    :param start_time: The date for the funding instrument to become active and
        usable. Expressed in ISO_8601.

    :param end_time: The date for funding instrument to become inactive.
        Expressed in ISO_8601.
    """
    binding = {'account_id': account_id, 'type': type, 'currency': currency,
               'funded_amount_local_micro': funded_amount_local_micro,
               'credit_limit_local_micro': credit_limit_local_micro,
               'start_time': start_time, 'end_time': end_time}
    url = 'https://ads-api-sandbox.twitter.com/1/accounts/{account_id}/funding_instruments'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-1-accounts-account-id-funding-instruments',
                          binding)


def tailored_audiences_permissions_by_id_and_account_id(id, account_id,
                                                        granted_account_id,
                                                        permission_level):
    """
    Creates a new permission object allowing this specific audience to be
    shared with a given account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param granted_account_id: The advertiser account ID you wish to set
        permissions for on this tailored audiences.

    :param permission_level: The permission level you want to grant for this
        account and tailored audience. Valid values here are READ_ONLY and
        READ_WRITE.
    """
    binding = {'account_id': account_id, 'granted_account_id':
               granted_account_id, 'permission_level': permission_level, 'id':
               id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}/permissions'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'ads:accounts',
                          'post-1-accounts-account-id-tailored-audiences-id-permissions',
                          binding)


def app_event_provider_configurations_by_id_and_account_id(id, account_id):
    """
    Disassociate a specific application event provider configuration associated
    with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param id: The identifier for the application event provider.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_event_provider_configurations/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-app-event-provider-configurations-id',
                          binding)


def app_event_tags_by_id_and_account_id(id, account_id):
    """
    Disassociate a specific application event tag associated from the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param id: The identifier for the application event tag.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/app_event_tags/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-app-event-tags-id',
                          binding)


def campaigns_by_campaign_id_and_account_id(campaign_id, account_id):
    """
    Delete an existing campaign associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param campaign_id: The identifier for a campaign associated with the
        current account.
    """
    binding = {'account_id': account_id, 'campaign_id': campaign_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/campaigns/{campaign_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-campaigns-campaign-id',
                          binding)


def cards_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given app download card. This card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/app_download/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-cards-app-download-card-id',
                          binding)


def cards_image_app_download_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given image app download card. This card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_app_download/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-cards-image-app-download-card-id',
                          binding)


def cards_image_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given image conversation card.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/image_conversation/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-cards-image-conversation-card-id',
                          binding)


def cards_video_app_download_by_id_and_account_id(id, account_id, card_id):
    """
    Delete a given Video App Download Card. This card is part of our

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id, 'id': id}
    url = 'DELETE accounts/{account_id}/cards/video_app_download/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-cards-video-app-download-id',
                          binding)


def cards_video_conversation_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given video conversation card.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/cards/video_conversation/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-cards-video-conversation-card-id',
                          binding)


def cards_website_by_card_id_and_account_id(card_id, account_id):
    """
    Delete a given website card.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param card_id: The identifier for the specific card.
    """
    binding = {'account_id': account_id, 'card_id': card_id}
    url = 'DELETE accounts/{account_id}/cards/website/{card_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-cards-website-card-id',
                          binding)


def line_item_apps_by_line_item_app_id_and_account_id(line_item_app_id,
                                                      account_id):
    """
    Delete a specific line item to mobile app association.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_app_id: The identifier for a line item app associated with
        the current account.
    """
    binding = {'account_id': account_id, 'line_item_app_id': line_item_app_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_item_apps/{line_item_app_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-line-item-apps-line-item-app-id',
                          binding)


def line_items_by_line_item_id_and_account_id(line_item_id, account_id):
    """
    Delete the specified line item belonging to the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param line_item_id: A reference to the line item you are operating with in
        the request.
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/line_items/{line_item_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-line-items-line-item-id',
                          binding)


def media_creatives_by_id_and_account_id(id, account_id):
    """
    Removes a media creative for the current ads account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user.

    :param id: The identifier for the media id associated with the current
        account.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/media_creatives/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-media-creatives-id',
                          binding)


def preroll_call_to_actions_by_preroll_call_to_action_id_and_account_id(preroll_call_to_action_id,
                                                                        account_id):
    """
    Deletes a Call-to-Action (CTAs) associated with a line item on this
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param preroll_call_to_action_id: A reference to the prerol call to action
        you are operating with in the request.
    """
    binding = {'account_id': account_id, 'preroll_call_to_action_id':
               preroll_call_to_action_id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/preroll_call_to_actions/{preroll_call_to_action_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-preroll-call-to-actions-preroll-call-to-action-id',
                          binding)


def promoted_tweets_by_id_and_account_id(id, account_id):
    """
    Disassociate a Promoted Tweet from a line item by specifying its instance

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param id: This identifier refers to the instance of a Promoted Tweet
        associated with a line item. This comes from the id field from a
        response item to GET accounts/:account_id/promoted_tweets, not the
        tweet_id of the Tweet in question. Supplied within the resource’s path.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/promoted_tweets/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-promoted-tweets-id',
                          binding)


def tailored_audiences_by_id_and_account_id(id, account_id):
    """
    Delete a tailored audience from an account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param id: The identifier for the tailored audience.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-tailored-audiences-id',
                          binding)


def targeting_criteria_by_id_and_account_id(id, account_id):
    """
    Remove a targeting criterion associated with a line item.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param id: The identifier for a targeting criteria associated with a
        campaign’s line items.
    """
    binding = {'account_id': account_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/targeting_criteria/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-targeting-criteria-id',
                          binding)


def videos_by_id_and_account_id(id, account_id, video_id):
    """
    Delete the specified video belonging to the current ads account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param video_id: The UUID identifier of the video object to be deleted.
    """
    binding = {'account_id': account_id, 'video_id': video_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/videos/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-videos-id',
                          binding)


def web_event_tags_by_id_and_account_id(id, account_id, web_event_tag_id):
    """
    Delete a specific web event tag associated to the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param web_event_tag_id: The identifier for the web event tag.
    """
    binding = {'account_id': account_id, 'web_event_tag_id': web_event_tag_id,
               'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/web_event_tags/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-accounts-account-id-web-event-tags-id',
                          binding)


def by_account_id(account_id):
    """


    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.
    """
    binding = {'account_id': account_id}
    url = 'https://ads-api-sandbox.twitter.com/1/accounts/{account_id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-1-accounts-account-id',
                          binding)


def features_by_account_id(account_id, type):
    """


    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param type: A comma-separated list of account features to remove from the
        account.
    """
    binding = {'account_id': account_id, 'type': type}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/features'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-1-accounts-account-id-features',
                          binding)


def funding_instruments_by_id_and_account_id(id, account_id,
                                             funding_instrument_id):
    """


    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param funding_instrument_id: The identifier of funding instrument to
        delete.
    """
    binding = {'account_id': account_id, 'funding_instrument_id':
               funding_instrument_id, 'id': id}
    url = 'https://ads-api-sandbox.twitter.com/1/accounts/{account_id}/funding_instruments/{id}'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-1-accounts-account-id-funding-instruments-id',
                          binding)


def tailored_audiences_permissions_by_id_and_account_id(id, account_id,
                                                        tailored_audience_id,
                                                        tailored_audience_permission_id):
    """
    Revokes permissions to a specific audience already shared with a different
    advertiser account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request.

    :param tailored_audience_id: The ID of the tailored audience.

    :param tailored_audience_permission_id: The ID of the tailored audience
        permission object.
    """
    binding = {'account_id': account_id, 'tailored_audience_id':
               tailored_audience_id, 'tailored_audience_permission_id':
               tailored_audience_permission_id, 'id': id}
    url = 'https://ads-api.twitter.com/1/accounts/{account_id}/tailored_audiences/{id}/permissions'
    url = url.format(**binding)
    return TwitterRequest('DELETE',
                          url,
                          'ads:accounts',
                          'delete-1-accounts-account-id-tailored-audiences-id-permissions',
                          binding)



###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def accounts(*, account_ids=_ELIDE, count=_ELIDE, cursor=_ELIDE,
             sort_by=_ELIDE, with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all advertising-enabled accounts the
    authenticating user has access to.

    :param account_ids: Scope the response to just the desired account IDs by
        specifying a comma-separated list of identifiers. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_ids': account_ids, 'count': count, 'cursor': cursor,
               'sort_by': sort_by, 'with_deleted': with_deleted,
               'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts'
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts',
                           binding)


def by_account_id(account_id, *, with_deleted=_ELIDE):
    """
    Retrieve a specific account that the authenticating user has access to.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id',
                           binding)


def account_media_by_account_id(account_id, *, account_media_ids=_ELIDE,
                                count=_ELIDE, cursor=_ELIDE, sort_by=_ELIDE,
                                with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all account media associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param account_media_ids: Scope the response to just the desired account
        media by specifying a comma-separated list of identifiers. Up to 200
        IDs may be provided. Type: string Example: 3wpx

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'account_media_ids':
               account_media_ids, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by, 'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/account_media'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-account-media',
                           binding)


def account_media_by_account_media_id_and_account_id(account_media_id,
                                                     account_id, *,
                                                     with_deleted=_ELIDE):
    """
    Retrieve a specific account media object associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param account_media_id: A reference to the account media you are operating
        with in the request. Type: string Example: 2pnfd

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'account_media_id': account_media_id,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/account_media/{account_media_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-account-media-account-media-id',
                           binding)


def app_event_provider_configurations_by_account_id(account_id, *,
                                                    count=_ELIDE,
                                                    cursor=_ELIDE,
                                                    ids=_ELIDE,
                                                    sort_by=_ELIDE,
                                                    with_deleted=_ELIDE,
                                                    with_total_count=_ELIDE):
    """
    Retrieve details for some or all application event provider configurations
    (core configuration for Mobile Application Conversion Tracking) associated
    with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param ids: Scope the response to just the desired configurations by
        specifying a comma-separated list of identifiers. Up to 200 IDs may be
        provided. Type: string Example: 25n

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'ids': ids, 'sort_by': sort_by, 'with_deleted': with_deleted,
               'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/app_event_provider_configurations'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-app-event-provider-configurations',
                           binding)


def app_event_tags_by_account_id(account_id, *, app_event_tag_ids=_ELIDE,
                                 count=_ELIDE, cursor=_ELIDE, sort_by=_ELIDE,
                                 with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all application event tags associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param app_event_tag_ids: Scope the response to just the desired app event
        tags by specifying a comma-separated list of identifiers. Up to 200 IDs
        may be provided. Type: string Example: jhp

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'app_event_tag_ids':
               app_event_tag_ids, 'count': count, 'cursor': cursor, 'sort_by':
               sort_by, 'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/app_event_tags'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-app-event-tags',
                           binding)


def app_event_tags_by_id_and_account_id(id, account_id, *,
                                        with_deleted=_ELIDE):
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/app_event_tags/{id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-app-event-tags-id',
                           binding)


def app_lists_by_account_id(account_id, *, app_list_ids=_ELIDE, count=_ELIDE,
                            cursor=_ELIDE, sort_by=_ELIDE,
                            with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all app lists associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param app_list_ids: Scope the response to just the desired app lists by
        specifying a comma-separated list of identifiers. Up to 200 IDs may be
        provided. Type: string Example: wm7x

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'app_list_ids': app_list_ids,
               'count': count, 'cursor': cursor, 'sort_by': sort_by,
               'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/app_lists'
    url = url.format(**binding)
    return _TwitterRequest('GET',
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/app_lists/{app_list_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/auction_insights'
    url = url.format(**binding)
    return _TwitterRequest('GET',
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/authenticated_user_access'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-authenticated-user-access',
                           binding)


def campaigns_by_account_id(account_id, *, campaign_ids=_ELIDE, count=_ELIDE,
                            cursor=_ELIDE, draft_only=_ELIDE,
                            funding_instrument_ids=_ELIDE, sort_by=_ELIDE,
                            with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all campaigns associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param campaign_ids: Scope the response to just the desired campaigns by
        specifying a comma-separated list of identifiers. Up to 200 IDs may be
        provided. Type: string Example: 8wku2

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param draft_only: Scope the response to just draft campaigns. Type:
        boolean Default: false Possible values: true, false

    :param funding_instrument_ids: Scope the response to just the campaigns
        under specific funding instruments by specifying a comma-separated list
        of identifiers. Up to 200 IDs may be provided. Type: string Example:
        lygyi

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'campaign_ids': campaign_ids,
               'count': count, 'cursor': cursor, 'draft_only': draft_only,
               'funding_instrument_ids': funding_instrument_ids, 'sort_by':
               sort_by, 'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/campaigns'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-campaigns',
                           binding)


def campaigns_by_campaign_id_and_account_id(campaign_id, account_id, *,
                                            with_deleted=_ELIDE):
    """
    Retrieve a specific campaign associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param campaign_id: A reference to the campaign you are operating with in
        the request. Type: string Example: 8wku2

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'campaign_id': campaign_id,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/campaigns/{campaign_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-campaigns-campaign-id',
                           binding)


def cards_app_download_by_account_id(account_id, *, card_ids=_ELIDE,
                                     count=_ELIDE, cursor=_ELIDE,
                                     sort_by=_ELIDE, with_deleted=_ELIDE,
                                     with_total_count=_ELIDE):
    """
    Retrieve details for some or all app download cards associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_ids: Scope the response to just the desired app download cards
        by specifying a comma-separated list of identifiers. Up to 200 IDs may
        be provided. Type: string Example: 43jo7

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'count': count,
               'cursor': cursor, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/app_download'
    url = url.format(**binding)
    return _TwitterRequest('GET',
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/app_download/{card_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-app-download-card-id',
                           binding)


def cards_image_app_download_by_account_id(account_id, *, card_ids=_ELIDE,
                                           count=_ELIDE, cursor=_ELIDE,
                                           sort_by=_ELIDE,
                                           with_deleted=_ELIDE,
                                           with_total_count=_ELIDE):
    """
    Retrieve details for some or all image app download cards associated with
    the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_ids: Scope the response to just the desired image app download
        cards by specifying a comma-separated list of identifiers. Up to 200
        IDs may be provided. Type: string Example: 4ca39

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'count': count,
               'cursor': cursor, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_app_download'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-image-app-download',
                           binding)


def cards_image_app_download_by_card_id_and_account_id(card_id, account_id,
                                                       *, with_deleted=_ELIDE):
    """
    Retrieve a specific image app download card associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_id: A reference to the image app download card you are
        operating with in the request. Type: string Example: 4hudo

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'card_id': card_id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_app_download/{card_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-image-app-download-card-id',
                           binding)


def cards_image_conversation_by_account_id(account_id, *, card_ids=_ELIDE,
                                           count=_ELIDE, cursor=_ELIDE,
                                           sort_by=_ELIDE,
                                           with_deleted=_ELIDE,
                                           with_total_count=_ELIDE):
    """
    Retrieve details for some or all image conversation cards associated with
    the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_ids: Scope the response to just the desired image conversation
        cards by specifying a comma-separated list of identifiers. Up to 200
        IDs may be provided. Type: string Example: 2hbtz

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'count': count,
               'cursor': cursor, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_conversation'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-image-conversation',
                           binding)


def cards_image_conversation_by_card_id_and_account_id(card_id, account_id,
                                                       *, with_deleted=_ELIDE):
    """
    Retrieve a specific image conversation card associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_id: A reference to the image conversation card you are
        operating with in the request. Type: string Example: 4i0qg

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'card_id': card_id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_conversation/{card_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-image-conversation-card-id',
                           binding)


def cards_video_app_download_by_account_id(account_id, *, card_ids=_ELIDE,
                                           count=_ELIDE, cursor=_ELIDE,
                                           sort_by=_ELIDE,
                                           with_deleted=_ELIDE,
                                           with_total_count=_ELIDE):
    """
    Retrieve details for some or all video app download cards associated with
    the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_ids: Scope the response to just the desired video app download
        cards by specifying a comma-separated list of identifiers. Up to 200
        IDs may be provided. Type: string Example: 2wjmk

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'count': count,
               'cursor': cursor, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_app_download'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-video-app-download',
                           binding)


def cards_video_app_download_by_card_id_and_account_id(card_id, account_id,
                                                       *, with_deleted=_ELIDE):
    """
    Retrieve a specific video app download card associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_id: A reference to the video app download card you are
        operating with in the request. Type: string Example: 4hug6

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'card_id': card_id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_app_download/{card_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-video-app-download-card-id',
                           binding)


def cards_video_conversation_by_account_id(account_id, *, card_ids=_ELIDE,
                                           count=_ELIDE, cursor=_ELIDE,
                                           sort_by=_ELIDE,
                                           with_deleted=_ELIDE,
                                           with_total_count=_ELIDE):
    """
    Retrieve details for some or all video conversation cards associated with
    the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_ids: Scope the response to just the desired video conversation
        cards by specifying a comma-separated list of identifiers. Up to 200
        IDs may be provided. Type: string Example: 2hc3b

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'count': count,
               'cursor': cursor, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_conversation'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-video-conversation',
                           binding)


def cards_video_conversation_by_card_id_and_account_id(card_id, account_id,
                                                       *, with_deleted=_ELIDE):
    """
    Retrieve a specific video conversation card associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_id: A reference to the video conversation card you are
        operating with in the request. Type: string Example: 4i0ya

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'card_id': card_id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_conversation/{card_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-video-conversation-card-id',
                           binding)


def cards_video_website_by_account_id(account_id, *, card_ids=_ELIDE,
                                      count=_ELIDE, cursor=_ELIDE,
                                      sort_by=_ELIDE, with_deleted=_ELIDE,
                                      with_total_count=_ELIDE):
    """
    Retrieve details for some or all video website cards associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_ids: Scope the response to just the desired video website cards
        by specifying a comma-separated list of identifiers. Up to 200 IDs may
        be provided. Type: string Example: 455hx

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'count': count,
               'cursor': cursor, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_website'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-video-website',
                           binding)


def cards_video_website_by_card_id_and_account_id(card_id, account_id, *,
                                                  with_deleted=_ELIDE):
    """
    Retrieve a specific video website card associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_id: A reference to the video website card you are operating
        with in the request. Type: string Example: 455hx

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'card_id': card_id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_website/{card_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-video-website-card-id',
                           binding)


def cards_website_by_account_id(account_id, *, card_ids=_ELIDE, count=_ELIDE,
                                cursor=_ELIDE, sort_by=_ELIDE,
                                with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all website cards associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_ids: Scope the response to just the desired website cards by
        specifying a comma-separated list of identifiers. Up to 200 IDs may be
        provided. Type: string Example: 3djgy

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'card_ids': card_ids, 'count': count,
               'cursor': cursor, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/website'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-website',
                           binding)


def cards_website_by_card_id_and_account_id(card_id, account_id, *,
                                            with_deleted=_ELIDE):
    """
    Retrieve a specific website card associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param card_id: A reference to the website card you are operating with in
        the request. Type: string Example: 4i91t

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'card_id': card_id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/cards/website/{card_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-cards-website-card-id',
                           binding)


def features_by_account_id(account_id, *, feature_keys=_ELIDE):
    """
    Retrieve the collection of whitelisted features accessible by this ads
    account. Features are indicated by a descriptive feature key and are only
    exposed on this endpoint if they are introduced in beta or an otherwise
    limited release and are available in the API. Features that do not meet
    this criteria will not be exposed on this endpoint.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param feature_keys: An optional parameter that enables querying for a
        specific feature key. Requests may include multiple comma-separated
        keys. Only the features that are accessible by this account will be
        included in the response. Type: string Possible value:
        AWARENESS_OBJECTIVE
    """
    binding = {'account_id': account_id, 'feature_keys': feature_keys}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/features'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-features',
                           binding)


def funding_instruments_by_account_id(account_id, *, count=_ELIDE,
                                      cursor=_ELIDE,
                                      funding_instrument_ids=_ELIDE,
                                      sort_by=_ELIDE, with_deleted=_ELIDE,
                                      with_total_count=_ELIDE):
    """
    Retrieve details for some or all funding instruments associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param funding_instrument_ids: Scope the response to just the desired
        funding instruments by specifying a comma-separated list of
        identifiers. Up to 200 IDs may be provided. Type: string Example: lygyi

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'funding_instrument_ids': funding_instrument_ids, 'sort_by':
               sort_by, 'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/funding_instruments'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-funding-instruments',
                           binding)


def funding_instruments_by_funding_instrument_id_and_account_id(funding_instrument_id,
                                                                account_id,
                                                                *,
                                                                with_deleted=_ELIDE):
    """
    Retrieve a specific funding instrument associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param funding_instrument_id: A reference to the funding instrument you are
        operating with in the request. Type: string Example: 43853bhii885

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'funding_instrument_id':
               funding_instrument_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/funding_instruments/:id'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-funding-instruments-funding-instrument-id',
                           binding)


def line_item_apps_by_account_id(account_id, *, count=_ELIDE, cursor=_ELIDE,
                                 line_item_id=_ELIDE,
                                 line_item_app_ids=_ELIDE, sort_by=_ELIDE,
                                 with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all apps associated with line items under the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param line_item_id: Scope the response to just the apps associated with
        the specified line item. Type: string Example: 6syda

    :param line_item_app_ids: Scope the response to just the desired line item
        apps by specifying a comma-separated list of identifiers. Up to 200 IDs
        may be provided. Type: string Example: 1eegy

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'line_item_id': line_item_id, 'line_item_app_ids':
               line_item_app_ids, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/line_item_apps'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-line-item-apps',
                           binding)


def line_item_apps_by_line_item_app_id_and_account_id(line_item_app_id,
                                                      account_id, *,
                                                      with_deleted=_ELIDE):
    """
    Retrieve a specific line item to mobile app association.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param line_item_app_id: A reference to the line item app you are operating
        with in the request. Type: string Example: vbbj

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'line_item_app_id': line_item_app_id,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/line_item_apps/{line_item_app_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-line-item-apps-line-item-app-id',
                           binding)


def line_items_by_account_id(account_id, *, campaign_ids=_ELIDE,
                             count=_ELIDE, cursor=_ELIDE, draft_only=_ELIDE,
                             funding_instrument_ids=_ELIDE,
                             line_item_ids=_ELIDE, sort_by=_ELIDE,
                             with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all line items associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param campaign_ids: Scope the response to just the line items under
        specific campaigns by specifying a comma-separated list of identifiers.
        Up to 200 IDs may be provided. Type: string Example: 8gdx6

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param draft_only: Scope the response to just line items under draft
        campaigns. Type: boolean Default: false Possible values: true, false

    :param funding_instrument_ids: Scope the response to just the line items
        under specific funding instruments by specifying a comma-separated list
        of identifiers. Up to 200 IDs may be provided. Type: string Example:
        lygyi

    :param line_item_ids: Scope the response to just the desired line items by
        specifying a comma-separated list of identifiers. Up to 200 IDs may be
        provided. Type: string Example: 8v7jo

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'campaign_ids': campaign_ids,
               'count': count, 'cursor': cursor, 'draft_only': draft_only,
               'funding_instrument_ids': funding_instrument_ids,
               'line_item_ids': line_item_ids, 'sort_by': sort_by,
               'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/line_items'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-line-items',
                           binding)


def line_items_by_line_item_id_and_account_id(line_item_id, account_id, *,
                                              with_deleted=_ELIDE):
    """
    Retrieve a specific line item associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param line_item_id: A reference to the line item you are operating with in
        the request. Type: string Example: 8v7jo

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/line_items/{line_item_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-line-items-line-item-id',
                           binding)


def media_creatives_by_account_id(account_id, *, campaign_id=_ELIDE,
                                  count=_ELIDE, cursor=_ELIDE,
                                  line_item_id=_ELIDE,
                                  media_creative_ids=_ELIDE, sort_by=_ELIDE,
                                  with_deleted=_ELIDE,
                                  with_total_count=_ELIDE):
    """
    Retrieve details for some or all media creatives associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param campaign_id: Scope the response to just the media creatives
        associated with the specified campaign. Type: string Example: 8gdx6

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param line_item_id: Scope the response to just the media creatives
        associated with the specified line item. Type: string Example: 8v7jo

    :param media_creative_ids: Scope the response to just the desired media
        creatives by specifying a comma-separated list of identifiers. Up to
        200 IDs may be provided. Type: string Example: 1bzq3

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'campaign_id': campaign_id, 'count':
               count, 'cursor': cursor, 'line_item_id': line_item_id,
               'media_creative_ids': media_creative_ids, 'sort_by': sort_by,
               'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/media_creatives'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-media-creatives',
                           binding)


def media_creatives_by_media_creative_id_and_account_id(media_creative_id,
                                                        account_id, *,
                                                        with_deleted=_ELIDE):
    """
    Retrieves details for a specific media creative associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param media_creative_id: A reference to the media creative you are
        operating with in the request. Type: string Example: 43853bhii885

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'media_creative_id':
               media_creative_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/media_creatives/{media_creative_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-media-creatives-media-creative-id',
                           binding)


def preroll_call_to_actions_by_account_id(account_id, line_item_id, *,
                                          count=_ELIDE, cursor=_ELIDE,
                                          preroll_call_to_action_ids=_ELIDE,
                                          sort_by=_ELIDE,
                                          with_deleted=_ELIDE,
                                          with_total_count=_ELIDE):
    """
    Retrieve details for some or all preroll Call-To-Actions (CTAs) associated
    with line items under the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param line_item_id: Scope the response to just the preroll CTAs associated
        with the specified line item. Type: string Example: 8v53k

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param preroll_call_to_action_ids: Scope the response to just the desired
        preroll CTAs by specifying a comma-separated list of identifiers. Up to
        200 IDs may be provided. Type: string Example: 8f0

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'count': count, 'cursor': cursor, 'preroll_call_to_action_ids':
               preroll_call_to_action_ids, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/preroll_call_to_actions'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-preroll-call-to-actions',
                           binding)


def preroll_call_to_actions_preroll_call_to_action_id_by_account_id(account_id,
                                                                    line_item_id,
                                                                    *,
                                                                    with_deleted=_ELIDE,
                                                                    count=_ELIDE,
                                                                    cursor=_ELIDE):
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/preroll_call_to_actions/:preroll_call_to_action_id'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-preroll-call-to-actions-preroll-call-to-action-id',
                           binding)


def promotable_users_by_account_id(account_id, *, count=_ELIDE,
                                   cursor=_ELIDE, promotable_user_ids=_ELIDE,
                                   sort_by=_ELIDE, with_deleted=_ELIDE,
                                   with_total_count=_ELIDE):
    """
    Retrieve details for some or all promotable users associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param promotable_user_ids: Scope the response to just the desired
        promotable users by specifying a comma-separated list of identifiers.
        Up to 200 IDs may be provided. Type: string Example: lygyi

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'promotable_user_ids': promotable_user_ids, 'sort_by': sort_by,
               'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/promotable_users'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-promotable-users',
                           binding)


def promoted__by_account_id(account_id, *, count=_ELIDE, cursor=_ELIDE,
                            line_item_id=_ELIDE, promoted_account_ids=_ELIDE,
                            sort_by=_ELIDE, with_deleted=_ELIDE,
                            with_total_count=_ELIDE):
    """
    Retrieve details for some or all promoted accounts associated with one or
    more line items under the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param line_item_id: Scope the response to just the promoted accounts
        associated with the specified line item. Type: string Example: 9bpb2

    :param promoted_account_ids: Scope the response to just the desired
        promoted accounts by specifying a comma-separated list of identifiers.
        Up to 200 IDs may be provided. Type: string Example: 19pl2

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'line_item_id': line_item_id, 'promoted_account_ids':
               promoted_account_ids, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/promoted_accounts'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-promoted-accounts',
                           binding)


def promoted__by_promoted_account_id_and_account_id(promoted_account_id,
                                                    account_id, *,
                                                    with_deleted=_ELIDE):
    """
    Retrieve a specific reference to an account associated with a line item
    under the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param promoted_account_id: A reference to the promoted account you are
        operating with in the request. Type: string Example: 19pl2

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'promoted_account_id':
               promoted_account_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/promoted_accounts/{promoted_account_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-promoted-accounts-promoted-account-id',
                           binding)


def promoted_tweets_by_account_id(account_id, *, count=_ELIDE, cursor=_ELIDE,
                                  line_item_ids=_ELIDE,
                                  promoted_tweet_ids=_ELIDE, sort_by=_ELIDE,
                                  with_deleted=_ELIDE,
                                  with_total_count=_ELIDE):
    """
    Retrieve details for some or all Tweets associated with one or more line
    items under the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param line_item_ids: Scope the response to just the Tweets associated with
        specific line items by specifying a comma-separated list of
        identifiers. Up to 200 IDs may be provided. Type: string Example: 96uzp

    :param promoted_tweet_ids: Scope the response to just the desired promoted
        Tweets by specifying a comma-separated list of identifiers. Up to 200
        IDs may be provided. Type: string Example: 1efwlo

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'line_item_ids': line_item_ids, 'promoted_tweet_ids':
               promoted_tweet_ids, 'sort_by': sort_by, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/promoted_tweets'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-promoted-tweets',
                           binding)


def promoted_tweets_by_promoted_tweet_id_and_account_id(promoted_tweet_id,
                                                        account_id, *,
                                                        with_deleted=_ELIDE):
    """
    Retrieve a specific reference to a Tweet associated with a line item under
    the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param promoted_tweet_id: A reference to the promoted Tweet you are
        operating with in the request. Type: string Example: 1efwlo

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'promoted_tweet_id':
               promoted_tweet_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/promoted_tweets/{promoted_tweet_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-promoted-tweets-promoted-tweet-id',
                           binding)


def reach_estimate_by_account_id(account_id, product_type, objective,
                                 bid_amount_local_micro, currency,
                                 campaign_daily_budget_amount_local_micro, *,
                                 bid_type=_ELIDE, followers_of_users=_ELIDE,
                                 similar_to_followers_of_users=_ELIDE,
                                 locations=_ELIDE, interests=_ELIDE,
                                 gender=_ELIDE, platforms=_ELIDE,
                                 tailored_audiences=_ELIDE,
                                 tailored_audiences_expanded=_ELIDE,
                                 languages=_ELIDE, platform_versions=_ELIDE,
                                 devices=_ELIDE, behaviors=_ELIDE,
                                 behaviors_expanded=_ELIDE,
                                 campaign_engagement=_ELIDE,
                                 user_engagement=_ELIDE,
                                 engagement_type=_ELIDE,
                                 network_operators=_ELIDE,
                                 app_store_categories=_ELIDE,
                                 app_store_categories_expanded=_ELIDE,
                                 exact_keywords=_ELIDE,
                                 broad_keywords=_ELIDE,
                                 phrase_keywords=_ELIDE, age_buckets=_ELIDE,
                                 wifi_only=_ELIDE):
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/reach_estimate'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-reach-estimate',
                           binding)


def recommendations_by_account_id(account_id):
    """
    Status:

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertising API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Note that this
        parameter is part of the resources path and should not be included as
        an additional parameter in your request. Type: string Example:
        18ce54d4x5t
    """
    binding = {'account_id': account_id}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/recommendations'
    url = url.format(**binding)
    return _TwitterRequest('GET',
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/recommendations/{recommendation_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-recommendations-recommendation-id',
                           binding)


def scheduled_promoted_tweets_by_account_id(account_id, *, count=_ELIDE,
                                            cursor=_ELIDE,
                                            line_item_ids=_ELIDE,
                                            scheduled_promoted_tweet_ids=_ELIDE,
                                            sort_by=_ELIDE,
                                            with_deleted=_ELIDE,
                                            with_total_count=_ELIDE):
    """
    Retrieve details for some or all scheduled promoted Tweets associated with
    the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param line_item_ids: Scope the response to just the scheduled Tweets
        associated with specific line items by specifying a comma-separated
        list of identifiers. Up to 200 IDs may be provided. Type: string
        Example: 8xdpe

    :param scheduled_promoted_tweet_ids: Scope the response to just the desired
        scheduled promoted Tweets by specifying a comma-separated list of
        identifiers. Up to 200 IDs may be provided. Type: string Example: 1xboq

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'line_item_ids': line_item_ids, 'scheduled_promoted_tweet_ids':
               scheduled_promoted_tweet_ids, 'sort_by': sort_by,
               'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_promoted_tweets'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-scheduled-promoted-tweets',
                           binding)


def scheduled_promoted_tweets_by_scheduled_promoted_tweet_id_and_account_id(scheduled_promoted_tweet_id,
                                                                            account_id,
                                                                            *,
                                                                            with_deleted=_ELIDE):
    """
    Retrieve a specific scheduled promoted Tweet associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param scheduled_promoted_tweet_id: A reference to the scheduled promoted
        Tweet you are operating with in the request. Type: string Example:
        1xboq

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'scheduled_promoted_tweet_id':
               scheduled_promoted_tweet_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_promoted_tweets/{scheduled_promoted_tweet_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-scheduled-promoted-tweets-scheduled-promoted-tweet-id',
                           binding)


def scheduled_tweets_by_account_id(account_id, *, count=_ELIDE,
                                   cursor=_ELIDE, with_deleted=_ELIDE,
                                   user_id=_ELIDE):
    """
    Retrieve details for some or all scheduled Tweets associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 100 Min, Max: 1, 200

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: c-j3cn6n40

    :param with_deleted: Include deleted results in your request. Deleted
        results can be identified by the scheduled_status response attribute
        and will have a value of DELETED. Type: boolean Default: false Possible
        values: true, false

    :param user_id: Specify the user to retrieve scheduled Tweets for. Defaults
        to the FULL promotable user on the account when not set. Type: long
        Example: 756201191646691328
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'with_deleted': with_deleted, 'user_id': user_id}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_tweets'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-scheduled-tweets',
                           binding)


def scheduled_tweets_by_scheduled_tweet_id_and_account_id(scheduled_tweet_id,
                                                          account_id, *,
                                                          with_deleted=_ELIDE):
    """
    Retrieve a specific scheduled Tweet associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param scheduled_tweet_id: A reference to the scheduled Tweet you are
        operating with in the request. Type: long Example: 867608856989270016

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'scheduled_tweet_id':
               scheduled_tweet_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_tweets/{scheduled_tweet_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-scheduled-tweets-scheduled-tweet-id',
                           binding)


def scoped_timeline_by_account_id(account_id, *, count=_ELIDE, cursor=_ELIDE,
                                  objective=_ELIDE, scoped_to=_ELIDE,
                                  trim_user=_ELIDE, tweet_mode=_ELIDE,
                                  user_id=_ELIDE):
    """
    Retrieve Tweet details for the account’s full promotable user (default) or
    the user specified in the

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: AAAAAFhLRpQLNF-
        sGBSgAA

    :param objective: Filter the results to only those Tweets appropriate for
        the given objective. See note above (top of page) about how filtering
        by objective affects result paging. Type: enum Possible values:
        APP_ENGAGEMENTS, APP_INSTALLS, AWARENESS, FOLLOWERS, TWEET_ENGAGEMENTS,
        VIDEO_VIEWS, VIDEO_VIEWS_PREROLL, WEBSITE_CLICKS

    :param scoped_to: followers to find Tweets in the users’s timeline or none
        to find nullcasted Tweets. Type: string Default: followers Possible
        values: followers, none

    :param trim_user: Whether to exclude the user object in the Tweet response.
        When enabled, the only part of the user object that will be returned is
        the Tweet’s author’s user ID. Type: boolean Default: false Possible
        values: true, false

    :param tweet_mode: Whether the response should be in compatibility or
        extended mode. See this for additional information. Type: string
        Possible values: compat, extended

    :param user_id: Specifies the user to scope Tweets to. Defaults to the FULL
        promotable user on the account when not set. Type: long Example:
        756201191646691328
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'objective': objective, 'scoped_to': scoped_to, 'trim_user':
               trim_user, 'tweet_mode': tweet_mode, 'user_id': user_id}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/scoped_timeline'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-scoped-timeline',
                           binding)


def tailored_audience_changes_by_account_id(account_id, *, count=_ELIDE,
                                            cursor=_ELIDE, sort_by=_ELIDE,
                                            tailored_audience_change_ids=_ELIDE,
                                            with_deleted=_ELIDE,
                                            with_total_count=_ELIDE):
    """
    Retrieve details for some or all changes made to tailored audiences
    associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param tailored_audience_change_ids: Scope the response to just the desired
        tailored audience changes by specifying a comma-separated list of
        identifiers. Up to 200 IDs may be provided. Type: string Example: 768t3

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'sort_by': sort_by, 'tailored_audience_change_ids':
               tailored_audience_change_ids, 'with_deleted': with_deleted,
               'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audience_changes'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-tailored-audience-changes',
                           binding)


def tailored_audience_changes_by_tailored_audience_change_id_and_account_id(tailored_audience_change_id,
                                                                            account_id,
                                                                            *,
                                                                            with_deleted=_ELIDE):
    """
    Retrieve a specific tailored audience change record.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param tailored_audience_change_id: A reference to the tailored audience
        change record you are operating with in the request. Type: string
        Example: 7nm3j

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'tailored_audience_change_id':
               tailored_audience_change_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audience_changes/{tailored_audience_change_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-tailored-audience-changes-tailored-audience-change-id',
                           binding)


def tailored_audiences_by_account_id(account_id, *, count=_ELIDE,
                                     cursor=_ELIDE, permission_scope=_ELIDE,
                                     sort_by=_ELIDE,
                                     tailored_audience_ids=_ELIDE,
                                     with_deleted=_ELIDE,
                                     with_total_count=_ELIDE):
    """
    Retrieve details for some or all tailored audiences associated with the
    current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param permission_scope: Allows filtering the response to lists you own or
        lists that have been shared with you. By default, without specifying
        this parameter you will only see audiences you own. Type: enum Default:
        OWNER Possible values: OWNER, SHARED

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param tailored_audience_ids: Scope the response to just the desired
        tailored audiences by specifying a comma-separated list of identifiers.
        Up to 200 IDs may be provided. Type: string Example: 1nmth

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'permission_scope': permission_scope, 'sort_by': sort_by,
               'tailored_audience_ids': tailored_audience_ids, 'with_deleted':
               with_deleted, 'with_total_count': with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audiences'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-tailored-audiences',
                           binding)


def tailored_audiences_by_tailored_audience_id_and_account_id(tailored_audience_id,
                                                              account_id, *,
                                                              with_deleted=_ELIDE):
    """
    Retrieve specific tailored audience associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param tailored_audience_id: A reference to the tailored audience you are
        operating with in the request. Type: string Example: 2906h

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'tailored_audience_id':
               tailored_audience_id, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audiences/{tailored_audience_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-tailored-audiences-tailored-audience-id',
                           binding)


def tailored_audiences_permissions_by_tailored_audience_id_and_account_id(tailored_audience_id,
                                                                          account_id,
                                                                          *,
                                                                          count=_ELIDE,
                                                                          cursor=_ELIDE,
                                                                          granted_account_ids=_ELIDE,
                                                                          sort_by=_ELIDE,
                                                                          tailored_audience_permission_ids=_ELIDE,
                                                                          with_total_count=_ELIDE):
    """
    Retrieve details for some or all permissions associated with the specified
    tailored audience.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param tailored_audience_id: A reference to the tailored audience you are
        operating with in the request. Type: string Example: 1nmth

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param granted_account_ids: Scope the response to just the desired accounts
        by specifying a comma-separated list of identifiers. Up to 200 IDs may
        be provided. Type: string Example: 18ce54aymz3

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param tailored_audience_permission_ids: Scope the response to just the
        desired tailored audience permissions by specifying a comma-separated
        list of identifiers. Up to 200 IDs may be provided. Type: string
        Example: ri

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'tailored_audience_id':
               tailored_audience_id, 'count': count, 'cursor': cursor,
               'granted_account_ids': granted_account_ids, 'sort_by': sort_by,
               'tailored_audience_permission_ids':
               tailored_audience_permission_ids, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audiences/{tailored_audience_id}/permissions'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-tailored-audiences-tailored-audience-id-permissions',
                           binding)


def targeting_criteria_by_account_id(account_id, line_item_id, *,
                                     count=_ELIDE, cursor=_ELIDE,
                                     lang=_ELIDE, sort_by=_ELIDE,
                                     targeting_criterion_ids=_ELIDE,
                                     with_deleted=_ELIDE,
                                     with_total_count=_ELIDE):
    """
    Retrieve details for some or all of the targeting criteria associated with
    line items under the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param line_item_id: Scope the response to just the targeting criteria
        under the specified line item. Type: string Example: 8u94t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param lang: An ISO-639-1 language code. When passed, an additional
        localized_name attribute will be returned in the response for objects
        where a localized name is available. Type: string Example: fr

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param targeting_criterion_ids: Scope the response to just the desired
        targeting criteria by specifying a comma-separated list of identifiers.
        Up to 200 IDs may be provided. Type: string Example: dpl3a6

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'line_item_id': line_item_id,
               'count': count, 'cursor': cursor, 'lang': lang, 'sort_by':
               sort_by, 'targeting_criterion_ids': targeting_criterion_ids,
               'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/targeting_criteria'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-targeting-criteria',
                           binding)


def targeting_criteria_by_targeting_criterion_id_and_account_id(targeting_criterion_id,
                                                                account_id,
                                                                *,
                                                                lang=_ELIDE,
                                                                with_deleted=_ELIDE):
    """
    Retrieve a specific targeting criterion associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param targeting_criterion_id: A reference to the targeting criterion you
        are operating with in the request. Type: string Example: eijd4y

    :param lang: An ISO-639-1 language code. When passed, an additional
        localized_name attribute will be returned in the response for objects
        where a localized name is available. Type: string Example: fr

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'targeting_criterion_id':
               targeting_criterion_id, 'lang': lang, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/targeting_criteria/{targeting_criterion_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-targeting-criteria-targeting-criterion-id',
                           binding)


def targeting_suggestions_by_account_id(account_id, suggestion_type,
                                        targeting_values, *, count=_ELIDE):
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/targeting_suggestions'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-targeting-suggestions',
                           binding)


def tweet_preview_by_account_id(account_id, *, text=_ELIDE,
                                as_user_id=_ELIDE, media_ids=_ELIDE,
                                preview_target=_ELIDE):
    """
    Preview a Tweet that does not already exist as it would appear across a
    variety of different platforms; iPhone, Android and Web. You can preview a
    Tweet both for how it will look like on Twitter or on the

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param text: The text of your status update, typically up to 140
        characters. Required if no media_ids are specified. Type: string
        Example: hello, world

    :param as_user_id: The user ID of the advertiser on behalf of whom you are
        posting the Tweet. The advertiser must grant your handle (or handles)
        access to their ads account via ads.twitter.com. This permission allows
        you to call the API using the OAuth tokens of your own handle rather
        than the advertiser’s. Type: long Example: 756201191646691328

    :param media_ids: Associate media with the Tweet by specifying a comma-
        separated list of identifiers. Include up to 4 images, 1 animated GIF,
        or 1 video. See Uploading Media for additional details on uploading
        media. Type: long Example: 870320790339637248

    :param preview_target: The target to render the Tweet preview for. Type:
        enum Default: TWITTER_TIMELINE Possible values: PUBLISHER_NETWORK,
        TWITTER_TIMELINE
    """
    binding = {'account_id': account_id, 'text': text, 'as_user_id':
               as_user_id, 'media_ids': media_ids, 'preview_target':
               preview_target}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/tweet/preview'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-tweet-preview',
                           binding)


def tweet_preview_by_tweet_id_and_account_id(tweet_id, account_id, *,
                                             as_user_id=_ELIDE,
                                             preview_target=_ELIDE):
    """
    Preview an existing Tweet as it would appear across a variety of different
    platforms: Android, iPhone, and Web. You can preview a Tweet both for how
    it will look like on Twitter or on the

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param tweet_id: The unique identifier referring to a Tweet. Type: long
        Example: 880950824339419136

    :param as_user_id: The user ID of the advertiser on behalf of whom you are
        posting the Tweet. The advertiser must grant your handle (or handles)
        access to their ads account via ads.twitter.com. This permission allows
        you to call the API using the OAuth tokens of your own handle rather
        than the advertiser’s. Type: long Example: 756201191646691328

    :param preview_target: The target to render the Tweet preview for. Type:
        enum Default: TWITTER_TIMELINE Possible values: PUBLISHER_NETWORK,
        TWITTER_TIMELINE
    """
    binding = {'account_id': account_id, 'tweet_id': tweet_id, 'as_user_id':
               as_user_id, 'preview_target': preview_target}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/tweet/preview/{tweet_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-tweet-preview-tweet-id',
                           binding)


def videos_by_account_id(account_id, *, count=_ELIDE, cursor=_ELIDE,
                         video_ids=_ELIDE, with_deleted=_ELIDE):
    """
    Retrieve details for some or all videos associated with the current
    account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 10 Min, Max: 1, 50

    :param cursor: Specifies a cursor to get the next page of results. See
        Pagination for more information. Type: string Example: 8x7v00oow

    :param video_ids: Scope the response to just the desired videos by
        specifying a comma-separated list of identifiers. Up to 200 IDs may be
        provided. Type: string Example: 13_875943225764098048

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'video_ids': video_ids, 'with_deleted': with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/videos'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-videos',
                           binding)


def videos_by_video_id_and_account_id(video_id, account_id, *,
                                      with_deleted=_ELIDE):
    """
    Retrieve a specific video associated with the current account.

    :param account_id: The identifier for the leveraged account. Appears within
        the resource’s path and is generally a required parameter for all
        Advertiser API requests excluding GET accounts. The specified account
        must be associated with the authenticating user. Type: string Example:
        18ce54d4x5t

    :param video_id: A reference to video you are operating with in the
        request. Type: string Example: 13_898199863531261954

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false
    """
    binding = {'account_id': account_id, 'video_id': video_id, 'with_deleted':
               with_deleted}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/videos/{video_id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-videos-video-id',
                           binding)


def web_event_tags_by_account_id(account_id, *, count=_ELIDE, cursor=_ELIDE,
                                 sort_by=_ELIDE, web_event_tag_ids=_ELIDE,
                                 with_deleted=_ELIDE, with_total_count=_ELIDE):
    """
    Retrieve details for some or all web event tags associated with the current
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

    :param sort_by: Sorts by supported attribute in ascending or descending
        order. See Sorting for more information. Type: string Example:
        created_at-asc

    :param web_event_tag_ids: Scope the response to just the desired web event
        tags by specifying a comma-separated list of identifiers. Up to 200 IDs
        may be provided. Type: string Example: nzuh4

    :param with_deleted: Include deleted results in your request. Type: boolean
        Default: false Possible values: true, false

    :param with_total_count: Include the total_count response attribute. Note:
        This parameter will be ignored if cursor is specified. Note: Requests
        which include total_count will have lower rate limits, currently set at
        200 per 15 minutes. Type: boolean Default: false Possible values: true,
        false
    """
    binding = {'account_id': account_id, 'count': count, 'cursor': cursor,
               'sort_by': sort_by, 'web_event_tag_ids': web_event_tag_ids,
               'with_deleted': with_deleted, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/web_event_tags'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-web-event-tags',
                           binding)


def web_event_tags_by_id_and_account_id(id, account_id, *,
                                        with_deleted=_ELIDE):
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
    url = 'https://ads-api.twitter.com/2/accounts/{account_id}/web_event_tags/{id}'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'ads:accounts',
                           'get-accounts-account-id-web-event-tags-id',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts'] = 'https://dev.twitter.com/ads/reference/get/accounts'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/account_media'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/account_media'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/account_media/{account_media_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/account_media/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/app_event_provider_configurations'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/app_event_provider_configurations'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/app_event_tags'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/app_event_tags'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/app_event_tags/{id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/app_event_tags/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/app_lists'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/app_lists'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/app_lists/{app_list_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/app_lists/app_list_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/auction_insights'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/auction_insights'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/authenticated_user_access'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/authenticated_user_access'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/campaigns'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/campaigns'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/campaigns/{campaign_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/campaigns/campaign_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/app_download'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/app_download'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/app_download/{card_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/app_download/card_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_app_download'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/image_app_download'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_app_download/{card_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/image_app_download/card_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_conversation'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/image_conversation'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/image_conversation/{card_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/image_conversation/card_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_app_download'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/video_app_download'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_app_download/{card_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/video_app_download/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_conversation'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/video_conversation'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_conversation/{card_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/video_conversation/card_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_website'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/video_website'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/video_website/{card_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/video_website/card_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/website'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/website'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/cards/website/{card_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/cards/website/card_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/features'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/features'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/funding_instruments'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/funding_instruments'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/funding_instruments/:id'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/funding_instruments/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/line_item_apps'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/line_item_apps'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/line_item_apps/{line_item_app_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/line_item_apps/line_item_app_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/line_items'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/line_items'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/line_items/{line_item_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/line_items/line_item_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/media_creatives'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/media_creatives'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/media_creatives/{media_creative_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/media_creatives/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/preroll_call_to_actions'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/preroll_call_to_actions'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/preroll_call_to_actions/:preroll_call_to_action_id'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/preroll_call_to_actions/preroll_call_to_action_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/promotable_users'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/promotable_users'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/promoted_accounts'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/promoted_accounts'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/promoted_accounts/{promoted_account_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/promoted_accounts/promoted_account_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/promoted_tweets'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/promoted_tweets'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/promoted_tweets/{promoted_tweet_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/promoted_tweets/promoted_tweet_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/reach_estimate'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/reach_estimate'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/recommendations'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/recommendations'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/recommendations/{recommendation_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/recommendations/recommendation_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_promoted_tweets'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/scheduled_promoted_tweets'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_promoted_tweets/{scheduled_promoted_tweet_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/scheduled_promoted_tweets/scheduled_promoted_tweet_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_tweets'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/scheduled_tweets'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/scheduled_tweets/{scheduled_tweet_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/scheduled_tweets/scheduled_tweet_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/scoped_timeline'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/scoped_timeline'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audience_changes'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/tailored_audience_change'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audience_changes/{tailored_audience_change_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/tailored_audience_change/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audiences'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/tailored_audiences'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audiences/{tailored_audience_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/tailored_audiences/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/tailored_audiences/{tailored_audience_id}/permissions'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/tailored_audiences/id/permissions'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/targeting_criteria'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/targeting_criteria'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/targeting_criteria/{targeting_criterion_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/targeting_criteria/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/targeting_suggestions'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/targeting_suggestions'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/tweet/preview'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/tweet/preview'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/tweet/preview/{tweet_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/tweet/preview/tweet_id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/videos'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/videos'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/videos/{video_id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/videos/id'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/web_event_tags'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/web_event_tags'
_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/accounts/{account_id}/web_event_tags/{id}'] = 'https://dev.twitter.com/ads/reference/get/accounts/account_id/web_event_tags/id'

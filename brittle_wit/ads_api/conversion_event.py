###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, IGNORE


def conversion_event(hashed_device_id, app_id, os_type, conversion_time,
                     conversion_type, *, click_window=IGNORE,
                     view_through_window=IGNORE,
                     non_twitter_engagement_time=IGNORE,
                     non_twitter_engagement_type=IGNORE,
                     extra_device_ids=IGNORE, conversion_value_micro=IGNORE,
                     limit_ad_tracking=IGNORE, registration_method=IGNORE,
                     content_type=IGNORE, content_id=IGNORE,
                     price_currency=IGNORE, price_micro=IGNORE, level=IGNORE,
                     number_items=IGNORE, search_string=IGNORE,
                     user_payment_info=IGNORE, max_rated_value=IGNORE,
                     description=IGNORE):
    """
    Record a mobile measurement conversion event. The response will indicate
    Twitter or Twitter Audience Platform (TAP) attribution. Relates to

    :param hashed_device_id: The HMAC_SHA-256 hashed IDFA or AdID.

    :param app_id: The unique identifier with the corresponding app store.

    :param os_type: The OS type for this app. Either IOS or ANDROID.

    :param conversion_time: The time of the conversion event in an ISO-8601
        timestamp format, with milliseconds appended. For example,
        1400726308103 would be represented as 2014-05-22T02:38:28.103Z.

    :param conversion_type: The type of conversion event. Possible values
        include PURCHASE, SIGN_UP, INSTALL, RE_ENGAGE, UPDATE,
        TUTORIAL_COMPLETE, RESERVATION, ADD_TO_CART, ADD_TO_WISHLIST, LOGIN,
        CHECKOUT_INITIATED, SEARCH, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED,
        CONTENT_VIEW, SHARE, INVITE, ADDED_PAYMENT_INFO, SPENT_CREDITS, RATED.

    :param click_window: The click window for this event in days.

    :param view_through_window: The view through window for this event in days.

    :param non_twitter_engagement_time: The time of the last non-twitter
        engagement prior to the conversion

    :param non_twitter_engagement_type: The type of non-twitter engagement
        prior to the conversion event, Possible values are CLICK or VIEW.

    :param extra_device_ids: A SHA256 of the SHA1 of the device ID passed in
        hashed_device_id, plus any additional hashed device IDs.

    :param conversion_value_micro: The value of this conversion event in
        micros.

    :param limit_ad_tracking: Indicate if this conversion event will be used to
        influence the serving of ads to end users. Setting the parameter to
        true will indicate intent to exclude the data from being used for
        purposes other than tracking and reporting.

    :param registration_method: Event metadata: A string describing the method
        of registration for the app associated to this event.

    :param content_type: Event metadata: String specifying the type or category
        of content or a product associated with this event.

    :param content_id: Event metadata: A string ID for the content or product
        associated to this event such as an International Article Number (EAN)
        or other product or content ID

    :param price_currency: Event metadata: Expected to be an ISO 4217 code to
        indicate the currency associated to this event.

    :param price_micro: Event metadata: A price amount associated to this event
        in micros.

    :param level: Event metadata: A level associated with this event.

    :param number_items: Event metadata: Number of items associated to this
        event.

    :param search_string: Event metadata: Any search string to be associated to
        this event.

    :param user_payment_info: Event metadata: A boolean value to indicate
        whether user payment is stored.

    :param max_rated_value: Event metadata: A double value to indicate the max
        rated value of this event.

    :param description: Event metadata: Any string description for this event.
    """
    binding = {'hashed_device_id': hashed_device_id, 'app_id': app_id,
               'os_type': os_type, 'conversion_time': conversion_time,
               'conversion_type': conversion_type, 'click_window':
               click_window, 'view_through_window': view_through_window,
               'non_twitter_engagement_time': non_twitter_engagement_time,
               'non_twitter_engagement_type': non_twitter_engagement_type,
               'extra_device_ids': extra_device_ids, 'conversion_value_micro':
               conversion_value_micro, 'limit_ad_tracking': limit_ad_tracking,
               'registration_method': registration_method, 'content_type':
               content_type, 'content_id': content_id, 'price_currency':
               price_currency, 'price_micro': price_micro, 'level': level,
               'number_items': number_items, 'search_string': search_string,
               'user_payment_info': user_payment_info, 'max_rated_value':
               max_rated_value, 'description': description}
    url = 'https://ads-api.twitter.com/1/conversion_event'
    return TwitterRequest('POST',
                          url,
                          'ads:conversion_event',
                          'post-conversion-event',
                          binding)



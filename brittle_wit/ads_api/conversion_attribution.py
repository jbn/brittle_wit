###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def conversion_attribution(hashed_device_id, app_id, os_type, conversion_time, conversion_type, *, click_window=IGNORE, view_through_window=IGNORE, non_twitter_engagement_time=IGNORE, non_twitter_engagement_type=IGNORE, extra_device_ids=IGNORE):
    """
    Query Twitter to check on conversion attribution without writing a
    conversion event. Response will indicate Twitter attribution. Relates to
    
    :param hashed_device_id: The HMAC_SHA-256 hashed IDFA or AdID. Type: string
        Example: ABCD1234XYZ (True)
    
    
    :param app_id: The unique identifier with the corresponding app store. Type
        : int, string Example: 333903271, com.vine.android (True)
    
    
    :param os_type: The OS type for the app. Type: enum Possible values: IOS, A
        NDROID (True)
    
    
    :param conversion_time: The time of the conversion event in an ISO-8601 tim
        estamp format, with milliseconds appended. Type: string Example:
        2014-05-22T02:38:28.103Z (True)
    
    
    :param conversion_type: The type of conversion event. Type: enum Possible v
        alues: PURCHASE, SIGN_UP, INSTALL, RE_ENGAGE, UPDATE,
        TUTORIAL_COMPLETE, RESERVATION, ADD_TO_CART, ADD_TO_WISHLIST, LOGIN,
        CHECKOUT_INITIATED, SEARCH, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED,
        CONTENT_VIEW, SHARE, INVITE, ADDED_PAYMENT_INFO, SPENT_CREDITS, RATED
        (True)
    
    
    :param click_window: The click window for this event in days. Type: int Def
        ault: 14 Possible values: 1, 7, 14, 30 (False)
    
    
    :param view_through_window: The view through window for this event in days.
        Type: int Default: 1 Possible values: 0, 1, 7, 14, 30 (False)
    
    
    :param non_twitter_engagement_time: The time of the last non-twitter engage
        ment prior to the conversion. Type: string Example:
        2014-05-22T02:38:28.103Z (False)
    
    
    :param non_twitter_engagement_type: The type of non-twitter engagement prio
        r to the conversion event. Type: enum Possible values: CLICK, VIEW
        (False)
    
    
    :param extra_device_ids: A SHA256 of the SHA1 of the device ID passed in ha
        shed_device_id, plus any additional hashed device IDs. Type: string
        Example: ABCD1234XYZ, DCBA4321XYZ (False)
    """
    url = "Resource URL¶
https://ads-api.twitter.com/1/conversion_attribution"
    return TwitterRequest('GET',
                          url,
                          'ADS:CONVERSION_ATTRIBUTION',
                          'GET-CONVERSION-ATTRIBUTION',
                          hashed_device_id=hashed_device_id
                          app_id=app_id
                          os_type=os_type
                          conversion_time=conversion_time
                          conversion_type=conversion_type
                          click_window=click_window
                          view_through_window=view_through_window
                          non_twitter_engagement_time=non_twitter_engagement_time
                          non_twitter_engagement_type=non_twitter_engagement_type
                          extra_device_ids=extra_device_ids)



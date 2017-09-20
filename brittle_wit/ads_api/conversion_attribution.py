###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def conversion_attribution(app_id, conversion_time, conversion_type,
                           hashed_device_id, os_type, *, click_window=_ELIDE,
                           extra_device_ids=_ELIDE,
                           non_twitter_engagement_time=_ELIDE,
                           non_twitter_engagement_type=_ELIDE,
                           view_through_window=_ELIDE):
    """
    Query Twitter to check on conversion attribution without writing a
    conversion event. Response will indicate Twitter attribution. Relates to

    :param app_id: The unique identifier with the corresponding app store.
        Type: int, string Example: 333903271, com.vine.android

    :param conversion_time: The time of the conversion event in an ISO-8601
        timestamp format, with milliseconds appended. Type: string Example:
        2014-05-22T02:38:28.103Z

    :param conversion_type: The type of conversion event. Type: enum Possible
        values: ACHIEVEMENT_UNLOCKED, ADDED_PAYMENT_INFO, ADD_TO_CART,
        ADD_TO_WISHLIST, CHECKOUT_INITIATED, CONTENT_VIEW, INSTALL, INVITE,
        LEVEL_ACHIEVED, LOGIN, PURCHASE, RATED, RESERVATION, RE_ENGAGE, SEARCH,
        SHARE, SIGN_UP, SPENT_CREDITS, TUTORIAL_COMPLETE, UPDATE

    :param hashed_device_id: The HMAC_SHA-256 hashed IDFA or AdID. Type: string
        Example: ABCD1234XYZ

    :param os_type: The OS type for the app. Type: enum Possible values: IOS,
        ANDROID

    :param click_window: The click window for this event in days. Note: Only
        the possible values listed below are accepted. Type: int Default: 14
        Possible values: 1, 7, 14, 30

    :param extra_device_ids: A SHA256 of the SHA1 of the device ID passed in
        hashed_device_id, plus any additional hashed device IDs. Type: string
        Example: ABCD1234XYZ, DCBA4321XYZ

    :param non_twitter_engagement_time: The time of the last non-twitter
        engagement prior to the conversion. Type: string Example:
        2014-05-22T02:38:28.103Z

    :param non_twitter_engagement_type: The type of non-twitter engagement
        prior to the conversion event. Type: enum Possible values: CLICK, VIEW

    :param view_through_window: The view through window for this event in days.
        Note: Only the possible values listed below are accepted. Type: int
        Default: 1 Possible values: 0, 1, 7, 14, 30
    """
    binding = {'app_id': app_id, 'conversion_time': conversion_time,
               'conversion_type': conversion_type, 'hashed_device_id':
               hashed_device_id, 'os_type': os_type, 'click_window':
               click_window, 'extra_device_ids': extra_device_ids,
               'non_twitter_engagement_time': non_twitter_engagement_time,
               'non_twitter_engagement_type': non_twitter_engagement_type,
               'view_through_window': view_through_window}
    url = 'https://ads-api.twitter.com/2/conversion_attribution'
    return _TwitterRequest('GET',
                           url,
                           'ads:conversion_attribution',
                           'get-conversion-attribution',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/conversion_attribution'] = 'https://dev.twitter.com/ads/reference/get/conversion_attribution'

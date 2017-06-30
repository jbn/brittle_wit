###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def settings():
    """
    Returns settings (including current trend, geo and sleep time information)
    for the authenticating user.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/account/settings.json'
    return TwitterRequest('GET',
                          url,
                          'rest:account',
                          'get-account-settings',
                          binding)


def verify_credentials(*, include_entities=ELIDE, skip_status=ELIDE,
                       include_email=ELIDE):
    """
    Returns an HTTP 200 OK response code and a representation of the requesting
    user if authentication was successful; returns a 401 status code and an
    error message if not. Use this method to test if supplied user credentials
    are valid.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user object.

    :param include_email: When set to true email will be returned in the user
        objects as a string. If the user does not have an email address on
        their account, or if the email address is not verified, null will be
        returned.
    """
    binding = {'include_entities': include_entities, 'skip_status':
               skip_status, 'include_email': include_email}
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    return TwitterRequest('GET',
                          url,
                          'rest:account',
                          'get-account-verify-credentials',
                          binding)


def remove_profile_banner():
    """
    Removes the uploaded profile banner for the authenticating user. Returns
    HTTP 200 upon success.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/account/remove_profile_banner.json'
    return TwitterRequest('POST',
                          url,
                          'rest:account',
                          'post-account-remove-profile-banner',
                          binding)


def settings(*, sleep_time_enabled=ELIDE, start_sleep_time=ELIDE,
             end_sleep_time=ELIDE, time_zone=ELIDE,
             trend_location_woeid=ELIDE, lang=ELIDE):
    """
    Updates the authenticating user’s settings.

    :param sleep_time_enabled: When set to true, t or 1, will enable sleep time
        for the user. Sleep time is the time when push or SMS notifications
        should not be sent to the user.

    :param start_sleep_time: The hour that sleep time should begin if it is
        enabled. The value for this parameter should be provided in ISO8601
        format (i.e. 00-23). The time is considered to be in the same timezone
        as the user’s time_zone setting.

    :param end_sleep_time: The hour that sleep time should end if it is
        enabled. The value for this parameter should be provided in ISO8601
        format (i.e. 00-23). The time is considered to be in the same timezone
        as the user’s time_zone setting.

    :param time_zone: The timezone dates and times should be displayed in for
        the user. The timezone must be one of the Rails TimeZone names.

    :param trend_location_woeid: The Yahoo! Where On Earth ID to use as the
        user’s default trend location. Global information is available by using
        1 as the WOEID. The woeid must be one of the locations returned by
        [node:59].

    :param lang: The language which Twitter should render in for this user. The
        language must be specified by the appropriate two letter ISO 639-1
        representation. Currently supported languages are provided by this
        endpoint.
    """
    binding = {'sleep_time_enabled': sleep_time_enabled, 'start_sleep_time':
               start_sleep_time, 'end_sleep_time': end_sleep_time,
               'time_zone': time_zone, 'trend_location_woeid':
               trend_location_woeid, 'lang': lang}
    url = 'https://api.twitter.com/1.1/account/settings.json'
    return TwitterRequest('POST',
                          url,
                          'rest:account',
                          'post-account-settings',
                          binding)


def update_profile(*, name=ELIDE, url=ELIDE, location=ELIDE,
                   description=ELIDE, profile_link_color=ELIDE,
                   include_entities=ELIDE, skip_status=ELIDE):
    """
    Sets some values that users are able to set under the “Account” tab of
    their settings page. Only the parameters specified will be updated.

    :param name: Full name associated with the profile. Maximum of 20
        characters.

    :param url: URL associated with the profile. Will be prepended with
        “http://” if not present. Maximum of 100 characters.

    :param location: The city or country describing where the user of the
        account is located. The contents are not normalized or geocoded in any
        way. Maximum of 30 characters.

    :param description: A description of the user owning the account. Maximum
        of 160 characters.

    :param profile_link_color: Sets a hex value that controls the color scheme
        of links used on the authenticating user’s profile page on twitter.com.
        This must be a valid hexadecimal value, and may be either three or six
        characters (ex: F00 or FF0000). This parameter replaces the deprecated
        (and separate) update_profile_colors API method.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'name': name, 'url': url, 'location': location, 'description':
               description, 'profile_link_color': profile_link_color,
               'include_entities': include_entities, 'skip_status':
               skip_status}
    url = 'https://api.twitter.com/1.1/account/update_profile.json'
    return TwitterRequest('POST',
                          url,
                          'rest:account',
                          'post-account-update-profile',
                          binding)


def update_profile_background_image(*, image=ELIDE, tile=ELIDE,
                                    include_entities=ELIDE,
                                    skip_status=ELIDE, media_id=ELIDE):
    """
    Updates the authenticating user’s profile background image. This method can
    also be used to enable or disable the profile background image.

    :param image: The background image for the profile, base64-encoded. Must be
        a valid GIF, JPG, or PNG image of less than 800 kilobytes in size.
        Images with width larger than 2048 pixels will be forcibly scaled down.
        The image must be provided as raw multipart data, not a URL.

    :param tile: Whether or not to tile the background image. If set to true, t
        or 1 the background image will be displayed tiled. The image will not
        be tiled otherwise.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.

    :param media_id: Specify the media to use as the background image. More
        information on upload of media is available here.
    """
    binding = {'image': image, 'tile': tile, 'include_entities':
               include_entities, 'skip_status': skip_status, 'media_id':
               media_id}
    url = 'https://api.twitter.com/1.1/account/update_profile_background_image.json'
    return TwitterRequest('POST',
                          url,
                          'rest:account',
                          'post-account-update-profile-background-image',
                          binding)


def update_profile_banner(banner, *, width=ELIDE, height=ELIDE,
                          offset_left=ELIDE, offset_top=ELIDE):
    """
    Uploads a profile banner on behalf of the authenticating user. More
    information about sizing variations can be found in

    :param banner: The Base64-encoded or raw image data being uploaded as the
        user’s new profile banner.

    :param width: The width of the preferred section of the image being
        uploaded in pixels. Use with height, offset_left, and offset_top to
        select the desired region of the image to use.

    :param height: The height of the preferred section of the image being
        uploaded in pixels. Use with width, offset_left, and offset_top to
        select the desired region of the image to use.

    :param offset_left: The number of pixels by which to offset the uploaded
        image from the left. Use with height, width, and offset_top to select
        the desired region of the image to use.

    :param offset_top: The number of pixels by which to offset the uploaded
        image from the top. Use with height, width, and offset_left to select
        the desired region of the image to use.
    """
    binding = {'banner': banner, 'width': width, 'height': height,
               'offset_left': offset_left, 'offset_top': offset_top}
    url = 'https://api.twitter.com/1.1/account/update_profile_banner.json'
    return TwitterRequest('POST',
                          url,
                          'rest:account',
                          'post-account-update-profile-banner',
                          binding)


def update_profile_image(image, *, include_entities=ELIDE, skip_status=ELIDE):
    """
    Updates the authenticating user’s profile image. Note that this method
    expects raw multipart data, not a URL to an image.

    :param image: The avatar image for the profile, base64-encoded. Must be a
        valid GIF, JPG, or PNG image of less than 700 kilobytes in size. Images
        with width larger than 400 pixels will be scaled down. Animated GIFs
        will be converted to a static GIF of the first frame, removing the
        animation.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'image': image, 'include_entities': include_entities,
               'skip_status': skip_status}
    url = 'https://api.twitter.com/1.1/account/update_profile_image.json'
    return TwitterRequest('POST',
                          url,
                          'rest:account',
                          'post-account-update-profile-image',
                          binding)



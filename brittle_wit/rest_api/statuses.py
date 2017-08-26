###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest, ELIDE


def home_timeline(*, count=ELIDE, since_id=ELIDE, max_id=ELIDE,
                  trim_user=ELIDE, exclude_replies=ELIDE,
                  include_entities=ELIDE):
    """
    Returns a collection of the most recent

    :param count: Specifies the number of records to retrieve. Must be less
        than or equal to 200. Defaults to 20. The value of count is best
        thought of as a limit to the number of tweets to return because
        suspended or deleted content is removed after the count has been
        applied.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param exclude_replies: This parameter will prevent replies from appearing
        in the returned timeline. Using exclude_replies with the count
        parameter will mean you will receive up-to count Tweets — this is
        because the count parameter retrieves that many Tweets before filtering
        out retweets and replies.

    :param include_entities: The entities node will not be included when set to
        false.
    """
    binding = {'count': count, 'since_id': since_id, 'max_id': max_id,
               'trim_user': trim_user, 'exclude_replies': exclude_replies,
               'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-home-timeline',
                          binding)


def lookup(id, *, include_entities=ELIDE, trim_user=ELIDE, map=ELIDE,
           include_ext_alt_text=ELIDE):
    """
    Returns fully-hydrated

    :param id: A comma separated list of Tweet IDs, up to 100 are allowed in a
        single request.

    :param include_entities: The entities node that may appear within embedded
        statuses will not be included when set to false.

    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param map: When using the map parameter, Tweets that do not exist or
        cannot be viewed by the current user will still have their key
        represented but with an explicitly null value paired with it

    :param include_ext_alt_text: If alt text has been added to any attached
        media entities, this parameter will return an ext_alt_text value in the
        top-level key for the media entity. If no value has been set, this will
        be returned as null
    """
    binding = {'id': id, 'include_entities': include_entities, 'trim_user':
               trim_user, 'map': map, 'include_ext_alt_text':
               include_ext_alt_text}
    url = 'https://api.twitter.com/1.1/statuses/lookup.json'
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-lookup',
                          binding)


def mentions_timeline(*, count=ELIDE, since_id=ELIDE, max_id=ELIDE,
                      trim_user=ELIDE, include_entities=ELIDE):
    """
    Returns the 20 most recent mentions (Tweets containing a users’s
    @screen_name) for the authenticating user.

    :param count: Specifies the number of Tweets to try and retrieve, up to a
        maximum of 200. The value of count is best thought of as a limit to the
        number of tweets to return because suspended or deleted content is
        removed after the count has been applied. We include retweets in the
        count, even if include_rts is not supplied. It is recommended you
        always send include_rts=1 when using this API method.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param include_entities: The entities node will not be included when set to
        false.
    """
    binding = {'count': count, 'since_id': since_id, 'max_id': max_id,
               'trim_user': trim_user, 'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-mentions-timeline',
                          binding)


def oembed(url, *, maxwidth=ELIDE, hide_media=ELIDE, hide_thread=ELIDE,
           omit_script=ELIDE, align=ELIDE, related=ELIDE, lang=ELIDE,
           theme=ELIDE, link_color=ELIDE, widget_type=ELIDE, dnt=ELIDE):
    """
    Returns a single Tweet, specified by either a Tweet web URL or the Tweet
    ID, in an

    :param url: The URL of the Tweet to be embedded

    :param maxwidth: The maximum width of a rendered Tweet in whole pixels.
        This value must be between 220 and 550 inclusive. A supplied value
        under or over the allowed range will be returned as the minimum or
        maximum supported width respectively; the reset width value will be
        reflected in the returned width property. Note that Twitter does not
        support the oEmbed maxheight parameter. Tweets are fundamentally text,
        and are therefore of unpredictable height that cannot be scaled like an
        image or video. Relatedly, the oEmbed response will not provide a value
        for height. Implementations that need consistent heights for Tweets
        should refer to the hide_thread and hide_media parameters below

    :param hide_media: When set to true, t, or 1 links in a Tweet are not
        expanded to photo, video, or link previews

    :param hide_thread: When set to true, t, or 1 a collapsed version of the
        previous Tweet in a conversation thread will not be displayed when the
        requested Tweet is in reply to another Tweet

    :param omit_script: When set to true, t, or 1 the <script> responsible for
        loading widgets.js will not be returned. Your webpages should include
        their own reference to widgets.js for use across all Twitter widgets
        including Embedded Tweets

    :param align: Specifies whether the embedded Tweet should be floated left,
        right, or center in the page relative to the parent element. Valid
        values are left, right, center, and none

    :param related: A comma-separated list of Twitter usernames related to your
        content. This value will be forwarded to Tweet action intents if a
        viewer chooses to reply, like, or retweet the embedded Tweet

    :param lang: Request returned HTML and a rendered Tweet in the specified
        Twitter language supported by embedded Tweets

    :param theme: When set to dark, the Tweet is displayed with light text over
        a dark background

    :param link_color: Adjust the color of Tweet text links with a hexadecimal
        color value

    :param widget_type: Set to video to return a Twitter Video embed for the
        given Tweet

    :param dnt: When set to true, the Tweet and its embedded page on your site
        are not used for purposes that include personalized suggestions and
        personalized ads
    """
    binding = {'url': url, 'maxwidth': maxwidth, 'hide_media': hide_media,
               'hide_thread': hide_thread, 'omit_script': omit_script,
               'align': align, 'related': related, 'lang': lang, 'theme':
               theme, 'link_color': link_color, 'widget_type': widget_type,
               'dnt': dnt}
    url = 'https://publish.twitter.com/oembed'
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-oembed',
                          binding)


def retweeters_ids(id, *, cursor=ELIDE, stringify_ids=ELIDE):
    """
    Returns a collection of up to 100 user IDs belonging to users who have
    retweeted the Tweet specified by the

    :param id: The numerical ID of the desired status.

    :param cursor: Causes the list of IDs to be broken into pages of no more
        than 100 IDs at a time. The number of IDs returned is not guaranteed to
        be 100 as suspended users are filtered out after connections are
        queried. If no cursor is provided, a value of -1 will be assumed, which
        is the first “page.” The response from the API will include a
        previous_cursor and next_cursor to allow paging back and forth. See our
        cursor docs for more information. While this method supports the cursor
        parameter, the entire result set can be returned in a single cursored
        collection. Using the count parameter with this method will not provide
        segmented cursors for use with this parameter.

    :param stringify_ids: Many programming environments will not consume Tweet
        ids due to their size. Provide this option to have ids returned as
        strings instead.
    """
    binding = {'id': id, 'cursor': cursor, 'stringify_ids': stringify_ids}
    url = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json'
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-retweeters-ids',
                          binding)


def retweets_by_id(id, *, count=ELIDE, trim_user=ELIDE):
    """
    Returns a collection of the 100 most recent retweets of the Tweet specified
    by the

    :param id: The numerical ID of the desired status.

    :param count: Specifies the number of records to retrieve. Must be less
        than or equal to 100.

    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
    """
    binding = {'id': id, 'count': count, 'trim_user': trim_user}
    url = 'https://api.twitter.com/1.1/statuses/retweets/{id}.json'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-retweets-id',
                          binding)


def retweets_of_me(*, count=ELIDE, since_id=ELIDE, max_id=ELIDE,
                   trim_user=ELIDE, include_entities=ELIDE,
                   include_user_entities=ELIDE):
    """
    Returns the most recent Tweets authored by the authenticating user that
    have been retweeted by others. This timeline is a subset of the user’s

    :param count: Specifies the number of records to retrieve. Must be less
        than or equal to 100. If omitted, 20 will be assumed.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param include_entities: The tweet entities node will not be included when
        set to false.

    :param include_user_entities: The user entities node will not be included
        when set to false.
    """
    binding = {'count': count, 'since_id': since_id, 'max_id': max_id,
               'trim_user': trim_user, 'include_entities': include_entities,
               'include_user_entities': include_user_entities}
    url = 'https://api.twitter.com/1.1/statuses/retweets_of_me.json'
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-retweets-of-me',
                          binding)


def show_by_id(id, *, trim_user=ELIDE, include_my_retweet=ELIDE,
               include_entities=ELIDE, include_ext_alt_text=ELIDE):
    """
    Returns a single

    :param id: The numerical ID of the desired Tweet.

    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param include_my_retweet: When set to either true, t or 1, any Tweets
        returned that have been retweeted by the authenticating user will
        include an additional current_user_retweet node, containing the ID of
        the source status for the retweet.

    :param include_entities: The entities node will not be included when set to
        false.

    :param include_ext_alt_text: If alt text has been added to any attached
        media entities, this parameter will return an ext_alt_text value in the
        top-level key for the media entity. If no value has been set, this will
        be returned as null
    """
    binding = {'id': id, 'trim_user': trim_user, 'include_my_retweet':
               include_my_retweet, 'include_entities': include_entities,
               'include_ext_alt_text': include_ext_alt_text}
    url = 'https://api.twitter.com/1.1/statuses/show.json'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-show-id',
                          binding)


def user_timeline(*, user_id=ELIDE, screen_name=ELIDE, since_id=ELIDE,
                  count=ELIDE, max_id=ELIDE, trim_user=ELIDE,
                  exclude_replies=ELIDE, include_rts=ELIDE):
    """
    Returns a collection of the most recent

    :param user_id: The ID of the user for whom to return results.

    :param screen_name: The screen name of the user for whom to return results.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        that can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param count: Specifies the number of Tweets to try and retrieve, up to a
        maximum of 200 per distinct request. The value of count is best thought
        of as a limit to the number of Tweets to return because suspended or
        deleted content is removed after the count has been applied. We include
        retweets in the count, even if include_rts is not supplied. It is
        recommended you always send include_rts=1 when using this API method.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param exclude_replies: This parameter will prevent replies from appearing
        in the returned timeline. Using exclude_replies with the count
        parameter will mean you will receive up-to count tweets — this is
        because the count parameter retrieves that many Tweets before filtering
        out retweets and replies.

    :param include_rts: When set to false, the timeline will strip any native
        retweets (though they will still count toward both the maximal length
        of the timeline and the slice selected by the count parameter). Note:
        If you’re using the trim_user parameter in conjunction with
        include_rts, the retweets will still contain a full user object.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'since_id':
               since_id, 'count': count, 'max_id': max_id, 'trim_user':
               trim_user, 'exclude_replies': exclude_replies, 'include_rts':
               include_rts}
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    return TwitterRequest('GET',
                          url,
                          'rest:statuses',
                          'get-statuses-user-timeline',
                          binding)


def destroy_by_id(id, *, trim_user=ELIDE):
    """
    Destroys the status specified by the required ID parameter. The
    authenticating user must be the author of the specified status. Returns the
    destroyed status if successful.

    :param id: The numerical ID of the desired status.

    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
    """
    binding = {'id': id, 'trim_user': trim_user}
    url = 'https://api.twitter.com/1.1/statuses/destroy/{id}.json'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'rest:statuses',
                          'post-statuses-destroy-id',
                          binding)


def retweet_by_id(id, *, trim_user=ELIDE):
    """
    Retweets a tweet. Returns the

    :param id: The numerical ID of the desired status.

    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
    """
    binding = {'id': id, 'trim_user': trim_user}
    url = 'https://api.twitter.com/1.1/statuses/retweet/{id}.json'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'rest:statuses',
                          'post-statuses-retweet-id',
                          binding)


def unretweet_by_id(id, *, trim_user=ELIDE):
    """
    Untweets a retweeted status. Returns the

    :param id: The numerical ID of the desired status.

    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
    """
    binding = {'id': id, 'trim_user': trim_user}
    url = 'https://api.twitter.com/1.1/statuses/unretweet/{id}.json'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'rest:statuses',
                          'post-statuses-unretweet-id',
                          binding)


def update(status, *, in_reply_to_status_id=ELIDE, possibly_sensitive=ELIDE,
           lat=ELIDE, long=ELIDE, place_id=ELIDE, display_coordinates=ELIDE,
           trim_user=ELIDE, media_ids=ELIDE, enable_dm_commands=ELIDE,
           fail_dm_commands=ELIDE):
    """
    Updates the authenticating user’s current status, also known as Tweeting.

    :param status: The text of the status update, typically up to 140
        characters. URL encode as necessary. t.co link wrapping may affect
        character counts. There are some special commands in this field to be
        aware of. For instance, preceding a message with “D ” or “M ” and
        following it with a screen name can create a Direct Message to that
        user if the relationship allows for it. See the ‘enable_dm_commands’
        parameter for information on disabling Direct Message creation to allow
        any text to be created as a Tweet.

    :param in_reply_to_status_id: The ID of an existing status that the update
        is in reply to. Note: This parameter will be ignored unless the author
        of the Tweet this parameter references is mentioned within the status
        text. Therefore, you must include @username, where username is the
        author of the referenced Tweet, within the update.

    :param possibly_sensitive: If you upload Tweet media that might be
        considered sensitive content such as nudity, violence, or medical
        procedures, you should set this value to true. See Media setting and
        best practices for more context.

    :param lat: The latitude of the location this Tweet refers to. This
        parameter will be ignored unless it is inside the range -90.0 to +90.0
        (North is positive) inclusive. It will also be ignored if there isn’t a
        corresponding long parameter.

    :param long: The longitude of the location this Tweet refers to. The valid
        ranges for longitude is -180.0 to +180.0 (East is positive) inclusive.
        This parameter will be ignored if outside that range, if it is not a
        number, if geo_enabled is disabled, or if there not a corresponding lat
        parameter.

    :param place_id: A place in the world.

    :param display_coordinates: Whether or not to put a pin on the exact
        coordinates a Tweet has been sent from.

    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.

    :param media_ids: A list of media_ids to associate with the Tweet. You may
        include up to 4 photos or 1 animated GIF or 1 video in a Tweet. See
        Uploading Media for further details on uploading media.

    :param enable_dm_commands: When set to true, enables shortcode commands for
        sending Direct Messages as part of the status text to send a Direct
        Message to a user. When set to false, disables this behavior and
        includes any leading characters in the status text that is posted

    :param fail_dm_commands: When set to true, causes any status text that
        starts with shortcode commands to return an API error. When set to
        false, allows shortcode commands to be sent in the status text and
        acted on by the API.
    """
    binding = {'status': status, 'in_reply_to_status_id':
               in_reply_to_status_id, 'possibly_sensitive':
               possibly_sensitive, 'lat': lat, 'long': long, 'place_id':
               place_id, 'display_coordinates': display_coordinates,
               'trim_user': trim_user, 'media_ids': media_ids,
               'enable_dm_commands': enable_dm_commands, 'fail_dm_commands':
               fail_dm_commands}
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    return TwitterRequest('POST',
                          url,
                          'rest:statuses',
                          'post-statuses-update',
                          binding)


def update_with_mediadeprecated(status, media, *, possibly_sensitive=ELIDE,
                                in_reply_to_status_id=ELIDE, lat=ELIDE,
                                long=ELIDE, place_id=ELIDE,
                                display_coordinates=ELIDE,
                                enable_dm_commands=ELIDE,
                                fail_dm_commands=ELIDE):
    """


    :param status: The text of your status update. URL encode as necessary.
        t.co link wrapping may affect character counts if the post contains
        URLs. You must additionally account for the
        characters_reserved_per_media per uploaded media, additionally
        accounting for space characters in between finalized URLs. Note :
        Request the GET help / configuration endpoint to get the current
        characters_reserved_per_media and max_media_per_upload values.

    :param media: Up to max_media_per_upload files may be specified in the
        request, each named media[]. Supported image formats are PNG, JPG and
        GIF, including animated GIFs of up to 3MB. This data must be either the
        raw image bytes or encoded as base64. Note : Request the GET help /
        configuration endpoint to get the current max_media_per_upload and
        photo_size_limit values.

    :param possibly_sensitive: Set to true for content which may not be
        suitable for every audience.

    :param in_reply_to_status_id: The ID of an existing status that the update
        is in reply to. Note : This parameter will be ignored unless the author
        of the Tweet this parameter references is mentioned within the status
        text. Therefore, you must include @username, where username is the
        author of the referenced Tweet, within the update.

    :param lat: The latitude of the location this Tweet refers to. This
        parameter will be ignored unless it is inside the range -90.0 to +90.0
        (North is positive) inclusive. It will also be ignored if there isn’t a
        corresponding long parameter.

    :param long: The longitude of the location this Tweet refers to. The valid
        ranges for longitude is -180.0 to +180.0 (East is positive) inclusive.
        This parameter will be ignored if outside that range, not a number,
        geo_enabled is disabled, or if there not a corresponding lat parameter.

    :param place_id: A place in the world identified by a Twitter place ID.
        Place IDs can be retrieved from geo/reverse_geocode.

    :param display_coordinates: Whether or not to put a pin on the exact
        coordinates a Tweet has been sent from.

    :param enable_dm_commands: When set to true, enables shortcode commands for
        sending Direct Messages as part of the status text to send a Direct
        Message to a user. When set to false, disables this behavior and
        includes any leading characters in the status text.

    :param fail_dm_commands: When set to true, causes any status text that
        starts with shortcode commands to return an API error. When set to
        false, allows shortcode commands to be sent in the status text and
        acted on by the API.
    """
    binding = {'status': status, 'media[]': media, 'possibly_sensitive':
               possibly_sensitive, 'in_reply_to_status_id':
               in_reply_to_status_id, 'lat': lat, 'long': long, 'place_id':
               place_id, 'display_coordinates': display_coordinates,
               'enable_dm_commands': enable_dm_commands, 'fail_dm_commands':
               fail_dm_commands}
    url = 'https://api.twitter.com/1.1/statuses/update_with_media.json'
    return TwitterRequest('POST',
                          url,
                          'rest:statuses',
                          'post-statuses-update-with-media-deprecated',
                          binding)



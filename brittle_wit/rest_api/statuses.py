###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def home_timeline(*, count=IGNORE, since_id=IGNORE, max_id=IGNORE, trim_user=IGNORE, exclude_replies=IGNORE, include_entities=IGNORE):
    """
    Returns a collection of the most recent
    
    :param count: Specifies the number of records to retrieve. Must be less tha
        n or equal to 200. Defaults to 20. The value of count is best thought
        of as a limit to the number of tweets to return because suspended or
        deleted content is removed after the count has been applied. (False)
    
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param exclude_replies: This parameter will prevent replies from appearing 
        in the returned timeline. Using exclude_replies with the count
        parameter will mean you will receive up-to count Tweets — this is
        because the count parameter retrieves that many Tweets before filtering
        out retweets and replies. (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    """
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-HOME-TIMELINE',
                          count=count
                          since_id=since_id
                          max_id=max_id
                          trim_user=trim_user
                          exclude_replies=exclude_replies
                          include_entities=include_entities)


def lookup(id, *, include_entities=IGNORE, trim_user=IGNORE, map=IGNORE, include_ext_alt_text=IGNORE):
    """
    Returns fully-hydrated
    
    :param id: A comma separated list of Tweet IDs, up to 100 are allowed in a 
        single request. (True)
    
    
    :param include_entities: The entities node that may appear within embedded 
        statuses will not be included when set to false. (False)
    
    
    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param map: When using the map parameter, Tweets that do not exist or canno
        t be viewed by the current user will still have their key represented
        but with an explicitly null value paired with it (False)
    
    
    :param include_ext_alt_text: If alt text has been added to any attached med
        ia entities, this parameter will return an ext_alt_text value in the
        top-level key for the media entity. If no value has been set, this will
        be returned as null (False)
    """
    url = "https://api.twitter.com/1.1/statuses/lookup.json"
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-LOOKUP',
                          id=id
                          include_entities=include_entities
                          trim_user=trim_user
                          map=map
                          include_ext_alt_text=include_ext_alt_text)


def mentions_timeline(*, count=IGNORE, since_id=IGNORE, max_id=IGNORE, trim_user=IGNORE, include_entities=IGNORE):
    """
    Returns the 20 most recent mentions (Tweets containing a users's
    @screen_name) for the authenticating user.
    
    :param count: Specifies the number of Tweets to try and retrieve, up to a m
        aximum of 200. The value of count is best thought of as a limit to the
        number of tweets to return because suspended or deleted content is
        removed after the count has been applied. We include retweets in the
        count, even if include_rts is not supplied. It is recommended you
        always send include_rts=1 when using this API method. (False)
    
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    """
    url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-MENTIONS-TIMELINE',
                          count=count
                          since_id=since_id
                          max_id=max_id
                          trim_user=trim_user
                          include_entities=include_entities)


def oembed(url, *, maxwidth=IGNORE, hide_media=IGNORE, hide_thread=IGNORE, omit_script=IGNORE, align=IGNORE, related=IGNORE, lang=IGNORE, theme=IGNORE, link_color=IGNORE, widget_type=IGNORE, dnt=IGNORE):
    """
    Returns a single Tweet, specified by either a Tweet web URL or the Tweet
    ID, in an
    
    :param url: The URL of the Tweet to be embedded (True)
    
    :param maxwidth: The maximum width of a rendered Tweet in whole pixels. Thi
        s value must be between 220 and 550 inclusive. A supplied value under
        or over the allowed range will be returned as the minimum or maximum
        supported width respectively; the reset width value will be reflected
        in the returned width property. Note that Twitter does not support the
        oEmbed maxheight parameter. Tweets are fundamentally text, and are
        therefore of unpredictable height that cannot be scaled like an image
        or video. Relatedly, the oEmbed response will not provide a value for
        height. Implementations that need consistent heights for Tweets should
        refer to the hide_thread and hide_media parameters below (False)
    
    
    :param hide_media: When set to true, t, or 1 links in a Tweet are not expan
        ded to photo, video, or link previews (False)
    
    
    :param hide_thread: When set to true, t, or 1 a collapsed version of the pr
        evious Tweet in a conversation thread will not be displayed when the
        requested Tweet is in reply to another Tweet (False)
    
    
    :param omit_script: When set to true, t, or 1 the <script> responsible for 
        loading widgets.js will not be returned. Your webpages should include
        their own reference to widgets.js for use across all Twitter widgets
        including Embedded Tweets (False)
    
    
    :param align: Specifies whether the embedded Tweet should be floated left, 
        right, or center in the page relative to the parent element. Valid
        values are left, right, center, and none (False)
    
    
    :param related: A comma-separated list of Twitter usernames related to your
        content. This value will be forwarded to Tweet action intents if a
        viewer chooses to reply, like, or retweet the embedded Tweet (False)
    
    
    :param lang: Request returned HTML and a rendered Tweet in the specified Tw
        itter language supported by embedded Tweets (False)
    
    
    :param theme: When set to dark, the Tweet is displayed with light text over
        a dark background (False)
    
    
    :param link_color: Adjust the color of Tweet text links with a hexadecimal 
        color value (False)
    
    
    :param widget_type: Set to video to return a Twitter Video embed for the gi
        ven Tweet (False)
    
    
    :param dnt: When set to true, the Tweet and its embedded page on your site 
        are not used for purposes that include personalized suggestions and
        personalized ads (False)
    """
    url = "https://publish.twitter.com/oembed"
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-OEMBED',
                          url=url
                          maxwidth=maxwidth
                          hide_media=hide_media
                          hide_thread=hide_thread
                          omit_script=omit_script
                          align=align
                          related=related
                          lang=lang
                          theme=theme
                          link_color=link_color
                          widget_type=widget_type
                          dnt=dnt)


def retweeters_ids(id, *, cursor=IGNORE, stringify_ids=IGNORE):
    """
    Returns a collection of up to 100 user IDs belonging to users who have
    retweeted the Tweet specified by the
    
    :param id: The numerical ID of the desired status. (True)
    
    :param cursor: Causes the list of IDs to be broken into pages of no more th
        an 100 IDs at a time. The number of IDs returned is not guaranteed to
        be 100 as suspended users are filtered out after connections are
        queried. If no cursor is provided, a value of -1 will be assumed, which
        is the first “page.” The response from the API will include a
        previous_cursor and next_cursor to allow paging back and forth. See our
        cursor docs for more information. While this method supports the cursor
        parameter, the entire result set can be returned in a single cursored
        collection. Using the count parameter with this method will not provide
        segmented cursors for use with this parameter. (False)
    
    
    :param stringify_ids: Many programming environments will not consume Tweet 
        ids due to their size. Provide this option to have ids returned as
        strings instead. (False)
    """
    url = "https://api.twitter.com/1.1/statuses/retweeters/ids.json"
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-RETWEETERS-IDS',
                          id=id
                          cursor=cursor
                          stringify_ids=stringify_ids)


def retweets_by_id(id, *, count=IGNORE, trim_user=IGNORE):
    """
    Returns a collection of the 100 most recent retweets of the Tweet specified
    by the
    
    :param id: The numerical ID of the desired status. (True)
    
    :param count: Specifies the number of records to retrieve. Must be less tha
        n or equal to 100. (False)
    
    
    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    """
    url = "https://api.twitter.com/1.1/statuses/retweets/{id}.json"
    url = url.format(id=id)
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-RETWEETS-ID',
                          id=id
                          count=count
                          trim_user=trim_user)


def retweets_of_me(*, count=IGNORE, since_id=IGNORE, max_id=IGNORE, trim_user=IGNORE, include_entities=IGNORE, include_user_entities=IGNORE):
    """
    Returns the most recent Tweets authored by the authenticating user that
    have been retweeted by others. This timeline is a subset of the user's
    
    :param count: Specifies the number of records to retrieve. Must be less tha
        n or equal to 100. If omitted, 20 will be assumed. (False)
    
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param include_entities: The tweet entities node will not be included when 
        set to false. (False)
    
    
    :param include_user_entities: The user entities node will not be included w
        hen set to false. (False)
    """
    url = "https://api.twitter.com/1.1/statuses/retweets_of_me.json"
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-RETWEETS-OF-ME',
                          count=count
                          since_id=since_id
                          max_id=max_id
                          trim_user=trim_user
                          include_entities=include_entities
                          include_user_entities=include_user_entities)


def show_by_id(id, *, trim_user=IGNORE, include_my_retweet=IGNORE, include_entities=IGNORE, include_ext_alt_text=IGNORE):
    """
    Returns a single
    
    :param id: The numerical ID of the desired Tweet. (True)
    
    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param include_my_retweet: When set to either true, t or 1, any Tweets retu
        rned that have been retweeted by the authenticating user will include
        an additional current_user_retweet node, containing the ID of the
        source status for the retweet. (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    
    
    :param include_ext_alt_text: If alt text has been added to any attached med
        ia entities, this parameter will return an ext_alt_text value in the
        top-level key for the media entity. If no value has been set, this will
        be returned as null (False)
    """
    url = "https://api.twitter.com/1.1/statuses/show.json"
    url = url.format(id=id)
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-SHOW-ID',
                          id=id
                          trim_user=trim_user
                          include_my_retweet=include_my_retweet
                          include_entities=include_entities
                          include_ext_alt_text=include_ext_alt_text)


def user_timeline(*, user_id=IGNORE, screen_name=IGNORE, since_id=IGNORE, count=IGNORE, max_id=IGNORE, trim_user=IGNORE, exclude_replies=IGNORE, include_rts=IGNORE):
    """
    Returns a collection of the most recent
    
    :param user_id: The ID of the user for whom to return results. (False)
    
    :param screen_name: The screen name of the user for whom to return results.
        (False)
    
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        that can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param count: Specifies the number of Tweets to try and retrieve, up to a m
        aximum of 200 per distinct request. The value of count is best thought
        of as a limit to the number of Tweets to return because suspended or
        deleted content is removed after the count has been applied. We include
        retweets in the count, even if include_rts is not supplied. It is
        recommended you always send include_rts=1 when using this API method.
        (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param exclude_replies: This parameter will prevent replies from appearing 
        in the returned timeline. Using exclude_replies with the count
        parameter will mean you will receive up-to count tweets — this is
        because the count parameter retrieves that many Tweets before filtering
        out retweets and replies. (False)
    
    
    :param include_rts: When set to false, the timeline will strip any native r
        etweets (though they will still count toward both the maximal length of
        the timeline and the slice selected by the count parameter). Note: If
        you're using the trim_user parameter in conjunction with include_rts,
        the retweets will still contain a full user object. (False)
    """
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    return TwitterRequest('GET',
                          url,
                          'REST:STATUSES',
                          'GET-STATUSES-USER-TIMELINE',
                          user_id=user_id
                          screen_name=screen_name
                          since_id=since_id
                          count=count
                          max_id=max_id
                          trim_user=trim_user
                          exclude_replies=exclude_replies
                          include_rts=include_rts)


def destroy_by_id(id, *, trim_user=IGNORE):
    """
    Destroys the status specified by the required ID parameter. The
    authenticating user must be the author of the specified status. Returns the
    destroyed status if successful.
    
    :param id: The numerical ID of the desired status. (True)
    
    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    """
    url = "https://api.twitter.com/1.1/statuses/destroy/{id}.json"
    url = url.format(id=id)
    return TwitterRequest('POST',
                          url,
                          'REST:STATUSES',
                          'POST-STATUSES-DESTROY-ID',
                          id=id
                          trim_user=trim_user)


def retweet_by_id(id, *, trim_user=IGNORE):
    """
    Retweets a tweet. Returns the
    
    :param id: The numerical ID of the desired status. (True)
    
    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    """
    url = "https://api.twitter.com/1.1/statuses/retweet/{id}.json"
    url = url.format(id=id)
    return TwitterRequest('POST',
                          url,
                          'REST:STATUSES',
                          'POST-STATUSES-RETWEET-ID',
                          id=id
                          trim_user=trim_user)


def unretweet_by_id(id, *, trim_user=IGNORE):
    """
    Untweets a retweeted status. Returns the
    
    :param id: The numerical ID of the desired status. (True)
    
    :param trim_user: When set to either true, t or 1, each tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    """
    url = "https://api.twitter.com/1.1/statuses/unretweet/{id}.json"
    url = url.format(id=id)
    return TwitterRequest('POST',
                          url,
                          'REST:STATUSES',
                          'POST-STATUSES-UNRETWEET-ID',
                          id=id
                          trim_user=trim_user)


def update(status, *, in_reply_to_status_id=IGNORE, possibly_sensitive=IGNORE, lat=IGNORE, long=IGNORE, place_id=IGNORE, display_coordinates=IGNORE, trim_user=IGNORE, media_ids=IGNORE, enable_dm_commands=IGNORE, fail_dm_commands=IGNORE):
    """
    Updates the authenticating user's current status, also known as Tweeting.
    
    :param status: The text of the status update, typically up to 140 character
        s. URL encode as necessary. t.co link wrapping may affect character
        counts. There are some special commands in this field to be aware of.
        For instance, preceding a message with “D ” or “M ” and following it
        with a screen name can create a Direct Message to that user if the
        relationship allows for it. See the ‘enable_dm_commands' parameter for
        information on disabling Direct Message creation to allow any text to
        be created as a Tweet. (True)
    
    
    :param in_reply_to_status_id: The ID of an existing status that the update 
        is in reply to. Note: This parameter will be ignored unless the author
        of the Tweet this parameter references is mentioned within the status
        text. Therefore, you must include @username, where username is the
        author of the referenced Tweet, within the update. (False)
    
    
    :param possibly_sensitive: If you upload Tweet media that might be consider
        ed sensitive content such as nudity, violence, or medical procedures,
        you should set this value to true. See Media setting and best practices
        for more context. (False)
    
    
    :param lat: The latitude of the location this Tweet refers to. This paramet
        er will be ignored unless it is inside the range -90.0 to +90.0 (North
        is positive) inclusive. It will also be ignored if there isn't a
        corresponding long parameter. (False)
    
    
    :param long: The longitude of the location this Tweet refers to. The valid 
        ranges for longitude is -180.0 to +180.0 (East is positive) inclusive.
        This parameter will be ignored if outside that range, if it is not a
        number, if geo_enabled is disabled, or if there not a corresponding lat
        parameter. (False)
    
    
    :param place_id: A place in the world. (False)
    
    :param display_coordinates: Whether or not to put a pin on the exact coordi
        nates a Tweet has been sent from. (False)
    
    
    :param trim_user: When set to either true, t or 1, each Tweet returned in a
        timeline will include a user object including only the status authors
        numerical ID. Omit this parameter to receive the complete user object.
        (False)
    
    
    :param media_ids: A list of media_ids to associate with the Tweet. You may 
        include up to 4 photos or 1 animated GIF or 1 video in a Tweet. See
        Uploading Media for further details on uploading media. (False)
    
    
    :param enable_dm_commands: When set to true, enables shortcode commands for
        sending Direct Messages as part of the status text to send a Direct
        Message to a user. When set to false, disables this behavior and
        includes any leading characters in the status text that is posted
        (False)
    
    
    :param fail_dm_commands: When set to true, causes any status text that star
        ts with shortcode commands to return an API error. When set to false,
        allows shortcode commands to be sent in the status text and acted on by
        the API. (False)
    """
    url = "https://api.twitter.com/1.1/statuses/update.json"
    return TwitterRequest('POST',
                          url,
                          'REST:STATUSES',
                          'POST-STATUSES-UPDATE',
                          status=status
                          in_reply_to_status_id=in_reply_to_status_id
                          possibly_sensitive=possibly_sensitive
                          lat=lat
                          long=long
                          place_id=place_id
                          display_coordinates=display_coordinates
                          trim_user=trim_user
                          media_ids=media_ids
                          enable_dm_commands=enable_dm_commands
                          fail_dm_commands=fail_dm_commands)


def update_with_media (deprecated)(status, media[], *, possibly_sensitive=IGNORE, in_reply_to_status_id=IGNORE, lat=IGNORE, long=IGNORE, place_id=IGNORE, display_coordinates=IGNORE, enable_dm_commands=IGNORE, fail_dm_commands=IGNORE):
    """
    :param status: The text of your status update. URL encode as necessary. t.c
        o link wrapping may affect character counts if the post contains URLs.
        You must additionally account for the characters_reserved_per_media per
        uploaded media, additionally accounting for space characters in between
        finalized URLs. Note : Request the GET help / configuration endpoint to
        get the current characters_reserved_per_media and max_media_per_upload
        values. (True)
    
    
    :param media[]: Up to max_media_per_upload files may be specified in the re
        quest, each named media[]. Supported image formats are PNG, JPG and
        GIF, including animated GIFs of up to 3MB. This data must be either the
        raw image bytes or encoded as base64. Note : Request the GET help /
        configuration endpoint to get the current max_media_per_upload and
        photo_size_limit values. (True)
    
    
    :param possibly_sensitive: Set to true for content which may not be suitabl
        e for every audience. (False)
    
    
    :param in_reply_to_status_id: The ID of an existing status that the update 
        is in reply to. Note : This parameter will be ignored unless the author
        of the Tweet this parameter references is mentioned within the status
        text. Therefore, you must include @username, where username is the
        author of the referenced Tweet, within the update. (False)
    
    
    :param lat: The latitude of the location this Tweet refers to. This paramet
        er will be ignored unless it is inside the range -90.0 to +90.0 (North
        is positive) inclusive. It will also be ignored if there isn't a
        corresponding long parameter. (False)
    
    
    :param long: The longitude of the location this Tweet refers to. The valid 
        ranges for longitude is -180.0 to +180.0 (East is positive) inclusive.
        This parameter will be ignored if outside that range, not a number,
        geo_enabled is disabled, or if there not a corresponding lat parameter.
        (False)
    
    
    :param place_id: A place in the world identified by a Twitter place ID. Pla
        ce IDs can be retrieved from geo/reverse_geocode. (False)
    
    
    :param display_coordinates: Whether or not to put a pin on the exact coordi
        nates a Tweet has been sent from. (False)
    
    
    :param enable_dm_commands: When set to true, enables shortcode commands for
        sending Direct Messages as part of the status text to send a Direct
        Message to a user. When set to false, disables this behavior and
        includes any leading characters in the status text. (False)
    
    
    :param fail_dm_commands: When set to true, causes any status text that star
        ts with shortcode commands to return an API error. When set to false,
        allows shortcode commands to be sent in the status text and acted on by
        the API. (False)
    """
    url = "https://api.twitter.com/1.1/statuses/update_with_media.json"
    return TwitterRequest('POST',
                          url,
                          'REST:STATUSES',
                          'POST-STATUSES-UPDATE-WITH-MEDIA-DEPRECATED',
                          status=status
                          media[]=media[]
                          possibly_sensitive=possibly_sensitive
                          in_reply_to_status_id=in_reply_to_status_id
                          lat=lat
                          long=long
                          place_id=place_id
                          display_coordinates=display_coordinates
                          enable_dm_commands=enable_dm_commands
                          fail_dm_commands=fail_dm_commands)



###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def user(*, delimited=ELIDE, stall_warnings=ELIDE, with_=ELIDE,
         replies=ELIDE, track=ELIDE, locations=ELIDE,
         stringify_friend_ids=ELIDE):
    """
    Streams messages for a single user, as described in

    :param delimited: Specifies whether messages should be length-delimited.
        See delimited for more information.

    :param stall_warnings: Specifies whether stall warnings should be
        delivered. See stall_warnings for more information.

    :param with_: Specifies whether to return information for just the
        authenticating user, or include messages from accounts the user
        follows. See with the with parameter documentation for more
        information.

    :param replies: Specifies whether to return additional @replies. See
        replies for more information.

    :param track: Includes additional Tweets matching the specified keywords.
        Phrases of keywords are specified by a comma-separated list. See track
        the track parameter documentation for more information.

    :param locations: Includes additional Tweets falling within the specified
        bounding boxes. See locations for more information.

    :param stringify_friend_ids: Specifies whether to send the Friend List
        preamble as an array of integers or an array of strings. See
        stringify_friends_id for more information.
    """
    binding = {'delimited': delimited, 'stall_warnings': stall_warnings,
               'with': with_, 'replies': replies, 'track': track, 'locations':
               locations, 'stringify_friend_ids': stringify_friend_ids}
    url = 'https://userstream.twitter.com/1.1/user.json'
    return TwitterRequest('GET',
                          url,
                          'streaming:user',
                          'get-user',
                          binding)



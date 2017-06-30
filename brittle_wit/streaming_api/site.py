###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def site(follow, *, delimited=ELIDE, stall_warnings=ELIDE, with_=ELIDE,
         replies=ELIDE, stringify_friend_ids=ELIDE):
    """
    Streams messages for a set of users, as described in

    :param follow: A comma separated list of user IDs, indicating the users to
        return statuses for in the stream. See follow for more information.

    :param delimited: Specifies whether messages should be length-delimited.
        See delimited for more information.

    :param stall_warnings: Specifies whether stall warnings should be
        delivered. See stall_warnings for more information.

    :param with_: Specifies whether to return information for just the users
        specified in the follow parameter, or include messages from accounts
        they follow. See with

    :param replies: Specifies whether to return additional @replies. See
        replies for more information.

    :param stringify_friend_ids: Specifies whether to send the friends lists
        preamble as an array of integers or an array of strings. See
        stringify_friend_id for more information.
    """
    binding = {'follow': follow, 'delimited': delimited, 'stall_warnings':
               stall_warnings, 'with': with_, 'replies': replies,
               'stringify_friend_ids': stringify_friend_ids}
    url = 'https://sitestream.twitter.com/1.1/site.json'
    return TwitterRequest('GET',
                          url,
                          'streaming:site',
                          'get-site',
                          binding)



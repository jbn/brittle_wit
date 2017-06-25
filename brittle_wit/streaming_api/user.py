###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def user(*, delimited=IGNORE, stall_warnings=IGNORE, with=IGNORE, replies=IGNORE, track=IGNORE, locations=IGNORE, stringify_friend_ids=IGNORE):
    """
    Streams messages for a single user, as described in
    
    :param delimited: Specifies whether messages should be length-delimited. Se
        e delimited for more information. (False)
    
    
    :param stall_warnings: Specifies whether stall warnings should be delivered
        . See stall_warnings for more information. (False)
    
    
    :param with: Specifies whether to return information for just the authentic
        ating user, or include messages from accounts the user follows. See
        with the with parameter documentation for more information. (False)
    
    
    :param replies: Specifies whether to return additional @replies. See replie
        s for more information. (False)
    
    
    :param track: Includes additional Tweets matching the specified keywords. P
        hrases of keywords are specified by a comma-separated list. See track
        the track parameter documentation for more information. (False)
    
    
    :param locations: Includes additional Tweets falling within the specified b
        ounding boxes. See locations for more information. (False)
    
    
    :param stringify_friend_ids: Specifies whether to send the Friend List prea
        mble as an array of integers or an array of strings. See
        stringify_friends_id for more information. (False)
    """
    url = "https://userstream.twitter.com/1.1/user.json"
    return TwitterRequest('GET',
                          url,
                          'STREAMING:USER',
                          'GET-USER',
                          delimited=delimited
                          stall_warnings=stall_warnings
                          with=with
                          replies=replies
                          track=track
                          locations=locations
                          stringify_friend_ids=stringify_friend_ids)



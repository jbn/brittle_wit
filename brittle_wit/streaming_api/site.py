###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def site(follow, *, delimited=IGNORE, stall_warnings=IGNORE, with=IGNORE, replies=IGNORE, stringify_friend_ids=IGNORE):
    """
    Streams messages for a set of users, as described in
    
    :param follow: A comma separated list of user IDs, indicating the users to 
        return statuses for in the stream. See follow for more information.
        (True)
    
    
    :param delimited: Specifies whether messages should be length-delimited. Se
        e delimited for more information. (False)
    
    
    :param stall_warnings: Specifies whether stall warnings should be delivered
        . See stall_warnings for more information. (False)
    
    
    :param with: Specifies whether to return information for just the users spe
        cified in the follow parameter, or include messages from accounts they
        follow. See with (False)
    
    
    :param replies: Specifies whether to return additional @replies. See replie
        s for more information. (False)
    
    
    :param stringify_friend_ids: Specifies whether to send the friends lists pr
        eamble as an array of integers or an array of strings. See
        stringify_friend_id for more information. (False)
    """
    url = "https://sitestream.twitter.com/1.1/site.json"
    return TwitterRequest('GET',
                          url,
                          'STREAMING:SITE',
                          'GET-SITE',
                          follow=follow
                          delimited=delimited
                          stall_warnings=stall_warnings
                          with=with
                          replies=replies
                          stringify_friend_ids=stringify_friend_ids)



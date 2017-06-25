###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def ids(*, user_id=IGNORE, screen_name=IGNORE, cursor=IGNORE, stringify_ids=IGNORE, count=IGNORE):
    """
    Returns a cursored collection of user IDs for every user following the
    specified user.
    
    :param user_id: The ID of the user for whom to return results for. (False)
    
    :param screen_name: The screen name of the user for whom to return results 
        for. (False)
    
    
    :param cursor: Causes the list of connections to be broken into pages of no
        more than 5000 IDs at a time. The number of IDs returned is not
        guaranteed to be 5000 as suspended users are filtered out after
        connections are queried. If no cursor is provided, a value of -1 will
        be assumed, which is the first “page.” The response from the API will
        include a previous_cursor and next_cursor to allow paging back and
        forth. See Using cursors to navigate collections for more information.
        (False)
    
    
    :param stringify_ids: Many programming environments will not consume our Tw
        eet ids due to their size. Provide this option to have ids returned as
        strings instead. More about [node:194]. (False)
    
    
    :param count: Specifies the number of IDs attempt retrieval of, up to a max
        imum of 5,000 per distinct request. The value of count is best thought
        of as a limit to the number of results to return. When using the count
        parameter with this method, it is wise to use a consistent count value
        across all requests to the same user's collection. Usage of this
        parameter is encouraged in environments where all 5,000 IDs constitutes
        too large of a response. (False)
    """
    url = "https://api.twitter.com/1.1/followers/ids.json"
    return TwitterRequest('GET',
                          url,
                          'REST:FOLLOWERS',
                          'GET-FOLLOWERS-IDS',
                          user_id=user_id
                          screen_name=screen_name
                          cursor=cursor
                          stringify_ids=stringify_ids
                          count=count)


def list(*, user_id=IGNORE, screen_name=IGNORE, cursor=IGNORE, count=IGNORE, skip_status=IGNORE, include_user_entities=IGNORE):
    """
    Returns a cursored collection of user objects for users following the
    specified user.
    
    :param user_id: The ID of the user for whom to return results for. (False)
    
    :param screen_name: The screen name of the user for whom to return results 
        for. (False)
    
    
    :param cursor: Causes the results to be broken into pages. If no cursor is 
        provided, a value of -1 will be assumed, which is the first “page.” The
        response from the API will include a previous_cursor and next_cursor to
        allow paging back and forth. See Using cursors to navigate collections
        for more information. (False)
    
    
    :param count: The number of users to return per page, up to a maximum of 20
        0. Defaults to 20. (False)
    
    
    :param skip_status: When set to either true, t or 1, statuses will not be i
        ncluded in the returned user objects. If set to any other value,
        statuses will be included. (False)
    
    
    :param include_user_entities: The user object entities node will not be inc
        luded when set to false. (False)
    """
    url = "https://api.twitter.com/1.1/followers/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:FOLLOWERS',
                          'GET-FOLLOWERS-LIST',
                          user_id=user_id
                          screen_name=screen_name
                          cursor=cursor
                          count=count
                          skip_status=skip_status
                          include_user_entities=include_user_entities)



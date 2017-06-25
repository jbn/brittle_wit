###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def ids(*, stringify_ids=IGNORE, cursor=IGNORE):
    """
    Returns an array of numeric user ids the authenticating user is blocking.
    
    :param stringify_ids: Many programming environments will not consume our id
        s due to their size. Provide this option to have ids returned as
        strings instead. Read more about Twitter IDs. (False)
    
    
    :param cursor: Causes the list of IDs to be broken into pages of no more th
        an 5000 IDs at a time. The number of IDs returned is not guaranteed to
        be 5000 as suspended users are filtered out after connections are
        queried. If no cursor is provided, a value of -1 will be assumed, which
        is the first “page.” The response from the API will include a
        previous_cursor and next_cursor to allow paging back and forth. See
        Using cursors to navigate collections for more information. (False)
    """
    url = "https://api.twitter.com/1.1/blocks/ids.json"
    return TwitterRequest('GET',
                          url,
                          'REST:BLOCKS',
                          'GET-BLOCKS-IDS',
                          stringify_ids=stringify_ids
                          cursor=cursor)


def list(*, include_entities=IGNORE, skip_status=IGNORE, cursor=IGNORE):
    """
    Returns a collection of
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    
    
    :param cursor: Causes the list of blocked users to be broken into pages of 
        no more than 5000 IDs at a time. The number of IDs returned is not
        guaranteed to be 5000 as suspended users are filtered out after
        connections are queried. If no cursor is provided, a value of -1 will
        be assumed, which is the first “page.” The response from the API will
        include a previous_cursor and next_cursor to allow paging back and
        forth. See Using cursors to navigate collections for more information.
        (False)
    """
    url = "https://api.twitter.com/1.1/blocks/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:BLOCKS',
                          'GET-BLOCKS-LIST',
                          include_entities=include_entities
                          skip_status=skip_status
                          cursor=cursor)


def create(*, screen_name=IGNORE, user_id=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Blocks the specified user from following the authenticating user. In
    addition the blocked user will not show in the authenticating users
    mentions or timeline (unless retweeted by another user). If a follow or
    friend relationship exists it is destroyed.
    
    :param screen_name: The screen name of the potentially blocked user. Helpfu
        l for disambiguating when a valid screen name is also a user ID.
        (False)
    
    
    :param user_id: The ID of the potentially blocked user. Helpful for disambi
        guating when a valid user ID is also a valid screen name. (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    """
    url = "https://api.twitter.com/1.1/blocks/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:BLOCKS',
                          'POST-BLOCKS-CREATE',
                          screen_name=screen_name
                          user_id=user_id
                          include_entities=include_entities
                          skip_status=skip_status)


def destroy(*, screen_name=IGNORE, user_id=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Un-blocks the user specified in the ID parameter for the authenticating
    user. Returns the un-blocked user in the requested format when successful.
    If relationships existed before the block was instated, they will not be
    restored.
    
    :param screen_name: The screen name of the potentially blocked user. Helpfu
        l for disambiguating when a valid screen name is also a user ID.
        (False)
    
    
    :param user_id: The ID of the potentially blocked user. Helpful for disambi
        guating when a valid user ID is also a valid screen name. (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    """
    url = "https://api.twitter.com/1.1/blocks/destroy.json"
    return TwitterRequest('POST',
                          url,
                          'REST:BLOCKS',
                          'POST-BLOCKS-DESTROY',
                          screen_name=screen_name
                          user_id=user_id
                          include_entities=include_entities
                          skip_status=skip_status)



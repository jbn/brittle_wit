###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def list(*, user_id=IGNORE, screen_name=IGNORE, reverse=IGNORE):
    """
    Returns all lists the authenticating or specified user subscribes to,
    including their own. The user is specified using the
    
    :param user_id: The ID of the user for whom to return results. Helpful for 
        disambiguating when a valid user ID is also a valid screen name. Note:
        : Specifies the ID of the user to get lists from. Helpful for
        disambiguating when a valid user ID is also a valid screen name.
        (False)
    
    
    :param screen_name: The screen name of the user for whom to return results.
        Helpful for disambiguating when a valid screen name is also a user ID.
        (False)
    
    
    :param reverse: Set this to true if you would like owned lists to be return
        ed first. See description above for information on how this parameter
        works. (False)
    """
    url = "https://api.twitter.com/1.1/lists/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-LIST',
                          user_id=user_id
                          screen_name=screen_name
                          reverse=reverse)


def members(list_id, slug, *, owner_screen_name=IGNORE, owner_id=IGNORE, count=IGNORE, cursor=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Returns the members of the specified list. Private list members will only
    be shown if the authenticated user owns the specified list.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    
    
    :param count: Specifies the number of results to return per page (see curso
        r below). The default is 20, with a maximum of 5,000. (False)
    
    
    :param cursor: Causes the collection of list members to be broken into “pag
        es” of consistent sizes (specified by the count parameter). If no
        cursor is provided, a value of -1 will be assumed, which is the first
        “page.” The response from the API will include a previous_cursor and
        next_cursor to allow paging back and forth. See Using cursors to
        navigate collections for more information. (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    """
    url = "https://api.twitter.com/1.1/lists/members.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-MEMBERS',
                          list_id=list_id
                          slug=slug
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id
                          count=count
                          cursor=cursor
                          include_entities=include_entities
                          skip_status=skip_status)


def members_show(list_id, slug, user_id, screen_name, *, owner_screen_name=IGNORE, owner_id=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Check if the specified user is a member of the specified list.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param user_id: The ID of the user for whom to return results for. Helpful 
        for disambiguating when a valid user ID is also a valid screen name.
        (True)
    
    
    :param screen_name: The screen name of the user for whom to return results 
        for. Helpful for disambiguating when a valid screen name is also a user
        ID. (True)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    
    
    :param include_entities: When set to either true, t or 1, each tweet will i
        nclude a node called “entities”. This node offers a variety of metadata
        about the tweet in a discreet structure, including: user_mentions,
        urls, and hashtags. While entities are opt-in on timelines at present,
        they will be made a default component of output in the future. See
        Tweet Entities for more details. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    """
    url = "https://api.twitter.com/1.1/lists/members/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-MEMBERS-SHOW',
                          list_id=list_id
                          slug=slug
                          user_id=user_id
                          screen_name=screen_name
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id
                          include_entities=include_entities
                          skip_status=skip_status)


def memberships(*, user_id=IGNORE, screen_name=IGNORE, count=IGNORE, cursor=IGNORE, filter_to_owned_lists=IGNORE):
    """
    Returns the lists the specified user has been added to. If
    
    :param user_id: The ID of the user for whom to return results for. Helpful 
        for disambiguating when a valid user ID is also a valid screen name.
        (False)
    
    
    :param screen_name: The screen name of the user for whom to return results 
        for. Helpful for disambiguating when a valid screen name is also a user
        ID. (False)
    
    
    :param count: The amount of results to return per page. Defaults to 20. No 
        more than 1000 results will ever be returned in a single page. (False)
    
    
    :param cursor: Breaks the results into pages. Provide a value of -1 to begi
        n paging. Provide values as returned in the response body's next_cursor
        and previous_cursor attributes to page back and forth in the list. It
        is recommended to always use cursors when the method supports them. See
        [node:10362] for more information. (False)
    
    
    :param filter_to_owned_lists: When set to true, t or 1, will return just li
        sts the authenticating user owns, and the user represented by user_id
        or screen_name is a member of. (False)
    """
    url = "https://api.twitter.com/1.1/lists/memberships.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-MEMBERSHIPS',
                          user_id=user_id
                          screen_name=screen_name
                          count=count
                          cursor=cursor
                          filter_to_owned_lists=filter_to_owned_lists)


def ownerships(*, user_id=IGNORE, screen_name=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Returns the lists owned by the specified Twitter user. Private lists will
    only be shown if the authenticated user is also the owner of the lists.
    
    :param user_id: The ID of the user for whom to return results for. (False)
    
    :param screen_name: The screen name of the user for whom to return results 
        for. (False)
    
    
    :param count: The amount of results to return per page. Defaults to 20. No 
        more than 1000 results will ever be returned in a single page. (False)
    
    
    :param cursor: Breaks the results into pages. Provide a value of -1 to begi
        n paging. Provide values as returned in the response body's next_cursor
        and previous_cursor attributes to page back and forth in the list. It
        is recommended to always use cursors when the method supports them. See
        [node:10362] for more information. (False)
    """
    url = "https://api.twitter.com/1.1/lists/ownerships.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-OWNERSHIPS',
                          user_id=user_id
                          screen_name=screen_name
                          count=count
                          cursor=cursor)


def show(list_id, slug, *, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Returns the specified list. Private lists will only be shown if the
    authenticated user owns the specified list.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    """
    url = "https://api.twitter.com/1.1/lists/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-SHOW',
                          list_id=list_id
                          slug=slug
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id)


def statuses(list_id, slug, *, owner_screen_name=IGNORE, owner_id=IGNORE, since_id=IGNORE, max_id=IGNORE, count=IGNORE, include_entities=IGNORE, include_rts=IGNORE):
    """
    Returns a timeline of tweets authored by members of the specified list.
    Retweets are included by default. Use the
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param count: Specifies the number of results to retrieve per “page.” (Fals
        e)
    
    
    :param include_entities: Entities are ON by default in API 1.1, each tweet 
        includes a node called “entities”. This node offers a variety of
        metadata about the tweet in a discreet structure, including:
        user_mentions, urls, and hashtags. You can omit entities from the
        result by using include_entities=false (False)
    
    
    :param include_rts: When set to either true, t or 1, the list timeline will
        contain native retweets (if they exist) in addition to the standard
        stream of tweets. The output format of retweeted tweets is identical to
        the representation you see in home_timeline. (False)
    """
    url = "https://api.twitter.com/1.1/lists/statuses.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-STATUSES',
                          list_id=list_id
                          slug=slug
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id
                          since_id=since_id
                          max_id=max_id
                          count=count
                          include_entities=include_entities
                          include_rts=include_rts)


def subscribers(list_id, slug, *, owner_screen_name=IGNORE, owner_id=IGNORE, count=IGNORE, cursor=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Returns the subscribers of the specified list. Private list subscribers
    will only be shown if the authenticated user owns the specified list.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    
    
    :param count: Specifies the number of results to return per page (see curso
        r below). The default is 20, with a maximum of 5,000. (False)
    
    
    :param cursor: Breaks the results into pages. A single page contains 20 lis
        ts. Provide a value of -1 to begin paging. Provide values as returned
        in the response body's next_cursor and previous_cursor attributes to
        page back and forth in the list. See Using cursors to navigate
        collections for more information. (False)
    
    
    :param include_entities: When set to either true, t or 1, each tweet will i
        nclude a node called “entities”. This node offers a variety of metadata
        about the tweet in a discreet structure, including: user_mentions,
        urls, and hashtags. While entities are opt-in on timelines at present,
        they will be made a default component of output in the future. See
        Tweet Entities for more details. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    """
    url = "https://api.twitter.com/1.1/lists/subscribers.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-SUBSCRIBERS',
                          list_id=list_id
                          slug=slug
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id
                          count=count
                          cursor=cursor
                          include_entities=include_entities
                          skip_status=skip_status)


def subscribers_show(list_id, slug, user_id, screen_name, *, owner_screen_name=IGNORE, owner_id=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Check if the specified user is a subscriber of the specified list. Returns
    the user if they are subscriber.
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param user_id: The ID of the user for whom to return results for. Helpful 
        for disambiguating when a valid user ID is also a valid screen name.
        (True)
    
    
    :param screen_name: The screen name of the user for whom to return results 
        for. Helpful for disambiguating when a valid screen name is also a user
        ID. (True)
    
    
    :param include_entities: When set to either true, t or 1, each tweet will i
        nclude a node called “entities”. This node offers a variety of metadata
        about the tweet in a discreet structure, including: user_mentions,
        urls, and hashtags. While entities are opt-in on timelines at present,
        they will be made a default component of output in the future. See
        Tweet Entities for more details. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    """
    url = "https://api.twitter.com/1.1/lists/subscribers/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-SUBSCRIBERS-SHOW',
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id
                          list_id=list_id
                          slug=slug
                          user_id=user_id
                          screen_name=screen_name
                          include_entities=include_entities
                          skip_status=skip_status)


def subscriptions(*, user_id=IGNORE, screen_name=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Obtain a collection of the lists the specified user is subscribed to, 20
    lists per page by default. Does not include the user's own lists.
    
    :param user_id: The ID of the user for whom to return results for. Helpful 
        for disambiguating when a valid user ID is also a valid screen name.
        (False)
    
    
    :param screen_name: The screen name of the user for whom to return results 
        for. Helpful for disambiguating when a valid screen name is also a user
        ID. (False)
    
    
    :param count: The amount of results to return per page. Defaults to 20. No 
        more than 1000 results will ever be returned in a single page. (False)
    
    
    :param cursor: Breaks the results into pages. Provide a value of -1 to begi
        n paging. Provide values as returned in the response body's next_cursor
        and previous_cursor attributes to page back and forth in the list. It
        is recommended to always use cursors when the method supports them. See
        [node:10362] for more information. (False)
    """
    url = "https://api.twitter.com/1.1/lists/subscriptions.json"
    return TwitterRequest('GET',
                          url,
                          'REST:LISTS',
                          'GET-LISTS-SUBSCRIPTIONS',
                          user_id=user_id
                          screen_name=screen_name
                          count=count
                          cursor=cursor)


def create(name, *, mode=IGNORE, description=IGNORE):
    """
    Creates a new list for the authenticated user. Note that you can create up
    to 1000 lists per account.
    
    :param name: The name for the list. A list's name must start with a letter 
        and can consist only of 25 or fewer letters, numbers, “-”, or “_”
        characters. (True)
    
    
    :param mode: Whether your list is public or private. Values can be public o
        r private. If no mode is specified the list will be public. (False)
    
    
    :param description: The description to give the list. (False)
    """
    url = "https://api.twitter.com/1.1/lists/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-CREATE',
                          name=name
                          mode=mode
                          description=description)


def destroy(list_id, slug, *, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Deletes the specified list. The authenticated user must own the list to be
    able to destroy it.
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    """
    url = "https://api.twitter.com/1.1/lists/destroy.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-DESTROY',
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id
                          list_id=list_id
                          slug=slug)


def members_create(list_id, slug, user_id, screen_name, *, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Add a member to a list. The authenticated user must own the list to be able
    to add members to it. Note that lists cannot have more than 5,000 members.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param user_id: The ID of the user for whom to return results for. Helpful 
        for disambiguating when a valid user ID is also a valid screen name.
        (True)
    
    
    :param screen_name: The screen name of the user for whom to return results 
        for. Helpful for disambiguating when a valid screen name is also a user
        ID. (True)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    """
    url = "https://api.twitter.com/1.1/lists/members/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-MEMBERS-CREATE',
                          list_id=list_id
                          slug=slug
                          user_id=user_id
                          screen_name=screen_name
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id)


def members_create_all(list_id, slug, *, user_id=IGNORE, screen_name=IGNORE, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Adds multiple members to a list, by specifying a comma-separated list of
    member ids or screen names. The authenticated user must own the list to be
    able to add members to it. Note that lists can't have more than 5,000
    members, and you are limited to adding up to 100 members to a list at a
    time with this method.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param user_id: A comma separated list of user IDs, up to 100 are allowed i
        n a single request. (False)
    
    
    :param screen_name: A comma separated list of screen names, up to 100 are a
        llowed in a single request. (False)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    """
    url = "https://api.twitter.com/1.1/lists/members/create_all.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-MEMBERS-CREATE-ALL',
                          list_id=list_id
                          slug=slug
                          user_id=user_id
                          screen_name=screen_name
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id)


def members_destroy(*, list_id=IGNORE, slug=IGNORE, user_id=IGNORE, screen_name=IGNORE, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Removes the specified member from the list. The authenticated user must be
    the list's owner to remove members from the list.
    
    :param list_id: The numerical id of the list. (False)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (False)
    
    
    :param user_id: The ID of the user to remove from the list. Helpful for dis
        ambiguating when a valid user ID is also a valid screen name. (False)
    
    
    :param screen_name: The screen name of the user for whom to remove from the
        list. Helpful for disambiguating when a valid screen name is also a
        user ID. (False)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    """
    url = "https://api.twitter.com/1.1/lists/members/destroy.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-MEMBERS-DESTROY',
                          list_id=list_id
                          slug=slug
                          user_id=user_id
                          screen_name=screen_name
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id)


def members_destroy_all(list_id, slug, *, user_id=IGNORE, screen_name=IGNORE, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Removes multiple members from a list, by specifying a comma-separated list
    of member ids or screen names. The authenticated user must own the list to
    be able to remove members from it. Note that lists can't have more than 500
    members, and you are limited to removing up to 100 members to a list at a
    time with this method.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param user_id: A comma separated list of user IDs, up to 100 are allowed i
        n a single request. (False)
    
    
    :param screen_name: A comma separated list of screen names, up to 100 are a
        llowed in a single request. (False)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    """
    url = "https://api.twitter.com/1.1/lists/members/destroy_all.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-MEMBERS-DESTROY-ALL',
                          list_id=list_id
                          slug=slug
                          user_id=user_id
                          screen_name=screen_name
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id)


def subscribers_create(list_id, slug, *, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Subscribes the authenticated user to the specified list.
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    """
    url = "https://api.twitter.com/1.1/lists/subscribers/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-SUBSCRIBERS-CREATE',
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id
                          list_id=list_id
                          slug=slug)


def subscribers_destroy(list_id, slug, *, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Unsubscribes the authenticated user from the specified list.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    """
    url = "https://api.twitter.com/1.1/lists/subscribers/destroy.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-SUBSCRIBERS-DESTROY',
                          list_id=list_id
                          slug=slug
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id)


def update(list_id, slug, *, name=IGNORE, mode=IGNORE, description=IGNORE, owner_screen_name=IGNORE, owner_id=IGNORE):
    """
    Updates the specified list. The authenticated user must own the list to be
    able to update it.
    
    :param list_id: The numerical id of the list. (True)
    
    :param slug: You can identify a list by its slug instead of its numerical i
        d. If you decide to do so, note that you'll also have to specify the
        list owner using the owner_id or owner_screen_name parameters. (True)
    
    
    :param name: The name for the list. (False)
    
    :param mode: Whether your list is public or private. Values can be public o
        r private. If no mode is specified the list will be public. (False)
    
    
    :param description: The description to give the list. (False)
    
    :param owner_screen_name: The screen name of the user who owns the list bei
        ng requested by a slug. (False)
    
    
    :param owner_id: The user ID of the user who owns the list being requested 
        by a slug. (False)
    """
    url = "https://api.twitter.com/1.1/lists/update.json"
    return TwitterRequest('POST',
                          url,
                          'REST:LISTS',
                          'POST-LISTS-UPDATE',
                          list_id=list_id
                          slug=slug
                          name=name
                          mode=mode
                          description=description
                          owner_screen_name=owner_screen_name
                          owner_id=owner_id)



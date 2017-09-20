###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def list(*, user_id=_ELIDE, screen_name=_ELIDE, reverse=_ELIDE):
    """
    Returns all lists the authenticating or specified user subscribes to,
    including their own. The user is specified using the

    :param user_id: The ID of the user for whom to return results. Helpful for
        disambiguating when a valid user ID is also a valid screen name. Note:
        : Specifies the ID of the user to get lists from. Helpful for
        disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to return results.
        Helpful for disambiguating when a valid screen name is also a user ID.

    :param reverse: Set this to true if you would like owned lists to be
        returned first. See description above for information on how this
        parameter works.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'reverse':
               reverse}
    url = 'https://api.twitter.com/1.1/lists/list.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-list',
                           binding)


def members(list_id, slug, *, owner_screen_name=_ELIDE, owner_id=_ELIDE,
            count=_ELIDE, cursor=_ELIDE, include_entities=_ELIDE,
            skip_status=_ELIDE):
    """
    Returns the members of the specified list. Private list members will only
    be shown if the authenticated user owns the specified list.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.

    :param count: Specifies the number of results to return per page (see
        cursor below). The default is 20, with a maximum of 5,000.

    :param cursor: Causes the collection of list members to be broken into
        “pages” of consistent sizes (specified by the count parameter). If no
        cursor is provided, a value of -1 will be assumed, which is the first
        “page.” The response from the API will include a previous_cursor and
        next_cursor to allow paging back and forth. See Using cursors to
        navigate collections for more information.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'list_id': list_id, 'slug': slug, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id, 'count': count,
               'cursor': cursor, 'include_entities': include_entities,
               'skip_status': skip_status}
    url = 'https://api.twitter.com/1.1/lists/members.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-members',
                           binding)


def members_show(list_id, slug, user_id, screen_name, *,
                 owner_screen_name=_ELIDE, owner_id=_ELIDE,
                 include_entities=_ELIDE, skip_status=_ELIDE):
    """
    Check if the specified user is a member of the specified list.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param user_id: The ID of the user for whom to return results for. Helpful
        for disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to return results
        for. Helpful for disambiguating when a valid screen name is also a user
        ID.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.

    :param include_entities: When set to either true, t or 1, each tweet will
        include a node called “entities”. This node offers a variety of
        metadata about the tweet in a discreet structure, including:
        user_mentions, urls, and hashtags. While entities are opt-in on
        timelines at present, they will be made a default component of output
        in the future. See Tweet Entities for more details.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'list_id': list_id, 'slug': slug, 'user_id': user_id,
               'screen_name': screen_name, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id, 'include_entities':
               include_entities, 'skip_status': skip_status}
    url = 'https://api.twitter.com/1.1/lists/members/show.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-members-show',
                           binding)


def memberships(*, user_id=_ELIDE, screen_name=_ELIDE, count=_ELIDE,
                cursor=_ELIDE, filter_to_owned_lists=_ELIDE):
    """
    Returns the lists the specified user has been added to. If

    :param user_id: The ID of the user for whom to return results for. Helpful
        for disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to return results
        for. Helpful for disambiguating when a valid screen name is also a user
        ID.

    :param count: The amount of results to return per page. Defaults to 20. No
        more than 1000 results will ever be returned in a single page.

    :param cursor: Breaks the results into pages. Provide a value of -1 to
        begin paging. Provide values as returned in the response body’s
        next_cursor and previous_cursor attributes to page back and forth in
        the list. It is recommended to always use cursors when the method
        supports them. See [node:10362] for more information.

    :param filter_to_owned_lists: When set to true, t or 1, will return just
        lists the authenticating user owns, and the user represented by user_id
        or screen_name is a member of.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'count': count,
               'cursor': cursor, 'filter_to_owned_lists':
               filter_to_owned_lists}
    url = 'https://api.twitter.com/1.1/lists/memberships.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-memberships',
                           binding)


def ownerships(*, user_id=_ELIDE, screen_name=_ELIDE, count=_ELIDE,
               cursor=_ELIDE):
    """
    Returns the lists owned by the specified Twitter user. Private lists will
    only be shown if the authenticated user is also the owner of the lists.

    :param user_id: The ID of the user for whom to return results for.

    :param screen_name: The screen name of the user for whom to return results
        for.

    :param count: The amount of results to return per page. Defaults to 20. No
        more than 1000 results will ever be returned in a single page.

    :param cursor: Breaks the results into pages. Provide a value of -1 to
        begin paging. Provide values as returned in the response body’s
        next_cursor and previous_cursor attributes to page back and forth in
        the list. It is recommended to always use cursors when the method
        supports them. See [node:10362] for more information.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'count': count,
               'cursor': cursor}
    url = 'https://api.twitter.com/1.1/lists/ownerships.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-ownerships',
                           binding)


def show(list_id, slug, *, owner_screen_name=_ELIDE, owner_id=_ELIDE):
    """
    Returns the specified list. Private lists will only be shown if the
    authenticated user owns the specified list.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.
    """
    binding = {'list_id': list_id, 'slug': slug, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id}
    url = 'https://api.twitter.com/1.1/lists/show.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-show',
                           binding)


def statuses(list_id, slug, *, owner_screen_name=_ELIDE, owner_id=_ELIDE,
             since_id=_ELIDE, max_id=_ELIDE, count=_ELIDE,
             include_entities=_ELIDE, include_rts=_ELIDE):
    """
    Returns a timeline of tweets authored by members of the specified list.
    Retweets are included by default. Use the

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param count: Specifies the number of results to retrieve per “page.”

    :param include_entities: Entities are ON by default in API 1.1, each tweet
        includes a node called “entities”. This node offers a variety of
        metadata about the tweet in a discreet structure, including:
        user_mentions, urls, and hashtags. You can omit entities from the
        result by using include_entities=false

    :param include_rts: When set to either true, t or 1, the list timeline will
        contain native retweets (if they exist) in addition to the standard
        stream of tweets. The output format of retweeted tweets is identical to
        the representation you see in home_timeline.
    """
    binding = {'list_id': list_id, 'slug': slug, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id, 'since_id': since_id,
               'max_id': max_id, 'count': count, 'include_entities':
               include_entities, 'include_rts': include_rts}
    url = 'https://api.twitter.com/1.1/lists/statuses.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-statuses',
                           binding)


def subscribers(list_id, slug, *, owner_screen_name=_ELIDE, owner_id=_ELIDE,
                count=_ELIDE, cursor=_ELIDE, include_entities=_ELIDE,
                skip_status=_ELIDE):
    """
    Returns the subscribers of the specified list. Private list subscribers
    will only be shown if the authenticated user owns the specified list.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.

    :param count: Specifies the number of results to return per page (see
        cursor below). The default is 20, with a maximum of 5,000.

    :param cursor: Breaks the results into pages. A single page contains 20
        lists. Provide a value of -1 to begin paging. Provide values as
        returned in the response body’s next_cursor and previous_cursor
        attributes to page back and forth in the list. See Using cursors to
        navigate collections for more information.

    :param include_entities: When set to either true, t or 1, each tweet will
        include a node called “entities”. This node offers a variety of
        metadata about the tweet in a discreet structure, including:
        user_mentions, urls, and hashtags. While entities are opt-in on
        timelines at present, they will be made a default component of output
        in the future. See Tweet Entities for more details.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'list_id': list_id, 'slug': slug, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id, 'count': count,
               'cursor': cursor, 'include_entities': include_entities,
               'skip_status': skip_status}
    url = 'https://api.twitter.com/1.1/lists/subscribers.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-subscribers',
                           binding)


def subscribers_show(list_id, slug, user_id, screen_name, *,
                     owner_screen_name=_ELIDE, owner_id=_ELIDE,
                     include_entities=_ELIDE, skip_status=_ELIDE):
    """
    Check if the specified user is a subscriber of the specified list. Returns
    the user if they are subscriber.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param user_id: The ID of the user for whom to return results for. Helpful
        for disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to return results
        for. Helpful for disambiguating when a valid screen name is also a user
        ID.

    :param include_entities: When set to either true, t or 1, each tweet will
        include a node called “entities”. This node offers a variety of
        metadata about the tweet in a discreet structure, including:
        user_mentions, urls, and hashtags. While entities are opt-in on
        timelines at present, they will be made a default component of output
        in the future. See Tweet Entities for more details.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'owner_screen_name': owner_screen_name, 'owner_id': owner_id,
               'list_id': list_id, 'slug': slug, 'user_id': user_id,
               'screen_name': screen_name, 'include_entities':
               include_entities, 'skip_status': skip_status}
    url = 'https://api.twitter.com/1.1/lists/subscribers/show.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-subscribers-show',
                           binding)


def subscriptions(*, user_id=_ELIDE, screen_name=_ELIDE, count=_ELIDE,
                  cursor=_ELIDE):
    """
    Obtain a collection of the lists the specified user is subscribed to, 20
    lists per page by default. Does not include the user’s own lists.

    :param user_id: The ID of the user for whom to return results for. Helpful
        for disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to return results
        for. Helpful for disambiguating when a valid screen name is also a user
        ID.

    :param count: The amount of results to return per page. Defaults to 20. No
        more than 1000 results will ever be returned in a single page.

    :param cursor: Breaks the results into pages. Provide a value of -1 to
        begin paging. Provide values as returned in the response body’s
        next_cursor and previous_cursor attributes to page back and forth in
        the list. It is recommended to always use cursors when the method
        supports them. See [node:10362] for more information.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'count': count,
               'cursor': cursor}
    url = 'https://api.twitter.com/1.1/lists/subscriptions.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:lists',
                           'get-lists-subscriptions',
                           binding)


def create(name, *, mode=_ELIDE, description=_ELIDE):
    """
    Creates a new list for the authenticated user. Note that you can create up
    to 1000 lists per account.

    :param name: The name for the list. A list’s name must start with a letter
        and can consist only of 25 or fewer letters, numbers, “-”, or “_”
        characters.

    :param mode: Whether your list is public or private. Values can be public
        or private. If no mode is specified the list will be public.

    :param description: The description to give the list.
    """
    binding = {'name': name, 'mode': mode, 'description': description}
    url = 'https://api.twitter.com/1.1/lists/create.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-create',
                           binding)


def destroy(list_id, slug, *, owner_screen_name=_ELIDE, owner_id=_ELIDE):
    """
    Deletes the specified list. The authenticated user must own the list to be
    able to destroy it.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.
    """
    binding = {'owner_screen_name': owner_screen_name, 'owner_id': owner_id,
               'list_id': list_id, 'slug': slug}
    url = 'https://api.twitter.com/1.1/lists/destroy.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-destroy',
                           binding)


def members_create(list_id, slug, user_id, screen_name, *,
                   owner_screen_name=_ELIDE, owner_id=_ELIDE):
    """
    Add a member to a list. The authenticated user must own the list to be able
    to add members to it. Note that lists cannot have more than 5,000 members.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param user_id: The ID of the user for whom to return results for. Helpful
        for disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to return results
        for. Helpful for disambiguating when a valid screen name is also a user
        ID.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.
    """
    binding = {'list_id': list_id, 'slug': slug, 'user_id': user_id,
               'screen_name': screen_name, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id}
    url = 'https://api.twitter.com/1.1/lists/members/create.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-members-create',
                           binding)


def members_create_all(list_id, slug, *, user_id=_ELIDE, screen_name=_ELIDE,
                       owner_screen_name=_ELIDE, owner_id=_ELIDE):
    """
    Adds multiple members to a list, by specifying a comma-separated list of
    member ids or screen names. The authenticated user must own the list to be
    able to add members to it. Note that lists can’t have more than 5,000
    members, and you are limited to adding up to 100 members to a list at a
    time with this method.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param user_id: A comma separated list of user IDs, up to 100 are allowed
        in a single request.

    :param screen_name: A comma separated list of screen names, up to 100 are
        allowed in a single request.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.
    """
    binding = {'list_id': list_id, 'slug': slug, 'user_id': user_id,
               'screen_name': screen_name, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id}
    url = 'https://api.twitter.com/1.1/lists/members/create_all.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-members-create-all',
                           binding)


def members_destroy(*, list_id=_ELIDE, slug=_ELIDE, user_id=_ELIDE,
                    screen_name=_ELIDE, owner_screen_name=_ELIDE,
                    owner_id=_ELIDE):
    """
    Removes the specified member from the list. The authenticated user must be
    the list’s owner to remove members from the list.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param user_id: The ID of the user to remove from the list. Helpful for
        disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to remove from the
        list. Helpful for disambiguating when a valid screen name is also a
        user ID.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.
    """
    binding = {'list_id': list_id, 'slug': slug, 'user_id': user_id,
               'screen_name': screen_name, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id}
    url = 'https://api.twitter.com/1.1/lists/members/destroy.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-members-destroy',
                           binding)


def members_destroy_all(list_id, slug, *, user_id=_ELIDE, screen_name=_ELIDE,
                        owner_screen_name=_ELIDE, owner_id=_ELIDE):
    """
    Removes multiple members from a list, by specifying a comma-separated list
    of member ids or screen names. The authenticated user must own the list to
    be able to remove members from it. Note that lists can’t have more than 500
    members, and you are limited to removing up to 100 members to a list at a
    time with this method.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param user_id: A comma separated list of user IDs, up to 100 are allowed
        in a single request.

    :param screen_name: A comma separated list of screen names, up to 100 are
        allowed in a single request.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.
    """
    binding = {'list_id': list_id, 'slug': slug, 'user_id': user_id,
               'screen_name': screen_name, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id}
    url = 'https://api.twitter.com/1.1/lists/members/destroy_all.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-members-destroy-all',
                           binding)


def subscribers_create(list_id, slug, *, owner_screen_name=_ELIDE,
                       owner_id=_ELIDE):
    """
    Subscribes the authenticated user to the specified list.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.
    """
    binding = {'owner_screen_name': owner_screen_name, 'owner_id': owner_id,
               'list_id': list_id, 'slug': slug}
    url = 'https://api.twitter.com/1.1/lists/subscribers/create.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-subscribers-create',
                           binding)


def subscribers_destroy(list_id, slug, *, owner_screen_name=_ELIDE,
                        owner_id=_ELIDE):
    """
    Unsubscribes the authenticated user from the specified list.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.
    """
    binding = {'list_id': list_id, 'slug': slug, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id}
    url = 'https://api.twitter.com/1.1/lists/subscribers/destroy.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-subscribers-destroy',
                           binding)


def update(list_id, slug, *, name=_ELIDE, mode=_ELIDE, description=_ELIDE,
           owner_screen_name=_ELIDE, owner_id=_ELIDE):
    """
    Updates the specified list. The authenticated user must own the list to be
    able to update it.

    :param list_id: The numerical id of the list.

    :param slug: You can identify a list by its slug instead of its numerical
        id. If you decide to do so, note that you’ll also have to specify the
        list owner using the owner_id or owner_screen_name parameters.

    :param name: The name for the list.

    :param mode: Whether your list is public or private. Values can be public
        or private. If no mode is specified the list will be public.

    :param description: The description to give the list.

    :param owner_screen_name: The screen name of the user who owns the list
        being requested by a slug.

    :param owner_id: The user ID of the user who owns the list being requested
        by a slug.
    """
    binding = {'list_id': list_id, 'slug': slug, 'name': name, 'mode': mode,
               'description': description, 'owner_screen_name':
               owner_screen_name, 'owner_id': owner_id}
    url = 'https://api.twitter.com/1.1/lists/update.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:lists',
                           'post-lists-update',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/list.json'] = 'https://dev.twitter.com/rest/reference/get/lists/list'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/members.json'] = 'https://dev.twitter.com/rest/reference/get/lists/members'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/members/show.json'] = 'https://dev.twitter.com/rest/reference/get/lists/members/show'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/memberships.json'] = 'https://dev.twitter.com/rest/reference/get/lists/memberships'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/ownerships.json'] = 'https://dev.twitter.com/rest/reference/get/lists/ownerships'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/show.json'] = 'https://dev.twitter.com/rest/reference/get/lists/show'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/statuses.json'] = 'https://dev.twitter.com/rest/reference/get/lists/statuses'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/subscribers.json'] = 'https://dev.twitter.com/rest/reference/get/lists/subscribers'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/subscribers/show.json'] = 'https://dev.twitter.com/rest/reference/get/lists/subscribers/show'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/subscriptions.json'] = 'https://dev.twitter.com/rest/reference/get/lists/subscriptions'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/create.json'] = 'https://dev.twitter.com/rest/reference/post/lists/create'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/destroy.json'] = 'https://dev.twitter.com/rest/reference/post/lists/destroy'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/members/create.json'] = 'https://dev.twitter.com/rest/reference/post/lists/members/create'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/members/create_all.json'] = 'https://dev.twitter.com/rest/reference/post/lists/members/create_all'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/members/destroy.json'] = 'https://dev.twitter.com/rest/reference/post/lists/members/destroy'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/members/destroy_all.json'] = 'https://dev.twitter.com/rest/reference/post/lists/members/destroy_all'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/subscribers/create.json'] = 'https://dev.twitter.com/rest/reference/post/lists/subscribers/create'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/subscribers/destroy.json'] = 'https://dev.twitter.com/rest/reference/post/lists/subscribers/destroy'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/lists/update.json'] = 'https://dev.twitter.com/rest/reference/post/lists/update'

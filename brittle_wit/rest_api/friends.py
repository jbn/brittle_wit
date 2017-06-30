###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def ids(*, user_id=ELIDE, screen_name=ELIDE, cursor=ELIDE,
        stringify_ids=ELIDE, count=ELIDE):
    """
    Returns a cursored collection of user IDs for every user the specified user
    is following (otherwise known as their “friends”).

    :param user_id: The ID of the user for whom to return results for.

    :param screen_name: The screen name of the user for whom to return results
        for.

    :param cursor: Causes the list of connections to be broken into pages of no
        more than 5000 IDs at a time. The number of IDs returned is not
        guaranteed to be 5000 as suspended users are filtered out after
        connections are queried. If no cursor is provided, a value of -1 will
        be assumed, which is the first “page.” The response from the API will
        include a previous_cursor and next_cursor to allow paging back and
        forth. See Using cursors to navigate collections for more information.

    :param stringify_ids: Many programming environments will not consume our
        Tweet ids due to their size. Provide this option to have ids returned
        as strings instead. More about Twitter IDs.

    :param count: Specifies the number of IDs attempt retrieval of, up to a
        maximum of 5,000 per distinct request. The value of count is best
        thought of as a limit to the number of results to return. When using
        the count parameter with this method, it is wise to use a consistent
        count value across all requests to the same user’s collection. Usage of
        this parameter is encouraged in environments where all 5,000 IDs
        constitutes too large of a response.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'cursor':
               cursor, 'stringify_ids': stringify_ids, 'count': count}
    url = 'https://api.twitter.com/1.1/friends/ids.json'
    return TwitterRequest('GET',
                          url,
                          'rest:friends',
                          'get-friends-ids',
                          binding)


def list(*, user_id=ELIDE, screen_name=ELIDE, cursor=ELIDE, count=ELIDE,
         skip_status=ELIDE, include_user_entities=ELIDE):
    """
    Returns a cursored collection of user objects for every user the specified
    user is following (otherwise known as their “friends”).

    :param user_id: The ID of the user for whom to return results.

    :param screen_name: The screen name of the user for whom to return results.

    :param cursor: Causes the results to be broken into pages. If no cursor is
        provided, a value of -1 will be assumed, which is the first “page.” The
        response from the API will include a previous_cursor and next_cursor to
        allow paging back and forth. See [node:10362, title=”Using cursors to
        navigate collections”] for more information.

    :param count: The number of users to return per page, up to a maximum of
        200. Defaults to 20.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.

    :param include_user_entities: The user object entities node will not be
        included when set to false.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'cursor':
               cursor, 'count': count, 'skip_status': skip_status,
               'include_user_entities': include_user_entities}
    url = 'https://api.twitter.com/1.1/friends/list.json'
    return TwitterRequest('GET',
                          url,
                          'rest:friends',
                          'get-friends-list',
                          binding)



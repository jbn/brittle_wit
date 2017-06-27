###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, IGNORE


def users_ids(*, stringify_ids=IGNORE, cursor=IGNORE):
    """
    Returns an array of numeric user ids the authenticating user has muted.

    :param stringify_ids: Many programming environments will not consume our
        ids due to their size. Provide this option to have ids returned as
        strings instead. Read more about Twitter IDs.

    :param cursor: Causes the list of IDs to be broken into pages of no more
        than 5000 IDs at a time. The number of IDs returned is not guaranteed
        to be 5000 as suspended users are filtered out. If no cursor is
        provided, a value of -1 will be assumed, which is the first “page.” The
        response from the API will include a previous_cursor and next_cursor to
        allow paging back and forth. See Using cursors to navigate collections
        for more information.
    """
    binding = {'stringify_ids': stringify_ids, 'cursor': cursor}
    url = 'https://api.twitter.com/1.1/mutes/users/ids.json'
    return TwitterRequest('GET',
                          url,
                          'rest:mutes',
                          'get-mutes-users-ids',
                          binding)


def users_list(*, cursor=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Returns an array of

    :param cursor: Causes the list of IDs to be broken into pages of no more
        than 5000 IDs at a time. The number of IDs returned is not guaranteed
        to be 5000 as suspended users are filtered out. If no cursor is
        provided, a value of -1 will be assumed, which is the first “page.” The
        response from the API will include a previous_cursor and next_cursor to
        allow paging back and forth. See Using cursors to navigate collections
        for more information.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'cursor': cursor, 'include_entities': include_entities,
               'skip_status': skip_status}
    url = 'https://api.twitter.com/1.1/mutes/users/list.json'
    return TwitterRequest('GET',
                          url,
                          'rest:mutes',
                          'get-mutes-users-list',
                          binding)


def users_create(*, screen_name=IGNORE, user_id=IGNORE):
    """
    Mutes the user specified in the ID parameter for the authenticating user.

    :param screen_name: The screen name of the potentially muted user. Helpful
        for disambiguating when a valid screen name is also a user ID.

    :param user_id: The ID of the potentially muted user. Helpful for
        disambiguating when a valid user ID is also a valid screen name.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id}
    url = 'https://api.twitter.com/1.1/mutes/users/create.json'
    return TwitterRequest('POST',
                          url,
                          'rest:mutes',
                          'post-mutes-users-create',
                          binding)


def users_destroy(*, screen_name=IGNORE, user_id=IGNORE):
    """
    Un-mutes the user specified in the ID parameter for the authenticating
    user.

    :param screen_name: The screen name of the potentially muted user. Helpful
        for disambiguating when a valid screen name is also a user ID.

    :param user_id: The ID of the potentially muted user. Helpful for
        disambiguating when a valid user ID is also a valid screen name.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id}
    url = 'https://api.twitter.com/1.1/mutes/users/destroy.json'
    return TwitterRequest('POST',
                          url,
                          'rest:mutes',
                          'post-mutes-users-destroy',
                          binding)



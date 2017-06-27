###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, IGNORE


def ids(*, stringify_ids=IGNORE, cursor=IGNORE):
    """
    Returns an array of numeric user ids the authenticating user is blocking.

    :param stringify_ids: Many programming environments will not consume our
        ids due to their size. Provide this option to have ids returned as
        strings instead. Read more about Twitter IDs.

    :param cursor: Causes the list of IDs to be broken into pages of no more
        than 5000 IDs at a time. The number of IDs returned is not guaranteed
        to be 5000 as suspended users are filtered out after connections are
        queried. If no cursor is provided, a value of -1 will be assumed, which
        is the first “page.” The response from the API will include a
        previous_cursor and next_cursor to allow paging back and forth. See
        Using cursors to navigate collections for more information.
    """
    binding = {'stringify_ids': stringify_ids, 'cursor': cursor}
    url = 'https://api.twitter.com/1.1/blocks/ids.json'
    return TwitterRequest('GET',
                          url,
                          'rest:blocks',
                          'get-blocks-ids',
                          binding)


def list(*, include_entities=IGNORE, skip_status=IGNORE, cursor=IGNORE):
    """
    Returns a collection of

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.

    :param cursor: Causes the list of blocked users to be broken into pages of
        no more than 5000 IDs at a time. The number of IDs returned is not
        guaranteed to be 5000 as suspended users are filtered out after
        connections are queried. If no cursor is provided, a value of -1 will
        be assumed, which is the first “page.” The response from the API will
        include a previous_cursor and next_cursor to allow paging back and
        forth. See Using cursors to navigate collections for more information.
    """
    binding = {'include_entities': include_entities, 'skip_status':
               skip_status, 'cursor': cursor}
    url = 'https://api.twitter.com/1.1/blocks/list.json'
    return TwitterRequest('GET',
                          url,
                          'rest:blocks',
                          'get-blocks-list',
                          binding)


def create(*, screen_name=IGNORE, user_id=IGNORE, include_entities=IGNORE,
           skip_status=IGNORE):
    """
    Blocks the specified user from following the authenticating user. In
    addition the blocked user will not show in the authenticating users
    mentions or timeline (unless retweeted by another user). If a follow or
    friend relationship exists it is destroyed.

    :param screen_name: The screen name of the potentially blocked user.
        Helpful for disambiguating when a valid screen name is also a user ID.

    :param user_id: The ID of the potentially blocked user. Helpful for
        disambiguating when a valid user ID is also a valid screen name.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id,
               'include_entities': include_entities, 'skip_status':
               skip_status}
    url = 'https://api.twitter.com/1.1/blocks/create.json'
    return TwitterRequest('POST',
                          url,
                          'rest:blocks',
                          'post-blocks-create',
                          binding)


def destroy(*, screen_name=IGNORE, user_id=IGNORE, include_entities=IGNORE,
            skip_status=IGNORE):
    """
    Un-blocks the user specified in the ID parameter for the authenticating
    user. Returns the un-blocked user in the requested format when successful.
    If relationships existed before the block was instated, they will not be
    restored.

    :param screen_name: The screen name of the potentially blocked user.
        Helpful for disambiguating when a valid screen name is also a user ID.

    :param user_id: The ID of the potentially blocked user. Helpful for
        disambiguating when a valid user ID is also a valid screen name.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id,
               'include_entities': include_entities, 'skip_status':
               skip_status}
    url = 'https://api.twitter.com/1.1/blocks/destroy.json'
    return TwitterRequest('POST',
                          url,
                          'rest:blocks',
                          'post-blocks-destroy',
                          binding)



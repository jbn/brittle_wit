###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def incoming(*, cursor=ELIDE, stringify_ids=ELIDE):
    """
    Returns a collection of numeric IDs for every user who has a pending
    request to follow the authenticating user.

    :param cursor: Causes the list of connections to be broken into pages of no
        more than 5000 IDs at a time. The number of IDs returned is not
        guaranteed to be 5000 as suspended users are filtered out after
        connections are queried. If no cursor is provided, a value of -1 will
        be assumed, which is the first “page.” The response from the API will
        include a previous_cursor and next_cursor to allow paging back and
        forth. See [node:10362, title=”Using cursors to navigate collections”]
        for more information.

    :param stringify_ids: Many programming environments will not consume our
        Tweet ids due to their size. Provide this option to have ids returned
        as strings instead. More about [node:194].
    """
    binding = {'cursor': cursor, 'stringify_ids': stringify_ids}
    url = 'https://api.twitter.com/1.1/friendships/incoming.json'
    return TwitterRequest('GET',
                          url,
                          'rest:friendships',
                          'get-friendships-incoming',
                          binding)


def lookup(*, screen_name=ELIDE, user_id=ELIDE):
    """
    Returns the relationships of the authenticating user to the comma-separated
    list of up to 100 screen_names or user_ids provided. Values for

    :param screen_name: A comma separated list of screen names, up to 100 are
        allowed in a single request.

    :param user_id: A comma separated list of user IDs, up to 100 are allowed
        in a single request.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id}
    url = 'https://api.twitter.com/1.1/friendships/lookup.json'
    return TwitterRequest('GET',
                          url,
                          'rest:friendships',
                          'get-friendships-lookup',
                          binding)


def no_retweets_ids(*, stringify_ids=ELIDE):
    """
    Returns a collection of user_ids that the currently authenticated user does
    not want to receive retweets from.

    :param stringify_ids: Many programming environments will not consume our
        ids due to their size. Provide this option to have ids returned as
        strings instead. Read more about [node:194]. This parameter is
        especially important to use in Javascript environments.
    """
    binding = {'stringify_ids': stringify_ids}
    url = 'https://api.twitter.com/1.1/friendships/no_retweets/ids.json'
    return TwitterRequest('GET',
                          url,
                          'rest:friendships',
                          'get-friendships-no-retweets-ids',
                          binding)


def outgoing(*, cursor=ELIDE, stringify_ids=ELIDE):
    """
    Returns a collection of numeric IDs for every protected user for whom the
    authenticating user has a pending follow request.

    :param cursor: Causes the list of connections to be broken into pages of no
        more than 5000 IDs at a time. The number of IDs returned is not
        guaranteed to be 5000 as suspended users are filtered out after
        connections are queried. If no cursor is provided, a value of -1 will
        be assumed, which is the first “page.” The response from the API will
        include a previous_cursor and next_cursor to allow paging back and
        forth. See [node:10362, title=”Using cursors to navigate collections”]
        for more information.

    :param stringify_ids: Many programming environments will not consume our
        Tweet ids due to their size. Provide this option to have ids returned
        as strings instead. More about [node:194].
    """
    binding = {'cursor': cursor, 'stringify_ids': stringify_ids}
    url = 'https://api.twitter.com/1.1/friendships/outgoing.format'
    return TwitterRequest('GET',
                          url,
                          'rest:friendships',
                          'get-friendships-outgoing',
                          binding)


def show(*, source_id=ELIDE, source_screen_name=ELIDE, target_id=ELIDE,
         target_screen_name=ELIDE):
    """
    Returns detailed information about the relationship between two arbitrary
    users.

    :param source_id: The user_id of the subject user.

    :param source_screen_name: The screen_name of the subject user.

    :param target_id: The user_id of the target user.

    :param target_screen_name: The screen_name of the target user.
    """
    binding = {'source_id': source_id, 'source_screen_name':
               source_screen_name, 'target_id': target_id,
               'target_screen_name': target_screen_name}
    url = 'https://api.twitter.com/1.1/friendships/show.json'
    return TwitterRequest('GET',
                          url,
                          'rest:friendships',
                          'get-friendships-show',
                          binding)


def create(*, screen_name=ELIDE, user_id=ELIDE, follow=ELIDE):
    """
    Allows the authenticating users to follow the user specified in the ID
    parameter.

    :param screen_name: The screen name of the user for whom to befriend.

    :param user_id: The ID of the user for whom to befriend.

    :param follow: Enable notifications for the target user.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id, 'follow':
               follow}
    url = 'https://api.twitter.com/1.1/friendships/create.json'
    return TwitterRequest('POST',
                          url,
                          'rest:friendships',
                          'post-friendships-create',
                          binding)


def destroy(*, screen_name=ELIDE, user_id=ELIDE):
    """
    Allows the authenticating user to unfollow the user specified in the ID
    parameter.

    :param screen_name: The screen name of the user for whom to unfollow.

    :param user_id: The ID of the user for whom to unfollow.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id}
    url = 'https://api.twitter.com/1.1/friendships/destroy.json'
    return TwitterRequest('POST',
                          url,
                          'rest:friendships',
                          'post-friendships-destroy',
                          binding)


def update(*, screen_name=ELIDE, user_id=ELIDE, device=ELIDE, retweets=ELIDE):
    """
    Allows one to enable or disable retweets and device notifications from the
    specified user.

    :param screen_name: The screen name of the user for whom to befriend.

    :param user_id: The ID of the user for whom to befriend.

    :param device: Enable/disable device notifications from the target user.

    :param retweets: Enable/disable retweets from the target user.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id, 'device':
               device, 'retweets': retweets}
    url = 'https://api.twitter.com/1.1/friendships/update.json'
    return TwitterRequest('POST',
                          url,
                          'rest:friendships',
                          'post-friendships-update',
                          binding)



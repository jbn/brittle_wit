###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def ids(*, stringify_ids=_ELIDE, cursor=_ELIDE):
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
    return _TwitterRequest('GET',
                           url,
                           'rest:blocks',
                           'get-blocks-ids',
                           binding)


def list(*, include_entities=_ELIDE, skip_status=_ELIDE, cursor=_ELIDE):
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
    return _TwitterRequest('GET',
                           url,
                           'rest:blocks',
                           'get-blocks-list',
                           binding)


def create(*, screen_name=_ELIDE, user_id=_ELIDE, include_entities=_ELIDE,
           skip_status=_ELIDE):
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
    return _TwitterRequest('POST',
                           url,
                           'rest:blocks',
                           'post-blocks-create',
                           binding)


def destroy(*, screen_name=_ELIDE, user_id=_ELIDE, include_entities=_ELIDE,
            skip_status=_ELIDE):
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
    return _TwitterRequest('POST',
                           url,
                           'rest:blocks',
                           'post-blocks-destroy',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/blocks/ids.json'] = 'https://dev.twitter.com/rest/reference/get/blocks/ids'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/blocks/list.json'] = 'https://dev.twitter.com/rest/reference/get/blocks/list'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/blocks/create.json'] = 'https://dev.twitter.com/rest/reference/post/blocks/create'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/blocks/destroy.json'] = 'https://dev.twitter.com/rest/reference/post/blocks/destroy'

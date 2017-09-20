###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def list(*, user_id=_ELIDE, screen_name=_ELIDE, count=_ELIDE,
         since_id=_ELIDE, max_id=_ELIDE, include_entities=_ELIDE):
    """
    Returns the 20 most recent Tweets favorited by the authenticating or
    specified user.

    :param user_id: The ID of the user for whom to return results for.

    :param screen_name: The screen name of the user for whom to return results
        for.

    :param count: Specifies the number of records to retrieve. Must be less
        than or equal to 200; defaults to 20. The value of count is best
        thought of as a limit to the number of tweets to return because
        suspended or deleted content is removed after the count has been
        applied.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param include_entities: The entities node will be omitted when set to
        false.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'count': count,
               'since_id': since_id, 'max_id': max_id, 'include_entities':
               include_entities}
    url = 'https://api.twitter.com/1.1/favorites/list.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:favorites',
                           'get-favorites-list',
                           binding)


def create(id, *, include_entities=_ELIDE):
    """
    Favorites the status specified in the ID parameter as the authenticating
    user. Returns the favorite status when successful.

    :param id: The numerical ID of the desired status.

    :param include_entities: The entities node will be omitted when set to
        false.
    """
    binding = {'id': id, 'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/favorites/create.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:favorites',
                           'post-favorites-create',
                           binding)


def destroy(id, *, include_entities=_ELIDE):
    """
    Un-favorites the status specified in the ID parameter as the authenticating
    user. Returns the un-favorited status in the requested format when
    successful.

    :param id: The numerical ID of the desired status.

    :param include_entities: The entities node will be omitted when set to
        false.
    """
    binding = {'id': id, 'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/favorites/destroy.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:favorites',
                           'post-favorites-destroy',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/favorites/list.json'] = 'https://dev.twitter.com/rest/reference/get/favorites/list'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/favorites/create.json'] = 'https://dev.twitter.com/rest/reference/post/favorites/create'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/favorites/destroy.json'] = 'https://dev.twitter.com/rest/reference/post/favorites/destroy'

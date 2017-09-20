###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def entries(id, *, count=_ELIDE, max_position=_ELIDE, min_position=_ELIDE):
    """
    Retrieve the identified Collection, presented as a list of the Tweets
    curated within.

    :param id: The identifier of the Collection to return results for.

    :param count: Specifies the maximum number of results to include in the
        response. Specify a count between 1 and 200. A next_cursor value will
        be provided in the response if additional results are available.

    :param max_position: Returns results with a position value less than or
        equal to the specified position.

    :param min_position: Returns results with a position greater than the
        specified position.
    """
    binding = {'id': id, 'count': count, 'max_position': max_position,
               'min_position': min_position}
    url = 'https://api.twitter.com/1.1/collections/entries.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:collections',
                           'get-collections-entries',
                           binding)


def list(user_id, screen_name, *, tweet_id=_ELIDE, count=_ELIDE,
         cursor=_ELIDE):
    """
    Find Collections created by a specific user or containing a specific
    curated Tweet.

    :param user_id: The ID of the user for whom to return results for.

    :param screen_name: The screen name of the user for whom to return results
        for.

    :param tweet_id: The identifier of the Tweet for which to return results
        for.

    :param count: Specifies the maximum number of results to include in the
        response. Specify a count between 1 and 200. A next_cursor value will
        be provided in the response if additional results are available.

    :param cursor: A string identifying the segment of the current result set
        to retrieve. Values for this parameter are yielded in the cursors node
        attached to response objects. Usage of the count parameter affects
        cursoring.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'tweet_id':
               tweet_id, 'count': count, 'cursor': cursor}
    url = 'https://api.twitter.com/1.1/collections/list.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:collections',
                           'get-collections-list',
                           binding)


def show(id):
    """
    Retrieve information associated with a specific Collection.

    :param id: The identifier of the Collection to return results for.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/collections/show.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:collections',
                           'get-collections-show',
                           binding)


def create(name, *, description=_ELIDE, url=_ELIDE, timeline_order=_ELIDE):
    """
    Create a Collection owned by the currently authenticated user.

    :param name: The title of the collection being created, in 25 characters or
        less.

    :param description: A brief description of this collection in 160
        characters or fewer.

    :param url: A fully-qualified URL to associate with this collection.

    :param timeline_order: Order Tweets chronologically or in the order they
        are added to a Collection. curation_reverse_chron - order added
        (default) tweet_chron - oldest first tweet_reverse_chron - most recent
        first
    """
    binding = {'name': name, 'description': description, 'url': url,
               'timeline_order': timeline_order}
    url = 'https://api.twitter.com/1.1/collections/create.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:collections',
                           'post-collections-create',
                           binding)


def destroy(id):
    """
    Permanently delete a Collection owned by the currently authenticated user.

    :param id: The identifier of the Collection to destroy.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/collections/destroy.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:collections',
                           'post-collections-destroy',
                           binding)


def entries_add(id, tweet_id, *, relative_to=_ELIDE, above=_ELIDE):
    """
    Add a specified Tweet to a Collection.

    :param id: The identifier of the Collection receiving the Tweet.

    :param tweet_id: The identifier of the Tweet to add to the Collection.

    :param relative_to: The identifier of the Tweet used for relative
        positioning in a curation_reverse_chron ordered collection.

    :param above: Set to false to insert the specified tweet_id below the
        relative_to Tweet in the collection. Default: true
    """
    binding = {'id': id, 'tweet_id': tweet_id, 'relative_to': relative_to,
               'above': above}
    url = 'https://api.twitter.com/1.1/collections/entries/add.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:collections',
                           'post-collections-entries-add',
                           binding)


def entries_curate():
    """
    Curate a Collection by adding or removing Tweets in bulk. Updates must be
    limited to 100 cumulative additions or removals per request.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/collections/entries/curate.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:collections',
                           'post-collections-entries-curate',
                           binding)


def entries_move(id, tweet_id, relative_to, *, above=_ELIDE):
    """
    Move a specified Tweet to a new position in a

    :param id: The identifier of the Collection receiving the Tweet.

    :param tweet_id: The identifier of the Tweet to add to the Collection.

    :param relative_to: The identifier of the Tweet used for relative
        positioning.

    :param above: Set to false to insert the specified tweet_id below the
        relative_to Tweet in the collection. Default: true
    """
    binding = {'id': id, 'tweet_id': tweet_id, 'relative_to': relative_to,
               'above': above}
    url = 'https://api.twitter.com/1.1/collections/entries/move.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:collections',
                           'post-collections-entries-move',
                           binding)


def entries_remove(id, tweet_id):
    """
    Remove the specified Tweet from a Collection.

    :param id: The identifier of the target Collection.

    :param tweet_id: The identifier of the Tweet to remove.
    """
    binding = {'id': id, 'tweet_id': tweet_id}
    url = 'https://api.twitter.com/1.1/collections/entries/remove.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:collections',
                           'post-collections-entries-remove',
                           binding)


def update(id, *, name=_ELIDE, description=_ELIDE, url=_ELIDE):
    """
    Update information concerning a Collection owned by the currently
    authenticated user.

    :param id: The identifier of the Collection to modify.

    :param name: The title of the Collection being created, in 25 characters or
        fewer.

    :param description: A brief description of this Collection in 160
        characters or fewer.

    :param url: A fully-qualified URL to associate with this Collection.
    """
    binding = {'id': id, 'name': name, 'description': description, 'url': url}
    url = 'https://api.twitter.com/1.1/collections/update.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:collections',
                           'post-collections-update',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/entries.json'] = 'https://dev.twitter.com/rest/reference/get/collections/entries'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/list.json'] = 'https://dev.twitter.com/rest/reference/get/collections/list'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/show.json'] = 'https://dev.twitter.com/rest/reference/get/collections/show'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/create.json'] = 'https://dev.twitter.com/rest/reference/post/collections/create'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/destroy.json'] = 'https://dev.twitter.com/rest/reference/post/collections/destroy'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/entries/add.json'] = 'https://dev.twitter.com/rest/reference/post/collections/entries/add'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/entries/curate.json'] = 'https://dev.twitter.com/rest/reference/post/collections/entries/curate'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/entries/move.json'] = 'https://dev.twitter.com/rest/reference/post/collections/entries/move'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/entries/remove.json'] = 'https://dev.twitter.com/rest/reference/post/collections/entries/remove'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/collections/update.json'] = 'https://dev.twitter.com/rest/reference/post/collections/update'

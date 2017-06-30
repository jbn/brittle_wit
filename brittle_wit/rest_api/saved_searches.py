###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def list():
    """
    Returns the authenticated user’s saved search queries.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/saved_searches/list.json'
    return TwitterRequest('GET',
                          url,
                          'rest:saved_searches',
                          'get-saved-searches-list',
                          binding)


def show_by_id(id):
    """
    Retrieve the information for the saved search represented by the given id.
    The authenticating user must be the owner of saved search ID being
    requested.

    :param id: The ID of the saved search.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/saved_searches/show/{id}.json'
    url = url.format(**binding)
    return TwitterRequest('GET',
                          url,
                          'rest:saved_searches',
                          'get-saved-searches-show-id',
                          binding)


def create(query):
    """
    Create a new saved search for the authenticated user. A user may only have
    25 saved searches.

    :param query: The query of the search the user would like to save.
    """
    binding = {'query': query}
    url = 'https://api.twitter.com/1.1/saved_searches/create.json'
    return TwitterRequest('POST',
                          url,
                          'rest:saved_searches',
                          'post-saved-searches-create',
                          binding)


def destroy_by_id(id):
    """
    Destroys a saved search for the authenticating user. The authenticating
    user must be the owner of saved search id being destroyed.

    :param id: The ID of the saved search.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/saved_searches/destroy/{id}.json'
    url = url.format(**binding)
    return TwitterRequest('POST',
                          url,
                          'rest:saved_searches',
                          'post-saved-searches-destroy-id',
                          binding)



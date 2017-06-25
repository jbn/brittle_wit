###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def list():
    """
    Returns the authenticated user's saved search queries.
    """
    url = "https://api.twitter.com/1.1/saved_searches/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:SAVED_SEARCHES',
                          'GET-SAVED-SEARCHES-LIST')


def show_by_id(id):
    """
    Retrieve the information for the saved search represented by the given id.
    The authenticating user must be the owner of saved search ID being
    requested.
    
    :param id: The ID of the saved search. (True)
    """
    url = "https://api.twitter.com/1.1/saved_searches/show/{id}.json"
    url = url.format(id=id)
    return TwitterRequest('GET',
                          url,
                          'REST:SAVED_SEARCHES',
                          'GET-SAVED-SEARCHES-SHOW-ID',
                          id=id)


def create(query):
    """
    Create a new saved search for the authenticated user. A user may only have
    25 saved searches.
    
    :param query: The query of the search the user would like to save. (True)
    """
    url = "https://api.twitter.com/1.1/saved_searches/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:SAVED_SEARCHES',
                          'POST-SAVED-SEARCHES-CREATE',
                          query=query)


def destroy_by_id(id):
    """
    Destroys a saved search for the authenticating user. The authenticating
    user must be the owner of saved search id being destroyed.
    
    :param id: The ID of the saved search. (True)
    """
    url = "https://api.twitter.com/1.1/saved_searches/destroy/{id}.json"
    url = url.format(id=id)
    return TwitterRequest('POST',
                          url,
                          'REST:SAVED_SEARCHES',
                          'POST-SAVED-SEARCHES-DESTROY-ID',
                          id=id)



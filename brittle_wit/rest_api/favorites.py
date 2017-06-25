###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def list(*, user_id=IGNORE, screen_name=IGNORE, count=IGNORE, since_id=IGNORE, max_id=IGNORE, include_entities=IGNORE):
    """
    Returns the 20 most recent Tweets favorited by the authenticating or
    specified user.
    
    :param user_id: The ID of the user for whom to return results for. (False)
    
    :param screen_name: The screen name of the user for whom to return results 
        for. (False)
    
    
    :param count: Specifies the number of records to retrieve. Must be less tha
        n or equal to 200; defaults to 20. The value of count is best thought
        of as a limit to the number of tweets to return because suspended or
        deleted content is removed after the count has been applied. (False)
    
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param include_entities: The entities node will be omitted when set to fals
        e. (False)
    """
    url = "https://api.twitter.com/1.1/favorites/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:FAVORITES',
                          'GET-FAVORITES-LIST',
                          user_id=user_id
                          screen_name=screen_name
                          count=count
                          since_id=since_id
                          max_id=max_id
                          include_entities=include_entities)


def create(id, *, include_entities=IGNORE):
    """
    Favorites the status specified in the ID parameter as the authenticating
    user. Returns the favorite status when successful.
    
    :param id: The numerical ID of the desired status. (True)
    
    :param include_entities: The entities node will be omitted when set to fals
        e. (False)
    """
    url = "https://api.twitter.com/1.1/favorites/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:FAVORITES',
                          'POST-FAVORITES-CREATE',
                          id=id
                          include_entities=include_entities)


def destroy(id, *, include_entities=IGNORE):
    """
    Un-favorites the status specified in the ID parameter as the authenticating
    user. Returns the un-favorited status in the requested format when
    successful.
    
    :param id: The numerical ID of the desired status. (True)
    
    :param include_entities: The entities node will be omitted when set to fals
        e. (False)
    """
    url = "https://api.twitter.com/1.1/favorites/destroy.json"
    return TwitterRequest('POST',
                          url,
                          'REST:FAVORITES',
                          'POST-FAVORITES-DESTROY',
                          id=id
                          include_entities=include_entities)



###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def entries(id, *, count=IGNORE, max_position=IGNORE, min_position=IGNORE):
    """
    Retrieve the identified Collection, presented as a list of the Tweets
    curated within.
    
    :param id: The identifier of the Collection to return results for. (True)
    
    :param count: Specifies the maximum number of results to include in the res
        ponse. Specify a count between 1 and 200. A next_cursor value will be
        provided in the response if additional results are available. (False)
    
    
    :param max_position: Returns results with a position value less than or equ
        al to the specified position. (False)
    
    
    :param min_position: Returns results with a position greater than the speci
        fied position. (False)
    """
    url = "https://api.twitter.com/1.1/collections/entries.json"
    return TwitterRequest('GET',
                          url,
                          'REST:COLLECTIONS',
                          'GET-COLLECTIONS-ENTRIES',
                          id=id
                          count=count
                          max_position=max_position
                          min_position=min_position)


def list(user_id, screen_name, *, tweet_id=IGNORE, count=IGNORE, cursor=IGNORE):
    """
    Find Collections created by a specific user or containing a specific
    curated Tweet.
    
    :param user_id: The ID of the user for whom to return results for. (True)
    
    :param screen_name: The screen name of the user for whom to return results 
        for. (True)
    
    
    :param tweet_id: The identifier of the Tweet for which to return results fo
        r. (False)
    
    
    :param count: Specifies the maximum number of results to include in the res
        ponse. Specify a count between 1 and 200. A next_cursor value will be
        provided in the response if additional results are available. (False)
    
    
    :param cursor: A string identifying the segment of the current result set t
        o retrieve. Values for this parameter are yielded in the cursors node
        attached to response objects. Usage of the count parameter affects
        cursoring. (False)
    """
    url = "https://api.twitter.com/1.1/collections/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:COLLECTIONS',
                          'GET-COLLECTIONS-LIST',
                          user_id=user_id
                          screen_name=screen_name
                          tweet_id=tweet_id
                          count=count
                          cursor=cursor)


def show(id):
    """
    Retrieve information associated with a specific Collection.
    
    :param id: The identifier of the Collection to return results for. (True)
    """
    url = "https://api.twitter.com/1.1/collections/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:COLLECTIONS',
                          'GET-COLLECTIONS-SHOW',
                          id=id)


def create(name, *, description=IGNORE, url=IGNORE, timeline_order=IGNORE):
    """
    Create a Collection owned by the currently authenticated user.
    
    :param name: The title of the collection being created, in 25 characters or
        less. (True)
    
    
    :param description: A brief description of this collection in 160 character
        s or fewer. (False)
    
    
    :param url: A fully-qualified URL to associate with this collection. (False
        )
    
    
    :param timeline_order: Order Tweets chronologically or in the order they ar
        e added to a Collection. curation_reverse_chron - order added (default)
        tweet_chron - oldest first tweet_reverse_chron - most recent first
        (False)
    """
    url = "https://api.twitter.com/1.1/collections/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:COLLECTIONS',
                          'POST-COLLECTIONS-CREATE',
                          name=name
                          description=description
                          url=url
                          timeline_order=timeline_order)


def destroy(id):
    """
    Permanently delete a Collection owned by the currently authenticated user.
    
    :param id: The identifier of the Collection to destroy. (True)
    """
    url = "https://api.twitter.com/1.1/collections/destroy.json"
    return TwitterRequest('POST',
                          url,
                          'REST:COLLECTIONS',
                          'POST-COLLECTIONS-DESTROY',
                          id=id)


def entries_add(id, tweet_id, *, relative_to=IGNORE, above=IGNORE):
    """
    Add a specified Tweet to a Collection.
    
    :param id: The identifier of the Collection receiving the Tweet. (True)
    
    :param tweet_id: The identifier of the Tweet to add to the Collection. (Tru
        e)
    
    
    :param relative_to: The identifier of the Tweet used for relative positioni
        ng in a curation_reverse_chron ordered collection. (False)
    
    
    :param above: Set to false to insert the specified tweet_id below the relat
        ive_to Tweet in the collection. Default: true (False)
    """
    url = "https://api.twitter.com/1.1/collections/entries/add.json"
    return TwitterRequest('POST',
                          url,
                          'REST:COLLECTIONS',
                          'POST-COLLECTIONS-ENTRIES-ADD',
                          id=id
                          tweet_id=tweet_id
                          relative_to=relative_to
                          above=above)


def entries_curate():
    """
    Curate a Collection by adding or removing Tweets in bulk. Updates must be
    limited to 100 cumulative additions or removals per request.
    """
    url = "https://api.twitter.com/1.1/collections/entries/curate.json"
    return TwitterRequest('POST',
                          url,
                          'REST:COLLECTIONS',
                          'POST-COLLECTIONS-ENTRIES-CURATE')


def entries_move(id, tweet_id, relative_to, *, above=IGNORE):
    """
    Move a specified Tweet to a new position in a
    
    :param id: The identifier of the Collection receiving the Tweet. (True)
    
    :param tweet_id: The identifier of the Tweet to add to the Collection. (Tru
        e)
    
    
    :param relative_to: The identifier of the Tweet used for relative positioni
        ng. (True)
    
    
    :param above: Set to false to insert the specified tweet_id below the relat
        ive_to Tweet in the collection. Default: true (False)
    """
    url = "https://api.twitter.com/1.1/collections/entries/move.json"
    return TwitterRequest('POST',
                          url,
                          'REST:COLLECTIONS',
                          'POST-COLLECTIONS-ENTRIES-MOVE',
                          id=id
                          tweet_id=tweet_id
                          relative_to=relative_to
                          above=above)


def entries_remove(id, tweet_id):
    """
    Remove the specified Tweet from a Collection.
    
    :param id: The identifier of the target Collection. (True)
    
    :param tweet_id: The identifier of the Tweet to remove. (True)
    """
    url = "https://api.twitter.com/1.1/collections/entries/remove.json"
    return TwitterRequest('POST',
                          url,
                          'REST:COLLECTIONS',
                          'POST-COLLECTIONS-ENTRIES-REMOVE',
                          id=id
                          tweet_id=tweet_id)


def update(id, *, name=IGNORE, description=IGNORE, url=IGNORE):
    """
    Update information concerning a Collection owned by the currently
    authenticated user.
    
    :param id: The identifier of the Collection to modify. (True)
    
    :param name: The title of the Collection being created, in 25 characters or
        fewer. (False)
    
    
    :param description: A brief description of this Collection in 160 character
        s or fewer. (False)
    
    
    :param url: A fully-qualified URL to associate with this Collection. (False
        )
    """
    url = "https://api.twitter.com/1.1/collections/update.json"
    return TwitterRequest('POST',
                          url,
                          'REST:COLLECTIONS',
                          'POST-COLLECTIONS-UPDATE',
                          id=id
                          name=name
                          description=description
                          url=url)



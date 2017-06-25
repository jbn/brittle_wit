###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def direct_messages(*, since_id=IGNORE, max_id=IGNORE, count=IGNORE, include_entities=IGNORE, skip_status=IGNORE):
    """
    Returns the 20 most recent direct messages sent to the authenticating user.
    Includes detailed information about the sender and recipient user. You can
    request up to 200 direct messages per call, and only the most recent 200
    DMs will be available using this endpoint.
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param count: Specifies the number of direct messages to try and retrieve, 
        up to a maximum of 200. The value of count is best thought of as a
        limit to the number of Tweets to return because suspended or deleted
        content is removed after the count has been applied. (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    
    
    :param skip_status: When set to either true, t or 1 statuses will not be in
        cluded in the returned user objects. (False)
    """
    url = "https://api.twitter.com/1.1/direct_messages.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES',
                          since_id=since_id
                          max_id=max_id
                          count=count
                          include_entities=include_entities
                          skip_status=skip_status)


def events_list(*, count=IGNORE, cursor=IGNORE):
    """
    Returns all Direct Message events (both sent
    """
    url = "https://api.twitter.com/1.1/direct_messages/events/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-EVENTS-LIST',
                          count=count
                          cursor=cursor)


def events_show(id):
    """
    Returns a single Direct Message event by the given id.
    """
    url = "https://api.twitter.com/1.1/direct_messages/events/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-EVENTS-SHOW',
                          id=id)


def sent(*, since_id=IGNORE, max_id=IGNORE, count=IGNORE, page=IGNORE, include_entities=IGNORE):
    """
    Returns the 20 most recent direct messages sent by the authenticating user.
    Includes detailed information about the sender and recipient user. You can
    request up to 200 direct messages per call, up to a maximum of 200 outgoing
    DMs.
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param count: Specifies the number of records to retrieve. Must be less tha
        n or equal to 200. (False)
    
    
    :param page: Specifies the page of results to retrieve. (False)
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    """
    url = "https://api.twitter.com/1.1/direct_messages/sent.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-SENT',
                          since_id=since_id
                          max_id=max_id
                          count=count
                          page=page
                          include_entities=include_entities)


def show(id):
    """
    Returns a single direct message, specified by an id parameter. Like the
    
    :param id: The ID of the direct message. (True)
    """
    url = "https://api.twitter.com/1.1/direct_messages/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-SHOW',
                          id=id)


def welcome_messages_list(*, count=IGNORE, cursor=IGNORE):
    """
    Returns a list of Welcome Messages.
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-WELCOME-MESSAGES-LIST',
                          count=count
                          cursor=cursor)


def welcome_messages_rules_list(*, count=IGNORE, cursor=IGNORE):
    """
    Returns a list of Welcome Message Rules.
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/list.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-WELCOME-MESSAGES-RULES-LIST',
                          count=count
                          cursor=cursor)


def welcome_messages_rules_show(id):
    """
    Returns a Welcome Message Rule by the given id.
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-WELCOME-MESSAGES-RULES-SHOW',
                          id=id)


def welcome_messages_show(id):
    """
    Returns a Welcome Message by the given id.
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/show.json"
    return TwitterRequest('GET',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'GET-DIRECT-MESSAGES-WELCOME-MESSAGES-SHOW',
                          id=id)


def destroy(id, *, include_entities=IGNORE):
    """
    Destroys the direct message specified in the required ID parameter. The
    authenticating user must be the recipient of the specified direct message.
    
    :param id: The ID of the direct message to delete. (True)
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    """
    url = "https://api.twitter.com/1.1/direct_messages/destroy.json"
    return TwitterRequest('POST',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'POST-DIRECT-MESSAGES-DESTROY',
                          id=id
                          include_entities=include_entities)


def events_new (message_create)():
    """
    Publishes a new
    """
    url = "https://api.twitter.com/1.1/direct_messages/events/new.json"
    return TwitterRequest('POST',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'POST-DIRECT-MESSAGES-EVENTS-NEW-MESSAGE-CREATE')


def new(text, *, user_id=IGNORE, screen_name=IGNORE):
    """
    Sends a new direct message to the specified user from the authenticating
    user. Requires both the
    
    :param user_id: The ID of the user who should receive the direct message. H
        elpful for disambiguating when a valid user ID is also a valid screen
        name. (False)
    
    
    :param screen_name: The screen name of the user who should receive the dire
        ct message. Helpful for disambiguating when a valid screen name is also
        a user ID. (False)
    
    
    :param text: The text of your direct message. Be sure to URL encode as nece
        ssary, and keep the message under 140 characters. (True)
    """
    url = "https://api.twitter.com/1.1/direct_messages/new.json"
    return TwitterRequest('POST',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'POST-DIRECT-MESSAGES-NEW',
                          user_id=user_id
                          screen_name=screen_name
                          text=text)


def welcome_messages_new():
    """
    Creates a new Welcome Message that will be stored and sent in the future
    from the authenticating user in defined circumstances. Returns the message
    template in the requested format if successful. Supports publishing with
    the same elements as Direct Messages (e.g. Quick Replies, media
    attachments).
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/new.json"
    return TwitterRequest('POST',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'POST-DIRECT-MESSAGES-WELCOME-MESSAGES-NEW')


def welcome_messages_rules_new():
    """
    Creates a new Welcome Message Rule that determines which Welcome Message
    will be shown in a given conversation. Returns the created rule if
    successful.
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/new.json"
    return TwitterRequest('POST',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'POST-DIRECT-MESSAGES-WELCOME-MESSAGES-RULES-NEW')


def welcome_messages_destroy(id):
    """
    Deletes a Welcome Message by the given id.
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/destroy.json"
    return TwitterRequest('DELETE',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'DELETE-DIRECT-MESSAGES-WELCOME-MESSAGES-DESTROY',
                          id=id)


def welcome_messages_rules_destroy(id):
    """
    Deletes a Welcome Message Rule by the given id.
    """
    url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/destroy.json"
    return TwitterRequest('DELETE',
                          url,
                          'REST:DIRECT_MESSAGES',
                          'DELETE-DIRECT-MESSAGES-WELCOME-MESSAGES-RULES-DESTROY',
                          id=id)



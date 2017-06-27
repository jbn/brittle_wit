###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, IGNORE


def direct_messages(*, since_id=IGNORE, max_id=IGNORE, count=IGNORE,
                    include_entities=IGNORE, skip_status=IGNORE):
    """
    Returns the 20 most recent direct messages sent to the authenticating user.
    Includes detailed information about the sender and recipient user. You can
    request up to 200 direct messages per call, and only the most recent 200
    DMs will be available using this endpoint.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param count: Specifies the number of direct messages to try and retrieve,
        up to a maximum of 200. The value of count is best thought of as a
        limit to the number of Tweets to return because suspended or deleted
        content is removed after the count has been applied.

    :param include_entities: The entities node will not be included when set to
        false.

    :param skip_status: When set to either true, t or 1 statuses will not be
        included in the returned user objects.
    """
    binding = {'since_id': since_id, 'max_id': max_id, 'count': count,
               'include_entities': include_entities, 'skip_status':
               skip_status}
    url = 'https://api.twitter.com/1.1/direct_messages.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages',
                          binding)


def events_list(*, count=IGNORE, cursor=IGNORE):
    """
    Returns all Direct Message events (both sent
    """
    binding = {'count': count, 'cursor': cursor}
    url = 'https://api.twitter.com/1.1/direct_messages/events/list.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-events-list',
                          binding)


def events_show(id):
    """
    Returns a single Direct Message event by the given id.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/direct_messages/events/show.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-events-show',
                          binding)


def sent(*, since_id=IGNORE, max_id=IGNORE, count=IGNORE, page=IGNORE,
         include_entities=IGNORE):
    """
    Returns the 20 most recent direct messages sent by the authenticating user.
    Includes detailed information about the sender and recipient user. You can
    request up to 200 direct messages per call, up to a maximum of 200 outgoing
    DMs.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param count: Specifies the number of records to retrieve. Must be less
        than or equal to 200.

    :param page: Specifies the page of results to retrieve.

    :param include_entities: The entities node will not be included when set to
        false.
    """
    binding = {'since_id': since_id, 'max_id': max_id, 'count': count, 'page':
               page, 'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/direct_messages/sent.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-sent',
                          binding)


def show(id):
    """
    Returns a single direct message, specified by an id parameter. Like the

    :param id: The ID of the direct message.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/direct_messages/show.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-show',
                          binding)


def welcome_messages_list(*, count=IGNORE, cursor=IGNORE):
    """
    Returns a list of Welcome Messages.
    """
    binding = {'count': count, 'cursor': cursor}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/list.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-welcome-messages-list',
                          binding)


def welcome_messages_rules_list(*, count=IGNORE, cursor=IGNORE):
    """
    Returns a list of Welcome Message Rules.
    """
    binding = {'count': count, 'cursor': cursor}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/list.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-welcome-messages-rules-list',
                          binding)


def welcome_messages_rules_show(id):
    """
    Returns a Welcome Message Rule by the given id.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/show.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-welcome-messages-rules-show',
                          binding)


def welcome_messages_show(id):
    """
    Returns a Welcome Message by the given id.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/show.json'
    return TwitterRequest('GET',
                          url,
                          'rest:direct_messages',
                          'get-direct-messages-welcome-messages-show',
                          binding)


def destroy(id, *, include_entities=IGNORE):
    """
    Destroys the direct message specified in the required ID parameter. The
    authenticating user must be the recipient of the specified direct message.

    :param id: The ID of the direct message to delete.

    :param include_entities: The entities node will not be included when set to
        false.
    """
    binding = {'id': id, 'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/direct_messages/destroy.json'
    return TwitterRequest('POST',
                          url,
                          'rest:direct_messages',
                          'post-direct-messages-destroy',
                          binding)


def events_newmessage_create():
    """
    Publishes a new
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'
    return TwitterRequest('POST',
                          url,
                          'rest:direct_messages',
                          'post-direct-messages-events-new-message-create',
                          binding)


def new(text, *, user_id=IGNORE, screen_name=IGNORE):
    """
    Sends a new direct message to the specified user from the authenticating
    user. Requires both the

    :param user_id: The ID of the user who should receive the direct message.
        Helpful for disambiguating when a valid user ID is also a valid screen
        name.

    :param screen_name: The screen name of the user who should receive the
        direct message. Helpful for disambiguating when a valid screen name is
        also a user ID.

    :param text: The text of your direct message. Be sure to URL encode as
        necessary, and keep the message under 140 characters.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name, 'text': text}
    url = 'https://api.twitter.com/1.1/direct_messages/new.json'
    return TwitterRequest('POST',
                          url,
                          'rest:direct_messages',
                          'post-direct-messages-new',
                          binding)


def welcome_messages_new():
    """
    Creates a new Welcome Message that will be stored and sent in the future
    from the authenticating user in defined circumstances. Returns the message
    template in the requested format if successful. Supports publishing with
    the same elements as Direct Messages (e.g. Quick Replies, media
    attachments).
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/new.json'
    return TwitterRequest('POST',
                          url,
                          'rest:direct_messages',
                          'post-direct-messages-welcome-messages-new',
                          binding)


def welcome_messages_rules_new():
    """
    Creates a new Welcome Message Rule that determines which Welcome Message
    will be shown in a given conversation. Returns the created rule if
    successful.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/new.json'
    return TwitterRequest('POST',
                          url,
                          'rest:direct_messages',
                          'post-direct-messages-welcome-messages-rules-new',
                          binding)


def welcome_messages_destroy(id):
    """
    Deletes a Welcome Message by the given id.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/destroy.json'
    return TwitterRequest('DELETE',
                          url,
                          'rest:direct_messages',
                          'delete-direct-messages-welcome-messages-destroy',
                          binding)


def welcome_messages_rules_destroy(id):
    """
    Deletes a Welcome Message Rule by the given id.
    """
    binding = {'id': id}
    url = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/destroy.json'
    return TwitterRequest('DELETE',
                          url,
                          'rest:direct_messages',
                          'delete-direct-messages-welcome-messages-rules-destroy',
                          binding)



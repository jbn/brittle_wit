###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def webhooks(url):
    """
    Registers a new webhook URL for the given application context. The URL will
    be validated via CRC request before saving. In case the validation fails,
    an error is returned. Only one webhook URL can be registered to an
    application.
    """
    url = "https://api.twitter.com/1.1/account_activity/webhooks.json"
    return TwitterRequest('POST',
                          url,
                          'WEBHOOKS:ACCOUNT_ACTIVITY',
                          'POST-ACCOUNT-ACTIVITY-WEBHOOKS',
                          url=url)


def webhooks():
    """
    Returns all URLs and their statuses for the given app. Currently, only one
    webhook URL can be registered to an application.
    """
    url = "https://api.twitter.com/1.1/account_activity/webhooks.json"
    return TwitterRequest('GET',
                          url,
                          'WEBHOOKS:ACCOUNT_ACTIVITY',
                          'GET-ACCOUNT-ACTIVITY-WEBHOOKS')


def webhooks_by_webhook_id(webhook_id):
    """
    Removes the webhook from the provided application's configuration. The
    webhook ID can be accessed by making a call to GET
    /1.1/account_activity/webhooks.
    """
    url = "https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}.json"
    url = url.format(webhook_id=webhook_id)
    return TwitterRequest('DELETE',
                          url,
                          'WEBHOOKS:ACCOUNT_ACTIVITY',
                          'DELETE-ACCOUNT-ACTIVITY-WEBHOOKS-WEBHOOK-ID',
                          webhook_id=webhook_id)


def webhooks_subscriptions_by_webhook_id(webhook_id):
    """
    Subscribes the provided app to events for the provided user context. When
    subscribed, all DM events for the provided user will be sent to the app's
    webhook via POST request.
    """
    url = "https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json"
    url = url.format(webhook_id=webhook_id)
    return TwitterRequest('POST',
                          url,
                          'WEBHOOKS:ACCOUNT_ACTIVITY',
                          'POST-ACCOUNT-ACTIVITY-WEBHOOKS-WEBHOOK-ID-SUBSCRIPTIONS',
                          webhook_id=webhook_id)


def webhooks_subscriptions_by_webhook_id(webhook_id):
    """
    Provides a way to determine if a webhook configuration is subscribed to the
    provided user's Direct Messages. If the provided user context has an active
    subscription with the provided app, returns 204 OK. If the response code is
    not 204, then the user does not have an active subscription. See HTTP
    Response code and error messages below for details.
    """
    url = "https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json"
    url = url.format(webhook_id=webhook_id)
    return TwitterRequest('GET',
                          url,
                          'WEBHOOKS:ACCOUNT_ACTIVITY',
                          'GET-ACCOUNT-ACTIVITY-WEBHOOKS-WEBHOOK-ID-SUBSCRIPTIONS',
                          webhook_id=webhook_id)


def webhooks_subscriptions_by_webhook_id(webhook_id):
    """
    Deactivates subscription for the provided user context and app. After
    deactivation, all DM events for the requesting user will no longer be sent
    to the webhook URL.
    """
    url = "https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json"
    url = url.format(webhook_id=webhook_id)
    return TwitterRequest('DELETE',
                          url,
                          'WEBHOOKS:ACCOUNT_ACTIVITY',
                          'DELETE-ACCOUNT-ACTIVITY-WEBHOOKS-WEBHOOK-ID-SUBSCRIPTIONS',
                          webhook_id=webhook_id)



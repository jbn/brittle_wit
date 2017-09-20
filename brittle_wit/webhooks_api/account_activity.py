###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def webhooks(url):
    """
    Registers a new webhook URL for the given application context. The URL will
    be validated via CRC request before saving. In case the validation fails,
    an error is returned. Only one webhook URL can be registered to an
    application.
    """
    binding = {'url': url}
    url = 'https://api.twitter.com/1.1/account_activity/webhooks.json'
    return _TwitterRequest('POST',
                           url,
                           'webhooks:account_activity',
                           'post-account-activity-webhooks',
                           binding)


def webhooks():
    """
    Returns all URLs and their statuses for the given app. Currently, only one
    webhook URL can be registered to an application.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/account_activity/webhooks.json'
    return _TwitterRequest('GET',
                           url,
                           'webhooks:account_activity',
                           'get-account-activity-webhooks',
                           binding)


def webhooks_by_webhook_id(webhook_id):
    """
    Removes the webhook from the provided application’s configuration. The
    webhook ID can be accessed by making a call to GET
    /1.1/account_activity/webhooks.
    """
    binding = {'webhook_id': webhook_id}
    url = 'https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}.json'
    url = url.format(**binding)
    return _TwitterRequest('DELETE',
                           url,
                           'webhooks:account_activity',
                           'delete-account-activity-webhooks-webhook-id',
                           binding)


def webhooks_by_webhook_id(webhook_id):
    """
    Triggers the challenge response check (CRC) for the given webhook’s URL. If
    the check is successful, returns 204 and reenables the webhook by setting
    its status to
    """
    binding = {'webhook_id': webhook_id}
    url = 'https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}.json'
    url = url.format(**binding)
    return _TwitterRequest('PUT',
                           url,
                           'webhooks:account_activity',
                           'put-account-activity-webhooks-webhook-id',
                           binding)


def webhooks_subscriptions_by_webhook_id(webhook_id):
    """
    Subscribes the provided app to events for the provided user context. When
    subscribed, all DM events for the provided user will be sent to the app’s
    webhook via POST request.
    """
    binding = {'webhook_id': webhook_id}
    url = 'https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json'
    url = url.format(**binding)
    return _TwitterRequest('POST',
                           url,
                           'webhooks:account_activity',
                           'post-account-activity-webhooks-webhook-id-subscriptions',
                           binding)


def webhooks_subscriptions_by_webhook_id(webhook_id):
    """
    Provides a way to determine if a webhook configuration is subscribed to the
    provided user’s Direct Messages. If the provided user context has an active
    subscription with the provided app, returns 204 OK. If the response code is
    not 204, then the user does not have an active subscription. See HTTP
    Response code and error messages below for details.
    """
    binding = {'webhook_id': webhook_id}
    url = 'https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'webhooks:account_activity',
                           'get-account-activity-webhooks-webhook-id-subscriptions',
                           binding)


def webhooks_subscriptions_by_webhook_id(webhook_id):
    """
    Deactivates subscription for the provided user context and app. After
    deactivation, all DM events for the requesting user will no longer be sent
    to the webhook URL.
    """
    binding = {'webhook_id': webhook_id}
    url = 'https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json'
    url = url.format(**binding)
    return _TwitterRequest('DELETE',
                           url,
                           'webhooks:account_activity',
                           'delete-account-activity-webhooks-webhook-id-subscriptions',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/account_activity/webhooks.json'] = 'https://dev.twitter.com/webhooks/reference/post/account_activity/webhooks'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/account_activity/webhooks.json'] = 'https://dev.twitter.com/webhooks/reference/get/account_activity/webhooks'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}.json'] = 'https://dev.twitter.com/webhooks/reference/del/account_activity/webhooks'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}.json'] = 'https://dev.twitter.com/webhooks/reference/put/account_activity/webhooks'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json'] = 'https://dev.twitter.com/webhooks/reference/post/account_activity/webhooks/subscriptions'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json'] = 'https://dev.twitter.com/webhooks/reference/get/account_activity/webhooks/subscriptions'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/account_activity/webhooks/{webhook_id}/subscriptions.json'] = 'https://dev.twitter.com/webhooks/reference/del/account_activity/webhooks/subscriptions'

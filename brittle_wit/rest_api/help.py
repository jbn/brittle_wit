###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def configuration():
    """
    Returns the current configuration used by Twitter including twitter.com
    slugs which are not usernames, maximum photo resolutions, and t.co
    shortened URL length.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/help/configuration.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:help',
                           'get-help-configuration',
                           binding)


def languages():
    """
    Returns the list of languages supported by Twitter along with the language
    code supported by Twitter.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/help/languages.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:help',
                           'get-help-languages',
                           binding)


def privacy():
    """
    Returns
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/help/privacy.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:help',
                           'get-help-privacy',
                           binding)


def tos():
    """
    Returns the
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/help/tos.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:help',
                           'get-help-tos',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/help/configuration.json'] = 'https://dev.twitter.com/rest/reference/get/help/configuration'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/help/languages.json'] = 'https://dev.twitter.com/rest/reference/get/help/languages'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/help/privacy.json'] = 'https://dev.twitter.com/rest/reference/get/help/privacy'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/help/tos.json'] = 'https://dev.twitter.com/rest/reference/get/help/tos'

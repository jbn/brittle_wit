###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest, ELIDE


def configuration():
    """
    Returns the current configuration used by Twitter including twitter.com
    slugs which are not usernames, maximum photo resolutions, and t.co
    shortened URL length.
    """
    binding = {}
    url = 'https://api.twitter.com/1.1/help/configuration.json'
    return TwitterRequest('GET',
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
    return TwitterRequest('GET',
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
    return TwitterRequest('GET',
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
    return TwitterRequest('GET',
                          url,
                          'rest:help',
                          'get-help-tos',
                          binding)



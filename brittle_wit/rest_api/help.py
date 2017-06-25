###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def configuration():
    """
    Returns the current configuration used by Twitter including twitter.com
    slugs which are not usernames, maximum photo resolutions, and t.co
    shortened URL length.
    """
    url = "https://api.twitter.com/1.1/help/configuration.json"
    return TwitterRequest('GET',
                          url,
                          'REST:HELP',
                          'GET-HELP-CONFIGURATION')


def languages():
    """
    Returns the list of languages supported by Twitter along with the language
    code supported by Twitter.
    """
    url = "https://api.twitter.com/1.1/help/languages.json"
    return TwitterRequest('GET',
                          url,
                          'REST:HELP',
                          'GET-HELP-LANGUAGES')


def privacy():
    """
    Returns
    """
    url = "https://api.twitter.com/1.1/help/privacy.json"
    return TwitterRequest('GET',
                          url,
                          'REST:HELP',
                          'GET-HELP-PRIVACY')


def tos():
    """
    Returns the
    """
    url = "https://api.twitter.com/1.1/help/tos.json"
    return TwitterRequest('GET',
                          url,
                          'REST:HELP',
                          'GET-HELP-TOS')



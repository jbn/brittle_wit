###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def lookup(*, screen_name=_ELIDE, user_id=_ELIDE, include_entities=_ELIDE):
    """
    Returns fully-hydrated

    :param screen_name: A comma separated list of screen names, up to 100 are
        allowed in a single request. You are strongly encouraged to use a POST
        for larger (up to 100 screen names) requests.

    :param user_id: A comma separated list of user IDs, up to 100 are allowed
        in a single request. You are strongly encouraged to use a POST for
        larger requests.

    :param include_entities: The entities node that may appear within embedded
        statuses will not be included when set to false.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id,
               'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/users/lookup.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:users',
                           'get-users-lookup',
                           binding)


def profile_banner(*, user_id=_ELIDE, screen_name=_ELIDE):
    """
    Returns a map of the available size variations of the specified user’s
    profile banner. If the user has not uploaded a profile banner, a HTTP 404
    will be served instead. This method can be used instead of string
    manipulation on the

    :param user_id: The ID of the user for whom to return results. Helpful for
        disambiguating when a valid user ID is also a valid screen name.

    :param screen_name: The screen name of the user for whom to return results.
        Helpful for disambiguating when a valid screen name is also a user ID.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name}
    url = 'https://api.twitter.com/1.1/users/profile_banner.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:users',
                           'get-users-profile-banner',
                           binding)


def search(q, *, page=_ELIDE, count=_ELIDE, include_entities=_ELIDE):
    """
    Provides a simple, relevance-based search interface to public user accounts
    on Twitter. Try querying by topical interest, full name, company name,
    location, or other criteria. Exact match searches are not supported.

    :param q: The search query to run against people search.

    :param page: Specifies the page of results to retrieve.

    :param count: The number of potential user results to retrieve per page.
        This value has a maximum of 20.

    :param include_entities: The entities node will not be included in embedded
        Tweet objects when set to false.
    """
    binding = {'q': q, 'page': page, 'count': count, 'include_entities':
               include_entities}
    url = 'https://api.twitter.com/1.1/users/search.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:users',
                           'get-users-search',
                           binding)


def show(user_id, screen_name, *, include_entities=_ELIDE):
    """
    Returns a

    :param user_id: The ID of the user for whom to return results. Either an id
        or screen_name is required for this method.

    :param screen_name: The screen name of the user for whom to return results.
        Either a id or screen_name is required for this method.

    :param include_entities: The entities node will not be included when set to
        false.
    """
    binding = {'user_id': user_id, 'screen_name': screen_name,
               'include_entities': include_entities}
    url = 'https://api.twitter.com/1.1/users/show.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:users',
                           'get-users-show',
                           binding)


def suggestions(*, lang=_ELIDE):
    """
    Access to Twitter’s suggested user list. This returns the list of suggested
    user categories. The category can be used in

    :param lang: Restricts the suggested categories to the requested language.
        The language must be specified by the appropriate two letter ISO 639-1
        representation. Currently supported languages are provided by the GET
        help / languages API request. Unsupported language codes will receive
        English (en) results. If you use lang in this request, ensure you also
        include it when requesting the GET users / suggestions / :slug list.
    """
    binding = {'lang': lang}
    url = 'https://api.twitter.com/1.1/users/suggestions.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:users',
                           'get-users-suggestions',
                           binding)


def suggestions_by_slug(slug, *, lang=_ELIDE):
    """
    Access the users in a given category of the Twitter suggested user list.

    :param slug: The short name of list or a category

    :param lang: Restricts the suggested categories to the requested language.
        The language must be specified by the appropriate two letter ISO 639-1
        representation. Currently supported languages are provided by the GET
        help / languages API request. Unsupported language codes will receive
        English (en) results. If you use lang in this request, ensure you also
        include it when requesting the GET users / suggestions / :slug list.
    """
    binding = {'slug': slug, 'lang': lang}
    url = 'https://api.twitter.com/1.1/users/suggestions/{slug}.json'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'rest:users',
                           'get-users-suggestions-slug',
                           binding)


def suggestions_members_by_slug(slug):
    """
    Access the users in a given category of the Twitter suggested user list and
    return their most recent status if they are not a protected user.

    :param slug: The short name of list or a category
    """
    binding = {'slug': slug}
    url = 'https://api.twitter.com/1.1/users/suggestions/{slug}/members.json'
    url = url.format(**binding)
    return _TwitterRequest('GET',
                           url,
                           'rest:users',
                           'get-users-suggestions-slug-members',
                           binding)


def report_spam(*, screen_name=_ELIDE, user_id=_ELIDE, perform_block=_ELIDE):
    """
    Report the specified user as a spam account to Twitter. Additionally,
    optionally performs the equivalent of

    :param screen_name: The screen_name of the user to report as a spammer.
        Helpful for disambiguating when a valid screen name is also a user ID.

    :param user_id: The ID of the user to report as a spammer. Helpful for
        disambiguating when a valid user ID is also a valid screen name.

    :param perform_block: Whether the account should be blocked by the
        authenticated user, as well as being reported for spam.
    """
    binding = {'screen_name': screen_name, 'user_id': user_id,
               'perform_block': perform_block}
    url = 'https://api.twitter.com/1.1/users/report_spam.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:users',
                           'post-users-report-spam',
                           binding)


_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/lookup.json'] = 'https://dev.twitter.com/rest/reference/get/users/lookup'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/profile_banner.json'] = 'https://dev.twitter.com/rest/reference/get/users/profile_banner'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/search.json'] = 'https://dev.twitter.com/rest/reference/get/users/search'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/show.json'] = 'https://dev.twitter.com/rest/reference/get/users/show'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/suggestions.json'] = 'https://dev.twitter.com/rest/reference/get/users/suggestions'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/suggestions/{slug}.json'] = 'https://dev.twitter.com/rest/reference/get/users/suggestions/slug'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/suggestions/{slug}/members.json'] = 'https://dev.twitter.com/rest/reference/get/users/suggestions/slug/members'
_TwitterRequest.DOC_URLS['https://api.twitter.com/1.1/users/report_spam.json'] = 'https://dev.twitter.com/rest/reference/post/users/report_spam'

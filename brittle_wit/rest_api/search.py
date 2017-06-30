###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def tweets(q, *, geocode=ELIDE, lang=ELIDE, locale=ELIDE, result_type=ELIDE,
           count=ELIDE, until=ELIDE, since_id=ELIDE, max_id=ELIDE,
           include_entities=ELIDE):
    """
    Returns a collection of relevant

    :param q: A UTF-8, URL-encoded search query of 500 characters maximum,
        including operators. Queries may additionally be limited by complexity.

    :param geocode: Returns tweets by users located within a given radius of
        the given latitude/longitude. The location is preferentially taking
        from the Geotagging API, but will fall back to their Twitter profile.
        The parameter value is specified by ” latitude,longitude,radius ”,
        where radius units must be specified as either ” mi ” (miles) or ” km ”
        (kilometers). Note that you cannot use the near operator via the API to
        geocode arbitrary locations; however you can use this geocode parameter
        to search near geocodes directly. A maximum of 1,000 distinct “sub-
        regions” will be considered when using the radius modifier.

    :param lang: Restricts tweets to the given language, given by an ISO 639-1
        code. Language detection is best-effort.

    :param locale: Specify the language of the query you are sending (only ja
        is currently effective). This is intended for language-specific
        consumers and the default should work in the majority of cases.

    :param result_type: Optional. Specifies what type of search results you
        would prefer to receive. The current default is “mixed.” Valid values
        include: * mixed : Include both popular and real time results in the
        response. * recent : return only the most recent results in the
        response * popular : return only the most popular results in the
        response.

    :param count: The number of tweets to return per page, up to a maximum of
        100. Defaults to 15. This was formerly the “rpp” parameter in the old
        Search API.

    :param until: Returns tweets created before the given date. Date should be
        formatted as YYYY-MM-DD. Keep in mind that the search index has a 7-day
        limit. In other words, no tweets will be found for a date older than
        one week.

    :param since_id: Returns results with an ID greater than (that is, more
        recent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available.

    :param max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    :param include_entities: The entities node will not be included when set to
        false.
    """
    binding = {'q': q, 'geocode': geocode, 'lang': lang, 'locale': locale,
               'result_type': result_type, 'count': count, 'until': until,
               'since_id': since_id, 'max_id': max_id, 'include_entities':
               include_entities}
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    return TwitterRequest('GET',
                          url,
                          'rest:search',
                          'get-search-tweets',
                          binding)



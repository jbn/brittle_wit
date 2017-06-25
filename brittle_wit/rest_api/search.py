###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def tweets(q, *, geocode=IGNORE, lang=IGNORE, locale=IGNORE, result_type=IGNORE, count=IGNORE, until=IGNORE, since_id=IGNORE, max_id=IGNORE, include_entities=IGNORE):
    """
    Returns a collection of relevant
    
    :param q: A UTF-8, URL-encoded search query of 500 characters maximum, incl
        uding operators. Queries may additionally be limited by complexity.
        (True)
    
    
    :param geocode: Returns tweets by users located within a given radius of th
        e given latitude/longitude. The location is preferentially taking from
        the Geotagging API, but will fall back to their Twitter profile. The
        parameter value is specified by ” latitude,longitude,radius ”, where
        radius units must be specified as either ” mi ” (miles) or ” km ”
        (kilometers). Note that you cannot use the near operator via the API to
        geocode arbitrary locations; however you can use this geocode parameter
        to search near geocodes directly. A maximum of 1,000 distinct “sub-
        regions” will be considered when using the radius modifier. (False)
    
    
    :param lang: Restricts tweets to the given language, given by an ISO 639-1 
        code. Language detection is best-effort. (False)
    
    
    :param locale: Specify the language of the query you are sending (only ja i
        s currently effective). This is intended for language-specific
        consumers and the default should work in the majority of cases. (False)
    
    
    :param result_type: Optional. Specifies what type of search results you wou
        ld prefer to receive. The current default is “mixed.” Valid values
        include: * mixed : Include both popular and real time results in the
        response. * recent : return only the most recent results in the
        response * popular : return only the most popular results in the
        response. (False)
    
    
    :param count: The number of tweets to return per page, up to a maximum of 1
        00. Defaults to 15. This was formerly the “rpp” parameter in the old
        Search API. (False)
    
    
    :param until: Returns tweets created before the given date. Date should be 
        formatted as YYYY-MM-DD. Keep in mind that the search index has a 7-day
        limit. In other words, no tweets will be found for a date older than
        one week. (False)
    
    
    :param since_id: Returns results with an ID greater than (that is, more rec
        ent than) the specified ID. There are limits to the number of Tweets
        which can be accessed through the API. If the limit of Tweets has
        occured since the since_id, the since_id will be forced to the oldest
        ID available. (False)
    
    
    :param max_id: Returns results with an ID less than (that is, older than) o
        r equal to the specified ID. (False)
    
    
    :param include_entities: The entities node will not be included when set to
        false. (False)
    """
    url = "https://api.twitter.com/1.1/search/tweets.json"
    return TwitterRequest('GET',
                          url,
                          'REST:SEARCH',
                          'GET-SEARCH-TWEETS',
                          q=q
                          geocode=geocode
                          lang=lang
                          locale=locale
                          result_type=result_type
                          count=count
                          until=until
                          since_id=since_id
                          max_id=max_id
                          include_entities=include_entities)



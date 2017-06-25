###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def iab_categories(*, count=IGNORE, cursor=IGNORE):
    """
    Request the valid app
    
    :param count: Specifies the number of categories to try and retrieve. (Fals
        e)
    
    
    :param cursor: Specifies a cursor to get the next page of categories. See P
        agination for more information. (False)
    """
    url = "Resource URL¶
https://ads-api.twitter.com/1/iab_categories"
    return TwitterRequest('GET',
                          url,
                          'ADS:IAB_CATEGORIES',
                          'GET-IAB-CATEGORIES',
                          count=count
                          cursor=cursor)



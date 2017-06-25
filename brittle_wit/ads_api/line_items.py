###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def placements(*, product_type=IGNORE):
    """
    Request the valid combinations of
    
    :param product_type: Scope the results by a specific product type. For the 
        possible values, see enumerations. (False)
    """
    url = "https://ads-api.twitter.com/1/line_items/placements"
    return TwitterRequest('GET',
                          url,
                          'ADS:LINE_ITEMS',
                          'GET-LINE-ITEMS-PLACEMENTS',
                          product_type=product_type)



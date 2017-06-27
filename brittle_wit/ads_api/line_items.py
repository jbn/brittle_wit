###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, IGNORE


def placements(*, product_type=IGNORE):
    """
    Request the valid combinations of

    :param product_type: Scope the results by a specific product type. For the
        possible values, see enumerations.
    """
    binding = {'product_type': product_type}
    url = 'https://ads-api.twitter.com/1/line_items/placements'
    return TwitterRequest('GET',
                          url,
                          'ads:line_items',
                          'get-line-items-placements',
                          binding)



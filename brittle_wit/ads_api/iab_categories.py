###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit.messages import TwitterRequest, ELIDE


def iab_categories(*, count=ELIDE, cursor=ELIDE):
    """
    Request the valid app

    :param count: Specifies the number of categories to try and retrieve.

    :param cursor: Specifies a cursor to get the next page of categories. See
        Pagination for more information.
    """
    binding = {'count': count, 'cursor': cursor}
    url = 'https://ads-api.twitter.com/1/iab_categories'
    return TwitterRequest('GET',
                          url,
                          'ads:iab_categories',
                          'get-iab-categories',
                          binding)



###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def iab_categories(*, count=_ELIDE, cursor=_ELIDE, with_total_count=_ELIDE):
    """
    Request the valid app

    :param count: Specifies the number of records to try and retrieve per
        distinct request. Type: int Default: 200 Min, Max: 1, 1000

    :param cursor: Specifies a cursor to get the next page of categories. See
        Pagination for more information. Type: string Example: gc-ddf4a

    :param with_total_count: Include the total_count response attribute. Note:
        total_count will only be returned when with_total_count is set to true
        and next_cursor is null. Note: Requests which include total_count will
        have lower rate limits, currently set at 200 per 15 minutes. Type:
        boolean Default: false Possible values: true, false
    """
    binding = {'count': count, 'cursor': cursor, 'with_total_count':
               with_total_count}
    url = 'https://ads-api.twitter.com/2/iab_categories'
    return _TwitterRequest('GET',
                           url,
                           'ads:iab_categories',
                           'get-iab-categories',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/iab_categories'] = 'https://dev.twitter.com/ads/reference/get/iab_categories'

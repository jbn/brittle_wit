###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def placements(*, product_type=_ELIDE):
    """
    Retrieve valid

    :param product_type: Scope the response to just the valid placements for
        the specified product type. Type: enum Possible values: LIVE_TV_EVENT,
        MEDIA, PROMOTED_ACCOUNT, PROMOTED_TWEETS
    """
    binding = {'product_type': product_type}
    url = 'https://ads-api.twitter.com/2/line_items/placements'
    return _TwitterRequest('GET',
                           url,
                           'ads:line_items',
                           'get-line-items-placements',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/line_items/placements'] = 'https://dev.twitter.com/ads/reference/get/line_items/placements'

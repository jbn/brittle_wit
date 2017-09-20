###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def bidding_rules(*, currency=_ELIDE):
    """
    Retrieve the bidding rules for a specific or all currencies. The response
    will indicate the minimum and maximum CPE (cost-per-engagement) bids.

    :param currency: The type of a currency to filter results by, identified
        using ISO-4217. This is a three-letter string “USD” or “EUR”. Omit this
        parameter to retrieve all bidding rules. associated with the
        authenticating user. Type: string Example: USD
    """
    binding = {'currency': currency}
    url = 'https://ads-api.twitter.com/2/bidding_rules'
    return _TwitterRequest('GET',
                           url,
                           'ads:bidding_rules',
                           'get-bidding-rules',
                           binding)


_TwitterRequest.DOC_URLS['https://ads-api.twitter.com/2/bidding_rules'] = 'https://dev.twitter.com/ads/reference/get/bidding_rules'

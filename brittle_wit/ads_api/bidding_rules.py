###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, IGNORE


def bidding_rules(*, currency=IGNORE):
    """
    Retrieve the bidding rules for a specific or all currencies. The response
    will indicate the minimum and maximum CPE (cost-per-engagement) bids.

    :param currency: The type of a currency to filter results by, identified
        using ISO-4217. This is a three-letter string like “USD” or “EUR”. Omit
        this parameter to retrieve all bidding rules.
    """
    binding = {'currency': currency}
    url = 'https://ads-api.twitter.com/1/bidding_rules'
    return TwitterRequest('GET',
                          url,
                          'ads:bidding_rules',
                          'get-bidding-rules',
                          binding)



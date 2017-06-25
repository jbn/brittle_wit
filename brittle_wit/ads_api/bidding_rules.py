###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def bidding_rules(*, currency=IGNORE):
    """
    Retrieve the bidding rules for a specific or all currencies. The response
    will indicate the minimum and maximum CPE (cost-per-engagement) bids.
    
    :param currency: The type of a currency to filter results by, identified us
        ing ISO-4217. This is a three-letter string like “USD” or “EUR”. Omit
        this parameter to retrieve all bidding rules. (False)
    """
    url = "Resource URL¶
https://ads-api.twitter.com/1/bidding_rules"
    return TwitterRequest('GET',
                          url,
                          'ADS:BIDDING_RULES',
                          'GET-BIDDING-RULES',
                          currency=currency)



###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest, ELIDE


def tailored_audience_memberships(operation_type, params, user_identifier,
                                  user_identifier_type, *,
                                  advertiser_account_id=ELIDE,
                                  membership_type=ELIDE,
                                  audience_names=ELIDE, effective_at=ELIDE,
                                  expires_at=ELIDE):
    """
    This real-time API will enable partners to upload batched tailored audience
    information to Twitter for processing in real-time.

    :param operation_type: The per item operation type being performed.
        Currently, only the Update operation is supported, and can be used to
        create new tailored audience associations.

    :param params: A JSON object containing all params for each user object
        (listed below).

    :param advertiser_account_id: The advertiser’s Twitter Ads account
        identifier. This is NOT the @handle for the advertiser. Required for
        LIST_MEMBERSHIP and WEB_MEMBERSHIP, optional for WEB_OPTOUT

    :param membership_type: The product this request is intended for. For a
        full list of available products please refer to the enums page.

    :param user_identifier: The unique ID that is used by the partner to
        identify the user.

    :param user_identifier_type: The type of identifier used for
        user_identifier. For the full list of supported types, please refer to
        the enums page

    :param audience_names: A comma separated list of tailored audiences to add
        this user to, identified by their audience names. If no existing
        audience is found for a provided audience name, a new audience will be
        created. Maximum length of this list: 100 characters. Required for
        WEB_MEMBERSHIP and LIST_MEMBERSHIP, optional for WEB_OPTOUT

    :param effective_at: The UTC time at which the tailored audience
        association(s) should take effect. Expressed in ISO 8601. Defaults to
        the current date and time.

    :param expires_at: The UTC time at which the tailored audience
        association(s) should expire. The specified time must be later than the
        value of effective_at. Expressed in ISO 8601. Defaults to your
        configured default expiration period (typically 30 days or 720 hours
        from effective_at )
    """
    binding = {'operation_type': operation_type, 'params': params,
               'advertiser_account_id': advertiser_account_id,
               'membership_type': membership_type, 'user_identifier':
               user_identifier, 'user_identifier_type': user_identifier_type,
               'audience_names': audience_names, 'effective_at': effective_at,
               'expires_at': expires_at}
    url = 'https://ads-api.twitter.com/1/tailored_audience_memberships'
    return TwitterRequest('POST',
                          url,
                          'ads:tailored_audience_memberships',
                          'post-tailored-audience-memberships',
                          binding)



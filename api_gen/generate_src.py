#!/usr/bin/env python

import json
import os
from collections import defaultdict
from api_code_gen import (generate_source, generate_modules,
                          _annotate_nonunique_names)


SELF_DIR = os.path.dirname(os.path.realpath(__file__))
LIB_BASE = os.path.join(SELF_DIR, os.pardir, "brittle_wit")
CLEAN_DIR = os.path.join(SELF_DIR, "data", "clean")
API_PATH = os.path.join(CLEAN_DIR, "api.json")


# These endpoints prefixed with 1 seem to be identical to those
# that are not prefixed with 1. I think it's legacy. I need to look
# into it more, but for now, I'll skip the edge case in src generation.
IGNORE_REF_URLS = {"https://ads-api.twitter.com/1/accounts/:account_id/tailored_audiences/:id",
                   "https://dev.twitter.com/ads/reference/1/get/accounts/account_id/tailored_audiences/id",
                   "https://dev.twitter.com/ads/reference/1/del/accounts/account_id/tailored_audiences/id",
                   "https://dev.twitter.com/ads/reference/1/get/accounts/account_id/tailored_audiences",
                   "https://dev.twitter.com/ads/reference/1/post/accounts/account_id/tailored_audiences"}


def correcting_code_gen(api_def):
    return generate_source(api_def, '_annotate_nonunique_names' in api_def)


if __name__ == '__main__':
    with open(API_PATH) as fp:
        definitions = {}
        for group, api_defns in json.load(fp).items():
            valid_api_defs = []
            for api_def in api_defns:
                if api_def['reference_url'] not in IGNORE_REF_URLS:
                    valid_api_defs.append(api_def)
            definitions[group] = valid_api_defs

    _annotate_nonunique_names(definitions)
    generate_modules(LIB_BASE, definitions)

#!/usr/bin/env python

import json
import os
import api_code_gen


SELF_DIR = os.path.dirname(os.path.realpath(__file__))
LIB_BASE = os.path.join(SELF_DIR, os.pardir, "brittle_wit")
CLEAN_DIR = os.path.join(SELF_DIR, "data", "clean")
API_PATH = os.path.join(CLEAN_DIR, "api.json")

if __name__ == '__main__':
    with open(API_PATH) as fp:
        definitions = json.load(fp)
    api_code_gen.generate_modules(LIB_BASE, definitions)

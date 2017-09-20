#!/usr/bin/env python

import json
import os
from collections import defaultdict
from vaquero import Vaquero, ModulePipeline
from vaquero.util import jsonlines_reader


SELF_DIR = os.path.dirname(os.path.realpath(__file__))
RAW_DIR = os.path.join(SELF_DIR, "data", "raw")
CLEAN_DIR = os.path.join(SELF_DIR, "data", "clean")
INPUT_PATH = os.path.join(RAW_DIR, "raw_html.jsonl")
OUTPUT_PATH = os.path.join(CLEAN_DIR, "api.json")

IGNORE_PAGES = {'https://dev.twitter.com/ads/reference/get',
                'https://dev.twitter.com/ads/reference/post',
                'https://dev.twitter.com/ads/reference/put',
                'https://dev.twitter.com/ads/reference/del'}

if __name__ == '__main__':
    os.makedirs(CLEAN_DIR, exist_ok=True)
    definitions = defaultdict(list)

    vaq = Vaquero(max_failures=0)
    import api_pipeline
    pipeline = ModulePipeline(api_pipeline)

    # These reset so you can do `%run -i extract_definitions.py` in a notebook
    vaq.reset()
    pipeline.reload()

    for src in jsonlines_reader(INPUT_PATH):
        dst = {}
        if src['reference_url'] in IGNORE_PAGES:
            continue
        print("Parsing:", src['reference_url'])
        with vaq:
            pipeline(src, dst)
            definitions[dst['group']].append(dst)

    print(vaq.stats())
    if not os.environ.get('DEBUG'):
        with open(OUTPUT_PATH, "w") as fp:
            json.dump(definitions, fp, indent=4)

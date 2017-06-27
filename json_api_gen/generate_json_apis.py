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


if __name__ == '__main__':
    os.makedirs(CLEAN_DIR, exist_ok=True)
    definitions = defaultdict(list)

    vaq = Vaquero(max_failures=0)
    import api_pipeline
    pipeline = ModulePipeline(api_pipeline)

    # These reset so you can do `%run -i extract_definitions.py`
    vaq.reset()
    pipeline.reload()

    for src in jsonlines_reader(INPUT_PATH):
        dst = {}
        with vaq:
            pipeline(src, dst)
            definitions[dst['group']].append(dst)

    if not os.environ.get('DEBUG'):
        for group, api_defs in definitions.items():
            with open(os.path.join(CLEAN_DIR, group + "_api.json"), "w") as fp:
                json.dump(api_defs, fp, indent=4)

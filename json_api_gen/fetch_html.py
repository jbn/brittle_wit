#!/usr/bin/env python

import json
import os
import requests
from lxml.html import fromstring


SELF_DIR = os.path.dirname(os.path.realpath(__file__))
RAW_DIR = os.path.join(SELF_DIR, "data", "raw")
REFERENCE_ROOTS = {"rest": "https://dev.twitter.com/rest/reference",
                   "streaming": "https://dev.twitter.com/streaming/reference",
                   "webhooks": "https://dev.twitter.com/webhooks/reference",
                   "ads": "https://dev.twitter.com/ads/reference"}


def fetch_endpoints_from(root_url):
    doc = fromstring(requests.get(root_url).content)
    doc.make_links_absolute(root_url)

    valid_methods = {'DELETE', 'GET', 'POST'}

    endpoints = []
    for a in doc.xpath("//a"):
        txt, href = a.text, a.attrib['href']
        if '/reference/' in href and a.text.split(" ")[0] in valid_methods:
            method, *service = a.text.split(" ")
            endpoints.append({'method': method,
                              'service': " ".join(service),
                              'reference_url': href})

    return endpoints


def fetch_and_save_all(fp, group, reference_root_url):
    already_fetched = set()
    endpoints = fetch_endpoints_from(reference_root_url)

    for d in endpoints:
        print("...", d['reference_url'])
        resp = requests.get(d['reference_url'])
        d['_raw_html'] = resp.content.decode(resp.encoding)
        d['group'] = group
        if d['reference_url'] not in already_fetched:
            fp.write(json.dumps(d) + "\n")
            already_fetched.add(d['reference_url'])


if __name__ == '__main__':
    os.makedirs(RAW_DIR, exist_ok=True)

    with open(os.path.join(RAW_DIR, "raw_html.jsonl"), "w") as fp:
        for group, reference_root_url in REFERENCE_ROOTS.items():
            print("Fetching for", group)
            fetch_and_save_all(fp, group, reference_root_url)
            print("")

#!/usr/bin/python3

"""
    opensearch.py
    MediaWiki API Demos
    Demo of `Opensearch` module: Search the wiki and obtain
	results in an OpenSearch (http://www.opensearch.org) format
    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

keywords = ""

PARAMS = {"action": "opensearch","namespace": "0","search": "","limit": "1","format": "json"}
PARAMS['search'] = keywords

#PARAMS = {"action": "opensearch","namespace": "0","search": "mdadm","limit": "1","format": "json"}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA[3][0])
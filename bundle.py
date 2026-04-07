#! /bin/python3

# This script bundles all wiki definitions into a single `data.json` file.
# It also generates a `meta.json` file describing `data.json`, which the
# extension queries to check whether it should update its cached definitions.

import hashlib
import json
import os
import re
import tomllib

from pathlib import Path

format_version = 0

wikis = {}

for e in os.scandir('wikis'):
    if e.is_file() and e.name.endswith('.toml'):
        id = re.sub(r'\.toml$', '', e.name)
        with open(e.path, 'rb') as f:
            wikis[id] = tomllib.load(f)

data = {
    'format_version': format_version,
    'hosts': [],
    'wikis': wikis,
}

Path("generated").mkdir(exist_ok=True)

def compact_json_dump(obj, file):
    json.dump(obj, file, separators=(',', ':'))

with open('generated/data.json', 'w+') as data_json:
    compact_json_dump(data, data_json)

with open('generated/data.json', 'rb') as data_json:
    hash = hashlib.file_digest(data_json, 'sha256').hexdigest()

    with open('generated/meta.json', 'w+') as meta_json:
        meta = {
            'format_version': format_version,
            'hash': hash,
        }
        compact_json_dump(meta, meta_json)




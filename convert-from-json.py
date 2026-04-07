#! /bin/python3

import json
import os
import tomli_w

wikis = {}

for e in os.scandir('json'):
    if e.is_file() and e.name.endswith('.json'):
        print(f'Converting {e.name}...')
        with open(e.path, 'r') as f:
            langwikis = json.load(f)
            for wiki in langwikis:
                [lang, id] = wiki['id'].split('-', 1)

                if id not in wikis:
                    wikis[id] = {}
                
                wikis[id][lang] = wiki
                wikis[id][lang].pop('id')

for id in wikis.keys():
    with open(f'wikis/{id}.toml', 'wb') as f:
        tomli_w.dump(wikis[id], f)

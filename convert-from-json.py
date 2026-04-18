#! /bin/python3

# Helper script to convert the old JSON files to TOML.

import json
import re
import os
import tomli_w

wikis = {}

def convert_wiki(wiki: dict, lang):
    used_keys = []
    def get(key):
        used_keys.append(key)
        return wiki.get(key)

    def convert_host(host: dict, prefix: str):
        props = {
            'name': prefix,
            'host': f'{prefix}_host',
            'url': f'{prefix}_base_url',
            'platform': f'{prefix}_platform',
            'icon': f'{prefix}_icon',
            'mainpage': f'{prefix}_main_page',
            'search-path': f'{prefix}_search_path',
            'content-path': f'{prefix}_content_path',
            'content-prefix': f'{prefix}_content_prefix',
            'content-suffix': f'{prefix}_content_suffix',
        }

        if prefix == 'origin':
            props['destination-content-prefix'] = 'destination_content_prefix'

        for key in host.keys():
            if key not in props.values():
                print(f'unknown host key {key}')

        r = {}
        for (k, v) in props.items():
            if prefix == 'destination':
                get(v)
            if host.get(v) is not None:
                r[k] = host.get(v)
        return r

    destination_host = dict(filter(lambda it: it[0].startswith('destination'), wiki.items()))
    destination = convert_host(destination_host, 'destination')

    destination['tags'] = get('tags') or []
    destination['tags'].append('recommended')

    r = {
        'name': re.sub(r'\s+Fandom.+Wiki.*$', '', get('origins_label') or ''),
        'icon': get('destination_icon'),
        'origin': list(map(lambda it: convert_host(it, 'origin'), get('origins') or {})),
        'destination': [destination],
    }
    get('id')

    for key in wiki.keys():
        if key not in used_keys:
            print(f'unknown wiki key {key}')

    return r

for e in os.scandir('json'):
    if e.is_file() and e.name.endswith('.json'):
        print(f'Converting {e.name}...')
        with open(e.path, 'r') as f:
            langwikis = json.load(f)
            for wiki in langwikis:
                [lang, id] = wiki['id'].split('-', 1)

                if id not in wikis:
                    wikis[id] = {}
                
                wikis[id][lang] = convert_wiki(wiki, lang)

for id in wikis.keys():
    with open(f'wikis/{id}.toml', 'wb') as f:
        tomli_w.dump(wikis[id], f)

from flask import render_template
from collections import defaultdict


class NYPLViewsLib:

    def __init__(self):
        pass

    def render_index(self, db):
        images = db.images.find()  # cursor
        return render_template('index.html',
                               images=images,
                               prefixes=get_prefixes(images.clone()),
                               pmatches=get_prefix_matches(images.clone()),
                               psets=get_prefix_sets(images.clone()))


def get_prefix_sets(images):
    pset = defaultdict(list)
    for item in images:
        pset[item['prefix']].append({'fname': item['fname'],
                                     'location': item['location'],
                                     'matches': item['matches']})
    return pset


def get_prefixes(images):
    prefixes = set()
    for item in images:
        prefixes.add(item['prefix'])
    return prefixes


def get_prefix_matches(images):
    pmatch = set()
    for item in images:
        if item['matches']:
            pmatch.add(item['prefix'])
    return pmatch

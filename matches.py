#!/usr/bin/env python

"""Get/sample matching upsearch results"""

from __future__ import division, print_function

import argparse
import os
import random
import requests
import sys
import time

from collections import defaultdict
from uploader import Uploader

__author__ = "@siznax"
__version__ = "July 2016"


class Reporter:

    cache = {}
    matches = {}
    nonmatches = {}
    outfile = None
    sample_size = 0
    uploads = []

    def __init__(self, outfile):
        if os.path.exists(outfile):
            print("ABORT: output match file exists! " + outfile)
            sys.exit(1)
        self.outfile = outfile

    def dump(self):
        data = dict(self.matches, **self.nonmatches)
        data.update(self.cache)
        fname = self.outfile
        with open(fname, "w") as fp:
            fp.write(repr(data) + "\n")
            print("wrote " + fname)

    def ranks(self):
        '''tally matched image artists'''
        totals = defaultdict(int)
        for fname, matches in self.matches.items():
            for key, val in matches.items():
                totals[key] += 1  # one tick regardless of num matches
        keys = sorted(totals, key=totals.get, reverse=True)
        for i, name in enumerate(keys[:10]):
            print("#%d %s: %d" % (i + 1, name, totals[name]))

    def report(self):
        n_m = len(self.matches)
        n_u = len(self.uploads)
        s_s = self.sample_size
        if n_m:
            if s_s:
                per = (n_m / s_s) * 100.0
                ans = "{0:.0f}% ({1:d}/{2:d})".format(per, n_m, s_s)
                print("Found %s matches in sample (%d/%d)" % (ans, s_s, n_u))
            else:
                per = (n_m / n_u) * 100.0
                ans = "{0:.0f}% ({1:d}/{2:d})".format(per, n_m, n_u)
                print("Found %s matches." % ans)
            self.dump()
            self.ranks()


def get_json(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()


def get_location(fname):
    with open(fname, 'r') as fp:
        for line in fp:
            if line.startswith('Location'):
                return line.split()[1]


def get_matches(rep, uploads, sleep, cache):
    print("getting %d matches" % len(uploads))
    count = 0
    matches = None
    for item in uploads:
        prematch_hit = False
        try:
            fname, location = item.split()
            if fname in cache:
                matches = cache[fname]
                prematch_hit = True
            else:
                json_url = location + '?type=json'
                matches = parse_json(get_json(json_url), json_url)
            # m = [ {'Kiyochika': 5, 'Kiyofoo': 4, 'Kiyobar': 3},
            #       {'Hokusai': 3, 'Hokufoo': 2, 'Hokuboo': 1},
            #       {'Kiyochika':3, 'Kiyobar': 5} ]
            # matches = m[count]
        except Exception as e:
            print("Caught %s: %s" % (type(e).__name__, e))
            print(item)

        count += 1
        if prematch_hit:
            print("{%d} %s %s %s" % (count, fname, matches, location))
        else:
            print("[%d] %s %s %s" % (count, fname, matches, location))
        sys.stdout.flush()
        if matches:
            rep.matches[fname] = matches
        else:
            rep.nonmatches[fname] = {}
        if count < len(uploads) and not prematch_hit:
            time.sleep(sleep)


def parse_json(_json, url):
    matches = defaultdict(int)
    if 'results' in _json:
        for match in _json['results']:
            try:
                short_name = match['artist']['short_name'].encode('utf-8')
                full_name = match['artist']['full_name'].encode('utf-8')
                if short_name:
                    matches[short_name] += 1
                else:
                    matches[full_name] += 1
            except KeyError:
                artist = match['artist']['full_name'].encode('utf-8')
                matches[artist] += 1
    return dict(matches)


def get_uploads(pname):
    uploads = []
    for upload in Uploader.findext(pname, '.upload'):
        location = get_location(upload)
        uploads.append("%s %s" % (upload.replace('.upload', ''), location))
    return uploads


def main(rep, pname, listflag, rsamp, sleep, cfile):
    cache = {}
    if cfile:
        with open(cfile, 'r') as fp:
            cache = eval(fp.read())
            rep.cache = cache

    uploads = get_uploads(pname)
    rep.uploads = uploads
    print("found %d uploads in %s" % (len(uploads), pname))

    if listflag:
        for item in uploads:
            print(item)
        return

    if rsamp:
        sample = random.sample(uploads, rsamp)
        rep.sample_size = len(sample)
        uploads = sample

    get_matches(rep, uploads, sleep, cache)


if __name__ == "__main__":
    DEFAULT_SLEEP = 5
    desc = "Get/sample matching upsearch results."
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("pname", help="file or directory pathname")
    argp.add_argument("dfile", help="output match data (dict) file")
    argp.add_argument("-c", "--cache", help="match data cache file")
    argp.add_argument("-l", "--list", action="store_true",
                      help="list uploads only")
    argp.add_argument("-r", "--rsamp", type=int, help="random sample size")
    argp.add_argument("-s", "--sleep", type=int, default=DEFAULT_SLEEP,
                      help="sleep seconds (default=%s)" % DEFAULT_SLEEP)
    args = argp.parse_args()

    rep = Reporter(args.dfile)
    try:
        print(time.ctime())
        main(rep, args.pname, args.list, args.rsamp, args.sleep, args.cache)
        rep.report()
    except KeyboardInterrupt:
        rep.report()
    # except Exception as e:
    #     print("Caught %s: %s" % (type(e).__name__, e))
    #     rep.report()

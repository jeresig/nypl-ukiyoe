from __future__ import print_function

import json
import os
import re
import sys


def get_prefix(fname):
    m = re.match(r'\d+', os.path.basename(fname))
    if m:
        return m.string[m.start():m.end()]


def dump(ldata, mdata):
    for key in sorted(ldata.keys()):
        print(json.dumps({"fname": key,
                          "matches": mdata[key],
                          "prefix": get_prefix(key),
                          "location": ldata[key]}))


def get_location_data(fname):
    data = {}
    with open(fname) as fp:
        for line in fp:
            fname, location = line.split('Location: ')
            fname = fname.replace('.upload', '').replace(':', '')
            location = location.strip()
            data[fname] = location
    return data


def get_match_data(fname):
    with open(fname) as fp:
        return eval(fp.read())


def peek(data, num=3):
    for key in sorted(data.keys())[:num]:
        print("%s %s" % (key, data[key]), file=sys.stderr)


def main(lfile, mfile):
    ldata = get_location_data(lfile)
    peek(ldata)
    mdata = get_match_data(mfile)
    peek(mdata)
    dump(ldata, mdata)


if __name__ == "__main__":
    main(lfile="locations.txt",
         mfile="cache_04MID.py")

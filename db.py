#!/usr/env/bin python

from __future__ import print_function

import pymongo

from pymongo import MongoClient


def peek(coll, num=3):
    srt = [("fname", pymongo.ASCENDING)]
    for item in coll.find().sort(srt)[:num]:
        print(item)


def main():
    client = MongoClient()
    db = client['nypl']
    coll = db.images
    peek(coll)


if __name__ == "__main__":
    main()

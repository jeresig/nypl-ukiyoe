#!/usr/bin/env python

"""upload images using Uploader."""

from __future__ import print_function

import argparse
import os

from uploader import Uploader

__author__ = "@siznax"
__version__ = "July 2016"


def upload(stack, upldr, limit):
    '''Uploader.upload(image) in stack up to limit'''
    count = 0
    for image in stack:
        upldr.upload(image)
        upldr.handle_response()
        count += 1
        if limit and count >= limit:
            return


def main(url, pname, sleep, verbose, dry, limit):
    '''see -help for argument details'''
    up = Uploader(url, sleep, verbose, dry)
    images = [pname]
    if os.path.isdir(pname):
        images = Uploader.findext(pname, '.jpg')
    upload(images, upldr=up, limit=limit)


if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("url", help="POST url")
    argp.add_argument("pname", help="image file or directory pathname")
    argp.add_argument("-d", "--dry", action="store_true",
                      help="dry run (skip upload)")
    argp.add_argument("-l", "--limit", type=int,
                      help="attempt limit")
    argp.add_argument(
        "-s", "--sleep", type=int,
        default=Uploader.DEFAULT_SLEEP,
        help="sleep seconds (default=%d)" % Uploader.DEFAULT_SLEEP)
    argp.add_argument("-v", "--verbose", action="store_true",
                      help="verbose logging")
    args = argp.parse_args()

    main(args.url, args.pname, args.sleep, args.verbose, args.dry, args.limit)

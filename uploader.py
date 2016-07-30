'''rerunnable, logging Uploader class.'''

import httplib
import json
import logging
import os
import requests
import sys
import time

__author__ = "@siznax"
__version__ = "July 2016"


class Uploader:
    '''
    a. image.jpg file not found
        [0] image.jpg NOT_FOUND
    b. ".upload" file exists
        [0] image.jpg UPLOADED
    c. upload success
        wrote image.jpg.upload
        [0] image.jpg 302 LOCATION
    d. upload failed
        wrote image.jpg.error
        [0] image.jpg 5XX ERROR
    e. request exception
        wrote image.jpg.error
        [0] image.jpg EXCEPTION
    '''

    DEFAULT_SLEEP = 60

    count = 0
    dry_run = False
    errfile = None
    infile = None
    response = None
    sleep = None
    status = None
    upfile = None
    url = None

    def __init__(self, url=None, sleep=None, verbose=False, dry=False):
        self.url = url
        self.sleep = sleep
        if sleep is None:
            self.sleep = self.DEFAULT_SLEEP
        if verbose:
            self.enable_requests_logging()
        if dry:
            self.dry_run = True
        self.setup_logger()
        self.logger.info("%s %s %s" % (__name__.upper(), time.ctime(),
                                       __file__))

    @staticmethod
    def enable_requests_logging():
        '''enables http_client and urllib debug messages'''
        httplib.HTTPConnection.debuglevel = 1
        rlog = logging.getLogger("requests.packages.urllib3")
        rlog.setLevel(logging.DEBUG)
        rlog.propagate = True

    @staticmethod
    def findext(root, ext):
        '''returns list files found by extension'''
        items = []
        for r, d, f in os.walk(root):
            for item in f:
                if item.endswith(ext):
                    path = os.path.normpath((os.sep).join([r, item]))
                    items.append(path)
        return items

    @staticmethod
    def get_headers_text(response, _type='text'):
        '''returns response headers as JSON or plain text'''
        if _type == 'json':
            return json.dumps(dict(response.headers),
                              indent=1, sort_keys=True,
                              separators=(',', ': '))
        h = dict(response.headers)
        return "\n".join(["%s: %s" % (x, h[x]) for x in sorted(h)])

    def handle_response(self):
        '''write .upload or .error file and append to log'''
        if self.response:
            response_code = self.response.status_code
            headers = self.get_headers_text(self.response)

            if "Location" in self.response.headers:
                self.status = "%s %s" % (response_code,
                                         self.response.headers['Location'])
                with open(self.upfile, 'w') as fp:
                    fp.write(headers + "\n")
                    self.logger.debug("wrote %s" % self.upfile)
            else:
                self.status = "%s %s" % (response_code, self.response.reason)
                self.write_error(headers)

        if 'exception' in self.status:
            self.write_error(self.status)

        self.logger.info("[%d] %s %s" % (self.count,
                                         self.infile,
                                         self.status))

    def setup_logger(self):
        '''setup logger for this instance'''
        logname = __name__
        logfile = __name__ + '.log'

        lgr = logging.getLogger(logname)
        lgr.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(name)s %(levelname)s: %(message)s')
        formatter = logging.Formatter('%(message)s')

        file_log = logging.FileHandler(logfile, mode='a')
        file_log.setLevel(logging.INFO)
        file_log.setFormatter(formatter)

        console_log = logging.StreamHandler(sys.stderr)
        console_log.setLevel(logging.DEBUG)
        console_log.setFormatter(formatter)

        lgr.addHandler(console_log)
        lgr.addHandler(file_log)
        self.logger = lgr

    def upload(self, fname):
        '''POST data or log NOT_FOUND, UPLOADED, DRY_RUN or Exception'''
        self.count += 1
        self.infile = fname
        self.upfile = fname + '.upload'
        self.errfile = fname + '.error'

        if not os.path.exists(fname):
            self.status = "NOT_FOUND"
            return

        if os.path.exists(self.upfile):
            self.status = "UPLOADED"
            return

        try:
            if self.sleep and self.response:
                self.logger.debug("sleeping %d seconds..." % self.sleep)
                time.sleep(self.sleep)

            if self.dry_run:
                self.status = "DRY_RUN"
                return

            # self.response = requests.get(self.url, verify=False)
            files = {'file': (fname, open(fname, 'rb'), 'image/jpeg')}
            self.response = requests.post(self.url,
                                          allow_redirects=False,
                                          # verify=False,
                                          files=files)
        except Exception as details:
            self.status = "Caught exception: %s" % details
            self.logger.debug(self.status)

    def write_error(self, msg):
        '''write Exception details or response headers'''
        with open(self.errfile, 'w') as fp:
            fp.write(msg + "\n")
            self.logger.debug("wrote %s" % self.errfile)

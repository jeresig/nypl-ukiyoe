#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''Tests for Uploader class.'''

import os
import requests
import unittest

TEST_UPLOADED = "uploader_tests/TEST_UPLOADED.jpg"
TEST_NOT_UPLOADED = "uploader_tests/TEST_NOT_UPLOADED.jpg"
TEST_ERROR_FILE = "uploader_tests/TEST_UPLOADED.error"
TEST_UPLOAD_FILE = "uploader_tests/TEST_NOT_UPLOADED.jpg.upload"


class UploadSuccessTestCase(unittest.TestCase):

    def test_upload_success(self):
        if os.path.exists(TEST_UPLOAD_FILE):
            msg = "TEST_UPLOAD_FILE exists: %s" % TEST_UPLOAD_FILE
            raise self.failureException(msg)

        from upload import Uploader
        up = Uploader("https://ukiyo-e.org/")
        up.infile = TEST_NOT_UPLOADED
        up.upfile = TEST_UPLOAD_FILE
        up.response = requests.Response()
        up.response.headers = {'Location': "LOCATION"}
        up.response.status_code = 302
        up.handle_response()

        self.assertTrue(os.path.exists(TEST_UPLOAD_FILE))

        os.remove(TEST_UPLOAD_FILE)


class UploadFailedTestCase(unittest.TestCase):

    def test_upload_failed(self):
        if os.path.exists(TEST_ERROR_FILE):
            msg = "TEST_ERROR_FILE exists: %s" % TEST_ERROR_FILE
            raise self.failureException(msg)

        from upload import Uploader
        up = Uploader("https://ukiyo-e.org/")
        up.infile = TEST_NOT_UPLOADED
        up.errfile = TEST_ERROR_FILE
        up.response = requests.Response()
        up.response.status_code = 600
        up.handle_response()

        if not os.path.exists(TEST_ERROR_FILE):
            self.assertTrue(os.path.exists(TEST_ERROR_FILE))

        os.remove(TEST_ERROR_FILE)


class FileNotFoundTestCase(unittest.TestCase):

    def test_file_not_found(self):
        from upload import Uploader
        up = Uploader()
        try:
            up.upload("bogus")
        except SystemExit:
            pass
        except:
            self.failureException("FAIL")


class UploadExistsTestCase(unittest.TestCase):

    def test_upload_exists(self):
        from upload import Uploader
        up = Uploader()
        up.upload(TEST_UPLOADED)
        up.handle_response()
        self.assertTrue('UPLOADED' in up.status)


class BadRequestTestCase(unittest.TestCase):

    def test_bad_request(self):
        from upload import Uploader
        up = Uploader("badhost", 0)
        up.upload(TEST_NOT_UPLOADED)
        self.assertTrue('exception' in up.status)


if __name__ == '__main__':
    unittest.main()

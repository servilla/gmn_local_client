#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_file_hash

:Synopsis:

:Author:
    servilla
  
:Created:
    8/14/15
"""

__author__ = 'servilla'

from tests import config

import logging
logger = logging.getLogger('tests.test_file_hash')
logger.setLevel(logging.DEBUG)

import unittest

from d1_actions.file_hash import file_hash

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fn = config.get('Tests', 'test_file')
        self.file_sha1 = '2b9dcb56e7bdf7057ead3160fdb9bbc952a1fc02'
        self.file_md5 = 'a10455a9623a90d49ae88de54cdbe5e1'

    def tearDown(self):
        pass

    def testFileSha1(self):
        try:
            file_sha1 = file_hash(self.fn, hash='sha1')
        except ValueError as e:
            self.assertRaises(e)
        else:
            self.assertTrue(file_sha1 == self.file_sha1)

    def testFileMd5(self):
        try:
            file_md5 = file_hash(self.fn, hash='md5')
        except ValueError as e:
            self.assertRaises(e)
        else:
            self.assertTrue(file_md5 == self.file_md5)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_obj

:Synopsis:

:Author:
    servilla
  
:Created:
    8/14/15
"""

__author__ = 'servilla'

import unittest
import logging

from d1_actions.file_hash import file_hash

logger = logging.getLogger('tests.test_file_hash')

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.file_name = '/home/servilla/PycharmProjects/gmn_local_client/data/NIN/knb-lter-nin.0.1.xml'
        self.file_sha1 = '2b9dcb56e7bdf7057ead3160fdb9bbc952a1fc02'
        self.file_md5 = 'a10455a9623a90d49ae88de54cdbe5e1'

    def tearDown(self):
        pass

    def test_file_sha1(self):
        try:
            file_sha1 = file_hash(self.file_name, hash='sha1')
        except ValueError as e:
            self.assertRaises(e)
        else:
            self.assertTrue(file_sha1 == self.file_sha1)

    def test_file_md5(self):
        try:
            file_md5 = file_hash(self.file_name, hash='md5')
        except ValueError as e:
            self.assertRaises(e)
        else:
            self.assertTrue(file_md5 == self.file_md5)


if __name__ == '__main__':
    unittest.main()

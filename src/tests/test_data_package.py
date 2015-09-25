#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_data_package

:Synopsis:

:Author:
    servilla
  
:Created:
    9/25/15
"""

__author__ = 'servilla'

import logging
logger = logging.getLogger('tests.test_file_hash')

import unittest

from eml_data_package import data_package

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.file_name = '/home/servilla/PycharmProjects/gmn_local_client/data/NIN/knb-lter-nin.0.1.xml'

    def tearDown(self):
        pass

    def test_data_package(self):
        dp = data_package.DataPackage(self.file_name)
        logger.warn("Hi")


if __name__ == '__main__':
    unittest.main()
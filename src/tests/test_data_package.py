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
logger.setLevel(logging.DEBUG)

import unittest

from eml_data_package import data_package

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.file_name = '/home/servilla/PycharmProjects/gmn_local_client/data/NIN/knb-lter-nin.0.1.xml'
        self.dp = data_package.DataPackage(self.file_name)
        self.packageId = 'knb-lter-nin.0.1'
        self.title = 'Meteorological data for North Inlet Estuary, South Carolina, from 1982 to 1982, North Inlet LTER'

    def tearDown(self):
        pass

    def test_package_id(self):
        packageId = self.dp.getPackageId()
        self.assertEqual(self.packageId, packageId)

    def test_title(self):
        title = self.dp.getTitle()
        self.assertEqual(self.title, title)

if __name__ == '__main__':
    unittest.main()

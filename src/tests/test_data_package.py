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

from tests import config

import logging
logger = logging.getLogger('tests.test_file_hash')
logger.setLevel(logging.DEBUG)

import unittest

from eml_data_package import data_package

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fn = config.get('Tests', 'test_file')
        self.package_id = config.get('Tests', 'test_pid')
        self.title = config.get('Tests', 'test_title')
        self.dp = data_package.DataPackage(self.fn)

    def tearDown(self):
        pass

    def test_package_id(self):
        package_id = self.dp.get_packageId()
        self.assertEqual(self.package_id, package_id)

    def test_title(self):
        title = self.dp.get_title()
        self.assertEqual(self.title, title)

if __name__ == '__main__':
    unittest.main()

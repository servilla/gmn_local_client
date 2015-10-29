#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_d1_sysmeta

:Synopsis:

:Author:
    servilla
  
:Created:
    10/28/15
"""

__author__ = 'servilla'

from tests import config # This is effectively "from __init__ import config"

import logging
logger = logging.getLogger('tests.test_d1_sysmeta')
logger.setLevel(logging.DEBUG)

import unittest

from d1_actions import d1_sysmeta


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fn = config.get('Tests', 'test_file')
        self.hash_algorithm = config.get('Tests', 'test_hash_alg')
        self.hash_value = config.get('Tests', 'test_hash_val')
        self.sm = d1_sysmeta.SysMeta(self.fn)

    def tearDown(self):
        pass

    def test_file_name(self):
        self.assertEqual(self.fn, self.fn)

    def test_hash_alg(self):
        self.assertEqual(self.sm.get_hash_algorithm(), self.hash_algorithm)

    def test_hash_value(self):
        self.assertEqual(self.sm.get_hash_value(), self.hash_value)


if __name__ == '__main__':
    unittest.main()

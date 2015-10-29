#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_data_table

:Synopsis:

:Author:
    servilla
  
:Created:
    9/27/15
"""

__author__ = 'servilla'

from tests import config # This is effectively "from __init__ import config"

import logging
logger = logging.getLogger('tests.test_file_hash')
logger.setLevel(logging.DEBUG)

import unittest

from eml_data_package import data_package
from eml_data_package import data_table

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fn = config.get('Tests', 'test_file')
        self.table_entityName = config.get('Tests', 'test_entity_name')
        self.table_physical_objectName = config.get('Tests', 'test_obj_name')
        self.table_count = config.getint('Tests', 'test_tbl_cnt')
        self.n_table = config.getint('Tests', 'test_ref_tbl')
        self.table_physical_count = config.getint('Tests', 'test_tbl_phys_cnt')
        self.n_physical = config.getint('Tests', 'test_ref_tbl_phys')
        self.dp = data_package.DataPackage(self.fn)
        self.dt = data_table.DataTable(self.dp.get_dataTable())

    def tearDown(self):
        pass

    def test_data_table_count(self):
        self.assertEqual(self.dt.get_table_count(), self.table_count)

    def test_data_table_entity_name(self):
        self.assertEqual(self.dt.get_table_entityName(self.n_table), self.table_entityName)

    def test_data_table_physical_count(self):
        self.assertEqual(self.dt.get_table_physical_count(self.n_table), self.table_physical_count)

    def test_data_table_physical_object_name(self):
        self.assertEqual(self.dt.get_table_physical_objectName(self.n_table, self.n_physical), self.table_physical_objectName)


if __name__ == '__main__':
    unittest.main()

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

import logging
logger = logging.getLogger('tests.test_file_hash')
logger.setLevel(logging.DEBUG)

import unittest

from eml_data_package import data_package
from eml_data_package import data_table

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.file_name = '/home/servilla/PycharmProjects/gmn_local_client/data/NIN/knb-lter-nin.0.1.xml'
        self.dp = data_package.DataPackage(self.file_name)
        self.dt = data_table.DataTable(self.dp.get_dataTable())
        self.table_count = 1
        self.n_table = 0
        self.table_entityName = 'MeteorologicalData-NIN-LTER-1982-1982'
        self.table_physical_count = 1
        self.n_physical = 0
        self.table_physical_objectName = 'LTER.NIN.MET.csv'

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

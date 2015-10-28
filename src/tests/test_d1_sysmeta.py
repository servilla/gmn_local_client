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

from eml_data_package import data_package
from eml_data_package import data_table


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fn = config.get('Tests', 'test_file')
        self.dp = data_package.DataPackage(self.fn)
        self.dt = data_table.DataTable(self.dp.get_dataTable())
        self.table_count = 1
        self.n_table = 0
        self.table_entityName = 'MeteorologicalData-NIN-LTER-1982-1982'
        self.table_physical_count = 1
        self.n_physical = 0
        self.table_physical_objectName = 'LTER.NIN.MET.csv'

    def tearDown(self):
        pass

    def test_file_name(self):
        self.assertEqual(self.fn, self.fn)


if __name__ == '__main__':
    unittest.main()

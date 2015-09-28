#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: data_table

:Synopsis:

:Author:
    servilla
  
:Created:
    9/25/15
"""

__author__ = "servilla"

class DataTable:

    def __init__(self, data_table):
        self.data_table = data_table
        pass

    def get_table_count(self):
        return len(self.data_table)

    def get_table_entityName(self, n_table):
        return self.data_table[n_table].entityName

    def get_table_physical_count(self, n_table):
        return len(self.data_table[n_table].physical)

    def get_table_physical_objectName(self, n_table, n_physical):
        return self.data_table[n_table].physical[n_physical].objectName


def main():
    return 0


if __name__ == "__main__":
    main()
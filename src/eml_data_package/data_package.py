#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: data_package

:Synopsis:
    Creates a data package based on an EML science metadata model.

:Author:
    servilla
  
:Created:
    9/24/15
"""

__author__ = "servilla"

import logging
logger = logging.getLogger('eml_data_package.data_package')

import pyxb

import eml2_1_0.eml2_1_0
import eml2_1_0._nsgroup

class DataPackage:

    def __init__(self, eml_path):
        self.eml_path = eml_path

        self.xml = open(self.eml_path).read()
        self.eml = eml2_1_0.eml2_1_0.CreateFromDocument(self.xml)

    def get_title(self):
        dataset = self.eml.dataset
        title_list = dataset.title
        title = ''
        for t in title_list:
            title += format('%s' % t)
        return title

    def get_packageId(self):
        package_id = self.eml.packageId
        return package_id

    def get_dataTable(self):
        dataset = self.eml.dataset
        return dataset.dataTable

def main():
    return 0


if __name__ == "__main__":
    main()
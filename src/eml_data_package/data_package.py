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

        # Prefetch required element content
        self.packageId = self._getPackageId(self.eml)
        self.title = self._getTitle(self.eml)

    def _getTitle(self, eml):
        dataset = eml.dataset
        title_list = dataset.title
        title = ''
        for t in title_list:
            title += format('%s' % t)
        return title

    def getTitle(self):
        return self.title

    def _getPackageId(self, eml):
        packageId = eml.packageId
        return packageId

    def getPackageId(self):
        return self.packageId

    def getDataTable(self, eml):
        return None

def main():

    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y%m%d-%H:%M:%S')
    dp = DataPackage('/home/servilla/PycharmProjects/gmn_local_client/data/NIN/knb-lter-nin.0.1.xml')

    return 0


if __name__ == "__main__":
    main()
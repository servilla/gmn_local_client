#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: file_iterator

:Synopsis:

:Author:
    servilla
  
:Created:
    8/28/15
"""

__author__ = "servilla"

import sys
import os
import ConfigParser
import eml2_1_0.eml2_1_0

def main():

    config_path ='../conf/gmn_local_client.conf'
    config = ConfigParser.ConfigParser()
    config.read(config_path)

    mp = config.get('Paths', 'metadata_path')
    dp = config.get('Paths', 'data_path')
    files = config.get('Files', 'metadata_files').split(',')

    xml = open('/home/servilla/PycharmProjects/gmn_local_client/data/NIN/knb-lter-nin.0.1.xml').read()
    eml = eml2_1_0.eml2_1_0.CreateFromDocument(xml)

    ds = eml.dataset
    ds_title = ds.title
    ds_tbl = ds.dataTable
    p = ds_tbl.physical

    print(ds_tbl)

    return 0


if __name__ == "__main__":
    main()
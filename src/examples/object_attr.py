#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: object_attr

:Synopsis:

:Author:
    servilla

:Created:
    8/14/15
"""

__author__ = "servilla"

import sys
from d1_actions.obj import Obj

def main():
    f = Obj('/home/servilla/PycharmProjects/gmn_local_client/data/NIN/knb-lter-nin.0.1.xml')
    print('Filename: %s' % f.file_name)
    print('Filesize: %d' % f.file_size)
    print('Filesha1: %s' % f.file_sha1)

    print(sys.path)

    return 0


if __name__ == "__main__":
    main()
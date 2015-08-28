#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: obj

:Synopsis:

:Author:
    servilla
  
:Created:
    8/14/15
"""

__author__ = "servilla"

import os
import hashlib

class Obj(object):
    """Container for file object information necessary for DataONE"""

    def __init__(self, file_name):
        """Obj constructor.

        :param file_name:
        :return: None
        """
        self.file_name = file_name
        self.file_size = os.stat(file_name).st_size
        self.file_sha1 = self._hash_file(file_name)

    @staticmethod
    def _hash_file(file_path):
        sha1 = hashlib.sha1()
        f = open(file_path, 'rb')
        try:
            sha1.update(f.read())
        finally:
            f.close()
        return sha1.hexdigest()



def main():
    return 0


if __name__ == "__main__":
    main()
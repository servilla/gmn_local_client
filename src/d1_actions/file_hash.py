#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: file_hash

:Synopsis:
    Return the hash value of the specified file
:Author:
    servilla
  
:Created:
    8/25/15
"""

__author__ = "servilla"

import io
import logging
import hashlib

logger = logging.getLogger('d1_actions.file_hash')

def file_hash(path, hash='sha1'):
    """Return the file hash

        Returns the hash value of the specified file. Hash scheme defaults to
        SHA-1.

    :param path:
        Path to file
    :param hash:
        Hash scheme
    :return:
        Hash string
    """

    try:
        f = io.open(path, 'rb')
    except IOError as e:
        logger.error("IOError - %s" % e)
        raise e

    try:
        hash_value = ''
        if hash in ('SHA1', 'sha1', 'SHA-1', 'sha-1'):
            hash_value = _hash_file_sha1(f)
        elif hash in ('MD5', 'md5'):
            hash_value = _hash_file_md5(f)
        else:
            raise ValueError("Unsupported hash type '%s'" % hash)
    except ValueError as e:
        logger.exception(e)
    else:
        return hash_value
    finally:
        f.close()

def _hash_file_sha1(f):
    """Return SHA-1 file hash

    :param f:
        File handle
    :return:
        SHA-1 hash
    """
    sha1 = hashlib.sha1()
    sha1.update(f.read())
    return sha1.hexdigest()


def _hash_file_md5(f):
    """Return MD5 file hash

    :param f:
        File handle
    :return:
        MD5 hash
    """
    md5 = hashlib.md5()
    md5.update(f.read())
    return md5.hexdigest()


def main():
    return 0


if __name__ == "__main__":
    main()
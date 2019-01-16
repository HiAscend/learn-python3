#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import fnmatch
import os


def allFiles(root, patterns='*', single_level=False, yield_folders=False):
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            # add subdirs to the tail of files
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break
        # only deal one level of the dir
        if single_level:
            break


pwd = os.path.abspath('.')
for name in allFiles(pwd, single_level=False):
    print(name)



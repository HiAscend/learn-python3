#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
import os


def search(path):
    pwd = os.path.abspath(path)
    for f in os.listdir(pwd):
        if os.path.isdir(f):
            search(os.path.join(path, f))
        else:
            print(f)


# search('.')



# for f in os.listdir(os.path.abspath('Z:/tmp')):
#     print(f, os.path.isdir(f))

# pwd = os.path.abspath('.')
# print(pwd)
# print(os.path.isdir(pwd))
# print(os.path.isdir('Z:/tmp/test.txt'))


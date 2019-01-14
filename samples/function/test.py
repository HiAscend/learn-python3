#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def findminandmax(L):
    if L is None or L == []:
        return None, None
    else:
        mi = L[0]
        ma = L[0]
        for item in L:
            if item < mi:
                mi = item
            if item > ma:
                ma = item
        return mi, ma


# 测试
if findminandmax([]) != (None, None):
    print('测试失败!')
elif findminandmax([7]) != (7, 7):
    print('测试失败!')
elif findminandmax([7, 1]) != (1, 7):
    print('测试失败!')
elif findminandmax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')




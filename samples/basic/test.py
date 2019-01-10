#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


t = move(100, 100, 60, int(math.pi / 6))
print(t[0])


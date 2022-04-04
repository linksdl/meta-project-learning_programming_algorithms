"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/25 15:59
@File        : HJ108 求最小公倍数2.py
"""


# HJ108 求最小公倍数


def lcm(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return a * b // i


print(lcm(4, 8))




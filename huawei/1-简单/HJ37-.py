"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 23:00
@File        : HJ37-.py
"""


def countRabbits(n):
    count = 0
    if n <= 2:
        count += 1
        return count
    count += countRabbits(n-1) + countRabbits(n-2)
    return count

n = int(input())
print(countRabbits(n))

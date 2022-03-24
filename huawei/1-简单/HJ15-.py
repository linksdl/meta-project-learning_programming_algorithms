"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 20:32
@File        : HJ15-.py
"""


def binaryCount(num):
    count = 0
    while num > 0:
        if num % 2:
            count += 1
        num //= 2
    return count


num = input().strip()
num = int(num)
print(binaryCount(num))




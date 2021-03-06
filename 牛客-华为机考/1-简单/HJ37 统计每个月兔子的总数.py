"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 23:00
@File        : HJ37 统计每个月兔子的总数.py
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

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:07
@File        : add4.py
"""

# 4 1 2 3 4
# 5 1 2 3 4 5
# 0

def fn_sum(nums):
    return sum(nums)
while True:
    try:
        lines = list(map(int, input().split()))
        if lines[0]==0 and len(lines) == 1:
            break
        print(fn_sum(lines[1:]))
    except:
        break

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:19
@File        : add8.py
"""

# 输入例子1:
# 5
# c d a bb e

while True:
    try:
        n = int(input())
        str = list(map(str, input().split()))
        sorted_str = sorted(str)

        print(' '.join(sorted_str))
    except:
        break



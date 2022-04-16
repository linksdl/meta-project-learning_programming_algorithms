"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:15
@File        : add7.py
"""

# 1 2 3
# 4 5
# 0 0 0 0 0

while True:
    try:
        lines = list(map(int, input().split()))
        print(sum(lines))
    except:
        break



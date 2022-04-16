"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:12
@File        : add5.py
"""
#

# 2
# 4 1 2 3 4
# 5 1 2 3 4 5


while True:
    try:
        n = int(input())
        for i in range(n):
            lines = list(map(int, input().split()))
            print(sum(lines[1:]))
    except:
        break

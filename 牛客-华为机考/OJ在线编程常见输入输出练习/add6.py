"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:14
@File        : add6.py
"""
#
# 输入例子1:
# 4 1 2 3 4
# 5 1 2 3 4 5

while True:
    try:
        lines = list(map(int, input().split()))
        print(sum(lines[1:]))
    except:
        break

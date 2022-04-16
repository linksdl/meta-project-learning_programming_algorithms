"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:23
@File        : add9.py
"""
#
# 输入例子1:
# a c bb
# f dddd
# nowcoder

while True:
    try:
        strs = list(map(str, input().split()))
        sorted_strs = sorted(strs)

        print(' '.join(sorted_strs))

    except:
        break

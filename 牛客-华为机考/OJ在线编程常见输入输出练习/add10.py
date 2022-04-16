"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:27
@File        : add10.py
"""


while True:
    try:
        strs = list(map(str, input().split(',')))
        sorted_strs = sorted(strs)

        print(','.join(sorted_strs))

    except:
        break



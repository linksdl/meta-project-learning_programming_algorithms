"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:30
@File        : add11.py
"""



# 输入例子1:
# 1 1
#
# 输出例子1:
# 2


while True:
    try:
        lines = list(map(int, input().split()))
        res = lines[0] + lines[1]
        print(res)

    except:
        break

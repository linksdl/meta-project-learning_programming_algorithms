"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 22:57
@File        : add3.py
"""
#
# 1 5
# 10 20
# 0 0

def add(a, b):
    return(a+b)

while True:
    try:
        line = list(map(int, input().split()))
        if not line[0] == 0 and not line[1] == 0:
            print(add(line[0], line[1]))
    except:
        break



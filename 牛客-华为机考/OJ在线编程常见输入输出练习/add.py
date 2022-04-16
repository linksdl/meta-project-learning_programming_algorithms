"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 22:48
@File        : add.py
"""
#
# 1 5
# 10 20

def add(a, b):
    return (a + b)

while True:
    try:
        line = input().split()
        num1, num2 = int(line[0]), int(line[1])
        print(add(num1, num2))
    except:
        break




"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/22 16:58
@File        : demo.py
"""


def dfs(arr):
    if not arr:
        return None

    max_v = arr[0]
    max_i = 0
    for i in range(len(arr)):
        if arr[i] > max_v:
            max_v = arr[i]
            max_i = i
    arr[max_i] = 0

    return max_i


def findMaxk(arr, k):

    n = len(arr)
    max_v = [0] * k
    max_i = []
    for i in range(k):
        max_i.append(dfs)

    print(max_i)



arr = [1, 23, 3, 4, 5, 2, 6, 3, 46, 2]
findMaxk(arr, 1)

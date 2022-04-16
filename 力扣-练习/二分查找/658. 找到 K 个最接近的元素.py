"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 17:40
@File        : 658. 找到 K 个最接近的元素.py
"""


# 找到 K 个最接近的元素


def findClosestElements(arr, k, x):
    """
    找到 K 个最接近的元素
    :param arr:
    :param k:
    :param x:
    """
    left, right = 0, len(arr) - k
    while left < right - 1:
        mid = left + (right - left) // 2
        a, b = arr[mid], arr[mid + k - 1]
        if a >= x:
            right = mid
        elif b <= x:
            left = mid
        elif abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b):
            right = mid
        else:
            left = mid

    if left == right:
        return arr[left: left + k]
    else:
        a, b = arr[left], arr[right + k - 1]
        if abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b):
            return arr[left: left + k]
        else:
            return arr[right: right + k]





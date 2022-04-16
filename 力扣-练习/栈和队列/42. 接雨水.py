"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 14:26
@File        : 42. 接雨水.py
"""


def trap(height):

    res = 0
    left_max = 0
    right_max = 0
    left = 0
    right = len(height) - 1

    while left <= right:
        if left_max <= right_max:
            left_max = max(left_max, height[left])
            res += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            res += right_max - height[right]
            right -= 1
    return res



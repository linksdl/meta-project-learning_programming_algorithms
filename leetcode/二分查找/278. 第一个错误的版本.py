"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 15:49
@File        : 278. 第一个错误的版本.py
"""

# 278. 第一个错误的版本
# https://leetcode-cn.com/problems/first-bad-version/

def firstBadVersion(self, n):
    """
    278. 第一个错误的版本
    :type n: int
    :rtype: int
    """
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

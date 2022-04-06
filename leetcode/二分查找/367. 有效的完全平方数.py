"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 19:53
@File        : 367. 有效的完全平方数.py
"""


# 有效的完全平方数

# 方法一：使用内置的库函数
# 方法二：暴力
# 方法三：二分查找
# 方法四：牛顿迭代法

def isPerfectSquare(num):
    """
    有效的完全平方数
    :param num:
    :return:
    """
    if num == 1:
        return True

    left, right = 0, num // 2
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid < num:
            left = mid + 1
        else:
            right = mid
    return True if left * left == num else False


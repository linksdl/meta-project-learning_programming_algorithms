"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 13:09
@File        : 69. x 的平方根.py
"""


# 给你一个非负整数 x ，计算并返回x的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

def mySqrt(x):
    """
    x 的平方根
    :param x:
    """

    if x < 2:
        return x

    left, right = 1, x
    while left <= right:
        mid = (right - left) // 2 + left
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid

    return left if left * left <= x else left - 1


res = mySqrt(5)
print(res)






"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 19:44
@File        : 50. Pow(x, n).py
"""

# 50. Pow(x, n)


# 方法一：快速幂 + 递归
def myPow(x, n):
    """
    方法一：快速幂 + 递归
    :param x:
    :param n:
    :return:
    """
    def quickMul(N):
        if N == 0:
            return 1.0

        y = quickMul(N//2)
        return y * y if N % 2 == 0 else y * y * x

    return quickMul(n) if n >= 0 else 1.0/quickMul(-n)

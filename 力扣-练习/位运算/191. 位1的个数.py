"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 22:52
@File        : 191. 位1的个数.py
"""


# https://leetcode-cn.com/problems/number-of-1-bits/

# 方法一：循环检查二进制位
def hammingWeight(n):
    """
    位1的个数
    :param n:
    :return:
    """
    ret = sum(1 for i in range(32) if n & (1 << i))
    return ret

# 方法二：位运算优化
def hammingWeight1(n):
    """
    位1的个数
    :param n:
    :return:
    """
    ret = 0
    while n:
        n &= n - 1
        print(n)
        ret += 1

    return ret

# hammingWeight1(11111111111111111111111111111101)

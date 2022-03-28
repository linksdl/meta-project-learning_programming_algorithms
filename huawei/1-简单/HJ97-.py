"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 21:24
@File        : HJ97-.py
"""


# HJ97 记负均正

# 描述
# 首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。
# 0即不是正整数，也不是负数，不计入计算。如果没有正数，则平均值为0。


def conutPostiveInteger(n, nums):
    """
    HJ97 记负均正
    :param n:
    :param nums:
    """
    sum_ = []
    avg = 0.0
    count = 0
    l = 0
    for i in nums:
        if i > 0:
            sum_.append(i)
            l += 1
        if i < 0:
            count += 1
    if sum != 0 and l > 0:
        avg = round(sum(sum_) / l, 1)
    print(count, avg)


n = int(input())
nums = list(map(int, input().split()))

conutPostiveInteger(n, nums)

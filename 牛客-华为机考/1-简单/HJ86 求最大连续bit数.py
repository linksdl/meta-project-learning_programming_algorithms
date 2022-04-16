"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 10:26
@File        : HJ86 求最大连续bit数.py
"""


# 描述
# 求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
#
# 数据范围：数据组数：1\le t\le 5\1≤t≤5 ，1\le n\le 500000\1≤n≤500000
# 进阶：时间复杂度：O(logn)\O(logn) ，空间复杂度：O(1)\O(1)
# 输入描述：
# 输入一个int类型数字
#
# 输出描述：
# 输出转成二进制之后连续1的个数


def countBits(n):
    """
    求一个int类型数字对应的二进制数字中1的最大连续数
    :param n:
    :return:
    """

    if n == 0:
        print(0)

    bits = []
    max_bit = 0
    while n:
        count = 0
        while n & 1 == 1:
            count += 1
            n >>= 1

        if count > max_bit:
            max_bit = count
        n >>= 1

    print(max_bit)


countBits(15)


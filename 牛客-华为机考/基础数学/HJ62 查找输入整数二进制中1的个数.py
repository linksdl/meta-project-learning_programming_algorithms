"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 09:54
@File        : HJ62 查找输入整数二进制中1的个数.py
"""


# HJ62 查找输入整数二进制中1的个数


def countOne(n):
    """
    HJ62 查找输入整数二进制中1的个数
    :param n:
    :return:
    """
    if n == 0:
        print(0)

    count = 1
    while n / 2 > 1:
        if n % 2 == 1:
            count += 1
        n //= 2

    print(count)

countOne(64)


bin(12)


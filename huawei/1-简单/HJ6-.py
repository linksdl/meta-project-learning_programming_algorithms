"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 17:40
@File        : HJ6-.py
"""
import math


def splitFactor(num):
    """
    描述
    功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
    数据范围： 1 \le n \le 2 \times 10^{9} + 14 \1≤n≤2×10 9+14
    输入描述：
    输入一个整数
    输出描述：
    按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
    :param num:
    :return:
    """
    factors = []
    num = int(num)
    for i in range(2, int(int(math.sqrt(num))+1)):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 2:
        factors.append(num)

    print(' '.join([str(s) for s in factors]))


splitFactor(121*11*180)

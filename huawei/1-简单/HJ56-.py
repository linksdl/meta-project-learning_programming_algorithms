"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 21:00
@File        : HJ56-.py

"""
# HJ56 完全数计算

# 描述
# 完全数（Perfect
# number），又称完美数或完备数，是一些特殊的自然数。
#
# 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
#
# 例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1 + 2 + 4 + 7 + 14 = 28。

import numpy as np


def factor_f(n):
    fc = []
    for i in range(1, int(n // 2) + 1):
        if n % i == 0:
            # print(i)
            fc.append(i)
    val = sum(fc)
    if val == n:
        return True

    return False


# print(factor_f(28))

count = 0
n = 1000
for i in range(1, n+1):
    if factor_f(i):
        print(i)
        count+= 1

print(count)

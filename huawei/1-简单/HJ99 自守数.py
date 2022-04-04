"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 21:12
@File        : HJ99 自守数.py
"""

# HJ99 自守数

# 描述
# 自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n(包括n)以内的自守数的个数
#
# 数据范围： 1 \le n \le 10000 \1≤n≤10000

import numpy as np


def zishou_num(n):
    """
    自守数是指一个数的平方的尾数等于该数自身的自然数。
    :param n:
    """
    s = str(n)
    new_num = n ** 2
    ss = str(new_num)
    print(s, ss, ss[-len(s)::])

    if s in ss[-len(s)::]:
        return True

    return False


print(zishou_num(76))








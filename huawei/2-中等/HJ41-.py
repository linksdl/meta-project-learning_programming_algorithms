"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 23:22
@File        : HJ41-.py
"""


def weightNums(n, m, x):
    """

    :param n:
    :param m:
    :param x:
    """
    weights = {0,}
    amount = []
    for i in range(n):
        for j in range(x[i]):
            amount.append(m[i])

    for i in amount:
        for j in list(weights):
            weights.add(i+j)

    return weights


print(len(weightNums(3, [1, 2, 3], [1, 2, 4])))

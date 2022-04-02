"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/2 09:51
@File        : HJ69-矩阵乘法.py
"""


# HJ69 矩阵乘法


def matrixMutil(x, y, z, m, n):
    """
    HJ69 矩阵乘法
    :param m:
    :param n:
    :return:
    """
    # m  x * y
    # n  y * z
    # o  x * z
    o = [[0] * z for _ in range(x)]
    #     print(o)
    c = 0
    for i in range(x):
        for j in range(z):
            for k in range(y):
                o[i][j] += m[i][k] * n[k][j]

    #     print(o)
    for line in o:
        print(*line)


matrixMutil(3, 2, 3, [[1, 1],[1, 1], [1, 1]], [[2, 2, 2],[2, 2, 2]])

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 22:38
@File        : HJ35 蛇形矩阵.py
"""

# 描述
# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
#
# 例如，当输入5时，应该输出的三角形为：
#
# 1 3 6 10 15
#
# 2 5 9 14
#
# 4 8 13
#
# 7 12
#
# 11
#
#
# 输入描述：
# 输入正整数N（N不大于100）
#
# 输出描述：
# 输出一个N行的蛇形矩阵。

def printSnake(n):
    if n == 1:
        print(n)
    else:
        for i in range(1, n+1):
            for j in range(1, n - i + 2):
                if j == n - i + 1:
                    print((i + j - 2) * (i + j - 1) // 2 + j)
                else:
                    print((i + j - 2) * (i + j - 1) // 2 + j, end=" ")

printSnake(4)

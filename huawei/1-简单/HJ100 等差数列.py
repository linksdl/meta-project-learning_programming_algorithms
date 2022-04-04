"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 22:09
@File        : HJ100 等差数列.py
"""


# HJ100 等差数列

# 描述
# 等差数列 2，5，8，11，14。。。。
# （从 2 开始的 3 为公差的等差数列）
# 输出求等差数列前n项和
#
#
# 数据范围： 1 \le n \le 1000 \1≤n≤1000
# 输入描述：
# 输入一个正整数n。
#
# 输出描述：
# 输出一个相加后的整数。


def sumInteger(n, c):
    if n == 1:
        return 2
    return sumInteger(n - 1, c) + c

sum = 0
n = 275
c = 3
for i in range(1, n+1):
    sum += sumInteger(i, c)

print(sum)


# def func(a0,d,n):
#     an = a0 + (n - 1) * d
#     return (a0 + an)/2*n
#
# while True:
#     try:
#         a = int(input())
#         b = func(2,3,a)
#         print(int(b))
#     except:
#         break

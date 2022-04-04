"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/25 15:59
@File        : HJ108 求最小公倍数2.py
"""


# HJ108 求最小公倍数
import math


def getFactors(num):
    """
    求因子
    :param num:
    """
    factors = []
    for i in range(2, int(int(math.sqrt(num))+1)):
        while num % i == 0:
            factors.append(i)
            num //= i

    if num > 2:
        factors.append(num)

    return factors

num1 = 18
num2 = 28
a = getFactors(num1)
b = getFactors(num2)
print('a的因子：', a)
print('b的因子：', b)

# 公有质因数
f = []
for v in a:
    if v in b and v not in f:
        f.append(v)

print('公共因子：', f)
for fc in f:
    if fc in a:
        a.remove(fc)
    if fc in b:
        b.remove(fc)

nums = f + a + b
print(f)
# print(a)
# print(b)
# print(nums)
r = 1
for number in nums:
    r *= number

print(min(max(num1, num2), r))



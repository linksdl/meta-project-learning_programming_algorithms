"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 12:13
@File        : HJ60-查找组成一个偶数最接近的两个素数.py
"""

# 描述
# 任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。
#
# 数据范围：输入的数据满足 4 \le n \le 1000 \4≤n≤1000

# 输入描述：
# 输入一个大于2的偶数
#
# 输出描述：
# 从小到大输出两个素数


def isPrime(n):
    """
    判断是不是素数
    :param n:
    """
    if n <= 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


# print(isPrime(15))


n = 4
a = 0
b = 0
min_val = n
for i in range(2, int(n//2)+1):
    if isPrime(i) and isPrime(n-i):
        a, b = i, n-i
        if min_val < (b-a):
            min_val = (b-a)
print(a)
print(b)


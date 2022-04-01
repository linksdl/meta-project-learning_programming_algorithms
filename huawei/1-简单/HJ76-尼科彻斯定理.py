"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 15:08
@File        : HJ76-尼科彻斯定理.py
"""

# HJ76 尼科彻斯定理
# 验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
# 例如：
# 1^3=1
# 2^3=3+5
# 3^3=7+9+11
# 4^3=13+15+17+19
# 输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出。
# 数据范围：1\le m\le 100\1≤m≤100
# 进阶：时间复杂度：O(m)\O(m) ，空间复杂度：O(1)\O(1)


def deInteger(n):
    """
    HJ76 尼科彻斯定理
    :param n:
    :return:
    """

    s_n = n ** 3
    # print(s_n)
    d = 2
    # s_n = a1 * n + (n*(n-1)/2) * d
    a1 = n*n - (n-1)
    c = []
    for i in range(0, n):
        # print(a1 + 2 * i)
        c.append(a1 + 2*i)

    cc = [str(a) for a in c]
    print('+'.join(cc))

deInteger(4)

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 10:52
@File        : HJ55-挑7.py
"""


# HJ55 挑7


# 描述
# 输出 1到n之间 的与 7 有关数字的个数。
# 一个数与7有关是指这个数是 7 的倍数，或者是包含 7 的数字（如 17 ，27 ，37 ... 70 ，71 ，72 ，73...）

# 数据范围： 1 \le n \le 30000 \1≤n≤30000

# 输入描述：
# 一个正整数 n 。( n 不大于 30000 )
#
# 输出描述：
# 一个整数，表示1到n之间的与7有关的数字个数。



def fn_seven(n):
    """
    HJ55 挑7
    :param n:
    """
    count = 0
    for i in range(1, n+1):
        # 7的倍数
        if i % 7 == 0:
            count += 1
        # 包含7
        elif '7' in str(i):
            count += 1

    print(count)


fn_seven(20)

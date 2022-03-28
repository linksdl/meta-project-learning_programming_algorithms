"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 23:31
@File        : HJ84-.py
"""


# HJ84 统计大写字母个数

# 描述
# 找出给定字符串中大写字符(即'A'-'Z')的个数。
# 数据范围：字符串长度：1\le |s|\le 250\1≤∣s∣≤250
# 字符串中可能包含空格或其他字符
# 进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)
# 输入描述：
# 对于每组样例，输入一行，代表待统计的字符串
#
# 输出描述：
# 输出一个整数，代表字符串中大写字母的个数


def conutUpper(str):

    count = 0
    for s in str:
        if s.isupper():
            count += 1
    return count


print(conutUpper('A 1 0 1 1150175017(&^%&$vabovbaoadd 123#$%#%#O'))

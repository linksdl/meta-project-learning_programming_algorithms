"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/29 22:58
@File        : HJ65-查找两个字符串a,b中的最长公共子串.py
"""


# HJ65 查找两个字符串a,b中的最长公共子串

# 查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
# 注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
#
# 数据范围：字符串长度1\le length \le300 \1≤length≤300
# 进阶：时间复杂度：O(n^3)，空间复杂度：O(n)
# 输入描述：
# 输入两个字符串
#
# 输出描述：
# 返回重复出现的字符


def commonSubStr(a, b):
    """
    HJ65 查找两个字符串a,b中的最长公共子串
    :param a:
    :param b:
    """
    m = len(a)
    n = len(b)

    max_len = 0
    max_sub_str = ''
    if m <= n:
        for w in range(2, m + 1):
            for i in range(0, m - w + 1):
                s = a[i:(i + w)]
                if s in b:
                    if w > max_len:
                        max_sub_str = s
                        max_len = w
    else:
        for w in range(2, n + 1):
            for i in range(0, n - w + 1):
                s = b[i:(i + w)]
                if s in a:
                    if w > max_len:
                        max_sub_str = s
                        max_len = w

    print(max_sub_str)


commonSubStr('abcdefghijklmnop', 'abcsafjklmnopqrstuvw')

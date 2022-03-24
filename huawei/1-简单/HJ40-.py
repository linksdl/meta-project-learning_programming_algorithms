"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 23:13
@File        : HJ40-.py
"""


def countStr(str):
    """
    输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

    数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000

    输入描述：
    输入一行字符串，可以有空格

    输出描述：
    统计其中英文字符，空格字符，数字字符，其他字符的个数
    :param str:
    """
    l = [0, 0, 0, 0]
    for s in str:
        l[0] += int(s.isalpha())
        l[1] += int(s == ' ')
        l[2] += int(s.isnumeric())
    l[3] = len(str) - l[0] - l[1] - l[2]

    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])


str = input()
countStr(str)

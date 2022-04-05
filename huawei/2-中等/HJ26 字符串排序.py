"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 11:30
@File        : HJ26 字符串排序.py
"""


# HJ26 字符串排序

# 描述
# 编写一个程序，将输入字符串中的字符按如下规则排序。
#
# 规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
#
# 如，输入： Type 输出： epTy
#
# 规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
#
# 如，输入： BabA 输出： aABb
#
# 规则 3 ：非英文字母的其它字符保持原来的位置。
#
#
# 如，输入： By?e 输出： Be?y
#
# 数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000
#
# 输入描述：
# 输入字符串
# 输出描述：
# 输出字符串


def orderStr(s):
    """
    HJ26 字符串排序
    :param s:
    :return:
    """

    out_s = ''
    d = []
    for i in range(len(s)):
        if s[i].isalpha():
            d.append((s[i], i, ord(s[i].lower())))
    d.sort(key=lambda x:(x[2], x[1]))
    # print(d)

    f = 0
    for i in range(len(s)):
        if s[i].isalpha():
            out_s += d[f][0]
            f += 1
        else:
            out_s += s[i]

    print(out_s)


orderStr('BabA')

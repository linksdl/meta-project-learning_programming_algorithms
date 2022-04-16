"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 18:40
@File        : HJ14 字符串排序.py
"""
# 描述
# 给定 n 个字符串，请对 n 个字符串按照字典序排列。
#
# 数据范围： 1 \le n \le 1000 \1≤n≤1000  ，字符串长度满足 1 \le len \le 100 \1≤len≤100
# 输入描述：
# 输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
# 输出描述：
# 数据输出n行，输出结果为按照字典序排列的字符串。


def sort(wa, wb):
    """
    单词内部排序
    :param wa:
    :param wb:
    :return:
    """
    for i in range(min(len(wa), len(wb))):
        if ord(wa[i]) < ord(wb[i]):
            return 1
        elif ord(wa[i]) > ord(wb[i]):
            return 0
        else:
            continue
    if len(wa) <= len(wb):
        return 1
    else:
        return 0


def orderStrings(strs):
    """
    描述
    给定 n 个字符串，请对 n 个字符串按照字典序排列。
    数据范围： 1 \le n \le 1000 \1≤n≤1000  ，字符串长度满足 1 \le len \le 100 \1≤len≤100
    输入描述：
    输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
    输出描述：
    数据输出n行，输出结果为按照字典序排列的字符串。
        :param strs:
    :return:
    """
    for i in range(len(strs)-1):
        for j in range(i+1, len(strs)):
            if not sort(strs[i], strs[j]):
                tmp = strs[i]
                strs[i] = strs[j]
                strs[j] = tmp

    return strs


print(orderStrings(['boat','boot','to','two', 'too']))







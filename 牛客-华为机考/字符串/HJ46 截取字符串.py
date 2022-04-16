"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 15:22
@File        : HJ46 截取字符串.py
"""


def subString(str, k):
    """
    描述
    输入一个字符串和一个整数 k ，截取字符串的前k个字符并输出
    数据范围：字符串长度满足 1 \le n \le 1000 \1≤n≤1000  ， 1 \le k \le n \1≤k≤n
    输入描述：
        1.输入待截取的字符串
        2.输入一个正整数k，代表截取的长度
    输出描述：
    截取后的字符串
    :param str:
    :return:
    """
    l = len(str)
    if k >= l:
        return str
    else:
        return str[0:k]


print(subString('Asdsff', 3))

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 16:54
@File        : HJ4-SplitString.py
"""


def splitString(str):
    """
    描述
    •连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；

    •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
    输入描述：
    连续输入字符串(每个字符串长度小于等于100)

    输出描述：
    依次输出所有分割后的长度为8的新字符串
    :param str:
    """
    l = len(str)
    m = l // 8
    n = l % 8
    for i in range(m):
        print(str[i * 8:(i + 1) * 8])
    if n != 0:
        print(str[-n:] + '0' * (8 - n))


splitString('dddddddhdabc')

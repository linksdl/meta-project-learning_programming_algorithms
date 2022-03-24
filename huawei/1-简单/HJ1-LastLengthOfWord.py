"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 16:09
@File        : HJ1-LastLengthOfWord.py
"""


def lastLengthOfWord(strs):
    """
    描述
    计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
    输入描述：
    输入一行，代表要计算的字符串，非空，长度小于5000。

    输出描述：
    输出一个整数，表示输入字符串最后一个单词的长度。
    :param strs:
    """
    l = 0
    len_s = len(strs.strip())
    for i in range(len_s - 1, -1, -1):
        if strs[i] == ' ':
            break
        l += 1
    return l


print(lastLengthOfWord('hellowww '))

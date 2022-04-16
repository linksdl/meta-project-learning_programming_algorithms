"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 15:13
@File        : HJ9 提取不重复的整数.py
"""


def duplicateInteger(num):
    """
    输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
    保证输入的整数最后一位不是 0 。
    :param num:
    """

    num = num[::-1]
    temp = []
    if num[0] != 0:
        for i in num:
            if i not in temp:
                temp.append(i)
        return ''.join(temp)
    else:
        return -1


print(duplicateInteger(input()))

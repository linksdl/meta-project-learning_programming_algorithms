"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/2 11:16
@File        : HJ57-高精度整数加法.py
"""


# HJ57 高精度整数加法


def addBigInteger(s1, s2):
    """
    HJ57 高精度整数加法
    输入两个用字符串 str 表示的整数，求它们所表示的数之和。
    数据范围： 1 \le len(str) \le 10000 \1≤len(str)≤10000
    输入描述：
    输入两个字符串。保证字符串只含有'0'~'9'字符
    输出描述：
    输出求和后的结果
    :param s1:
    :param s2:
    """
    # 字符串数字相加
    def add(str_num1, str_num2):
        out_str = ''
        l1 = len(str_num1)
        l2 = len(str_num2)
        c = 0
        for i in range(l1-1, -1, -1):
            n = int(str_num1[i]) + int(str_num2[i]) + c
            # print(c, int(str_num1[i]), int(str_num2[i]), (n % 10))
            if n >= 10:
                out_str += str((n % 10))
                c = 1
            else:
                out_str += str((n % 10))
                c = 0
        if c == 1:
            out_str += str(1)
        print(out_str[::-1])

    l1 = len(s1)
    l2 = len(s2)
    out_str = []
    if l2 <= l1:
        s2 = '0' * (l1 - l2) + s2
        add(s1, s2)
    else:
        s1 = '0' * (l2 - l1) + s1
        add(s1, s2)


addBigInteger('12345', '567')
addBigInteger('9876543210', '1234567890')

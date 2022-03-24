"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 17:05
@File        : HJ5-ConvertTen.py
"""


def convertTen(str):
    """
    描述
    写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

    数据范围：保证结果在 1 \le n \le 2^{31}-1 \1≤n≤2
    31
     −1
    输入描述：
    输入一个十六进制的数值字符串。

    输出描述：
    输出该数值的十进制字符串。不同组的测试用例用\n隔开。
    :param str:
    :return:
    """

    s = str[2::]
    num = 0
    l = len(s)
    for i in range(l):
        temp = 0
        ch = s[i].lower()
        if ch == 'a':
            temp = 10
        elif ch == 'b':
            temp = 11
        elif ch == 'c':
            temp = 12
        elif ch == 'd':
            temp = 13
        elif ch == 'e':
            temp = 14
        elif ch == 'f':
            temp = 15
        else:
            temp = int(ch)

        # print(temp)
        if (l - i - 1) > 0:
            num += temp * 16 ** (l - i - 1)
        else:
            num += temp

    print(num)


convertTen('ox2C')

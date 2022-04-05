"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 20:42
@File        : HJ21 简单密码.py
"""


def encoderStr(str):
    """
    描述
    现在有一种密码变换算法。
    九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
    而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
    数字和其它的符号都不做变换。
    数据范围： 输入的字符串长度满足 1 \le n \le 100 \1≤n≤100
    输入描述：
    输入一组密码，长度不超过100个字符。

    输出描述：
    输出密码变换后的字符串

    输入：
    YUANzhi1987
    输出：
    zvbo9441987
    :param str:
    :return:
    """
    new_str = []
    for i in range(len(str)):
        ch = str[i]
        if ch.isupper():
            if ch != 'Z':
                ch = chr(ord(ch.lower()) + 1)
                new_str.append(ch)
            else:
                new_str.append('a')
        elif ch in ['a', 'b', 'c']:
            new_str.append('2')
        elif ch in ['d', 'e', 'f']:
            new_str.append('3')
        elif ch in ['g', 'h', 'i']:
            new_str.append('4')
        elif ch in ['j', 'k', 'l']:
            new_str.append('5')
        elif ch in ['m', 'n', 'o']:
            new_str.append('6')
        elif ch in ['p', 'q', 'r', 's']:
            new_str.append('7')
        elif ch in ['t', 'u', 'v']:
            new_str.append('8')
        elif ch in ['w', 'x', 'y', 'z']:
            new_str.append('9')
        else:
            new_str.append(ch)

    return new_str


print(''.join(encoderStr('YUANzhi1987')))

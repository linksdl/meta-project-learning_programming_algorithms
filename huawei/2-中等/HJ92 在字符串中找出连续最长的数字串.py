"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/29 13:19
@File        : HJ92 在字符串中找出连续最长的数字串.py
"""


# HJ92 在字符串中找出连续最长的数字串

def maxDigitLen(str):
    """
    输入描述：
    输入一个字符串。1<=len(字符串)<=200

    输出描述：
    输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输出（中间不要输出空格）。
    :param input_str:
    :return:
    """
    window_size_min = 1
    l = len(str)
    window_size_max = l

    for i in range(window_size_min, window_size_max + 1, 1):
        for j in range(0, l - i + 1):
            ss = str[j:j + i]


def ff(in_str):
    """
    双指针方式
    :param in_str:
    :return:
    """
    in_str += 'a'
    l = len(in_str)
    if l == 1 and in_str[0].isdigit():
        print(in_str[0] + ',' + '1')
    point_i = 0
    point_j = 0
    max_len = 0
    max_len_nums = []
    while point_j < l:
        if not in_str[point_i].isdigit():
            point_i += 1
            point_j += 1
        else:
            if in_str[point_j].isdigit():
                point_j += 1
            else:
                cc = in_str[point_i:point_j]
                if (point_j - point_i) == max_len:
                    max_len_nums.append(cc)
                elif (point_j - point_i) > max_len:
                    max_len = (point_j - point_i)
                    max_len_nums = [cc]

                point_j += 1
                point_i = point_j

    # print(point_i, point_j)
    print(''.join(max_len_nums) + ',' + str(max_len))


ff('abcd12345ed125ss123058789')
ff('a8a72a6a5yy98y65ee1r2')

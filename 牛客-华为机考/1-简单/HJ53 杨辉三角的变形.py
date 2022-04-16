"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 19:46
@File        : HJ53 杨辉三角的变形.py
"""


# HJ53 杨辉三角的变形

def print_triange(n):
    """
    杨辉三角
    :param n:
    """
    triangle = [1]
    if n == 1:
        return triangle
    if n == 2:
        triangle = [1, 1, 1]
        return triangle
    if n > 3:
        nums = 2*n -1
        i = n-1
        for i in range(1, nums+1):
            triangle
    triangle = [x + y + z for x, y, z in zip([0] + print_triange(n - 1), print_triange(n - 1), print_triange(n - 1) + [0])]
    # print(triangle)
    return triangle



# print(''.join(str(print_triange(3))).center(100))



def print_tri(n):
    list = [2, 3, 2, 4]
    if n == 1 or n == 2:
        print(-1)
    else:
        l = (n + 2) % 4
        print(list[l - 1])



"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 21:04
@File        : HJ22 汽水瓶.py
"""


def f_bottle(num):
    count = num // 3
    empty_num = num // 3 + num % 3  #
    if num < 2:
        return count
    if num == 2:
        count += 1
    else:
        count += f_bottle(empty_num)

    return count


print(f_bottle(81))

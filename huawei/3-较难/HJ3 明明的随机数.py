"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 13:54
@File        : HJ3 明明的随机数.py
"""


# HJ3 明明的随机数


def randomHashset(n, nums):
    """
    HJ3 明明的随机数
    :param n:
    :param nums:
    :return:
    """

    new_nums = set(nums)
    for j in sorted(new_nums):
        print(j)


while True:
    try:
        n = int(input())
        nums = []
        for i in range(int(n)):
            nums.append(int(input()))
        randomHashset(n, nums)

    except (EOFError, KeyboardInterrupt):
        break

# randomHashset(7, [22, 55, 2, 2, 1, 3, 4, 5, 6, 1, 2, 3])

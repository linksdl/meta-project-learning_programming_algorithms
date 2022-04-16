"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 15:36
@File        : HJ58 输入n个整数，输出其中最小的k个.py
"""


def minKInteger(n, k, nums):
    """
    描述
    输入n个整数，找出其中最小的k个整数并按升序输出
    本题有多组输入样例
    数据范围：1 \le n \le 1000 \1≤n≤1000  ，输入的整数满足 1 \le val \le 10000 \1≤val≤10000
    输入描述：
    第一行输入两个整数n和k
    第二行输入一个整数数组
    输出描述：
    从小到大输出最小的k个整数，用空格分开。
    :param n:
    :param k:
    :param nums:
    """
    nums.sort()
    if k >= n:
        return ' '.join(nums)

    else:
        new_nums = nums[0:k]
        # print(new_nums)
        return ' '.join([str(s) for s in new_nums])


print(minKInteger(5, 2, [1,3,5,7,2]))



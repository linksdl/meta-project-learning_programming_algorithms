"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 09:59
@File        : HJ105-记负均正II.py
"""


# HJ105 记负均正II
# 描述
# 输入
# n
# 个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
# 本题有多组输入数据，输入到文件末尾。
#
# 数据范围：1 \le
# n \le
# 50000 \1≤n≤50000  ，其中每个数都满足 | val | \le
# 10 ^ {6} \∣val∣≤10
# 6
#
# 输入描述：
# 输入任意个整数，每行输入一个。
#
# 输出描述：
# 输出负数个数以及所有非负数的平均值


def countNegativeInteger(nums):
    """
    输出负数个数以及所有非负数的平均值
    :param nums:
    :return:
    """

    no_neg_nums = []
    count = 0
    for n in nums:
        if n >= 0:
            no_neg_nums.append(n)
        else:
            count += 1

    print(count)
    if len(no_neg_nums) > 0:
        print('%.1f'%(sum(no_neg_nums) / len(no_neg_nums)))
    else:
        print(0.0)


countNegativeInteger([-13, -4, -7])
countNegativeInteger([-12, 1, 2])

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 15:55
@File        : 正方形个数.py
"""

import itertools


def cal_dis(c1, c2):
    dis = int((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)
    # dis **= 0.5
    # print(dis)
    return dis


def is_cude(points):
    a, b, c, d = points
    d1 = cal_dis(a, b)
    d2 = cal_dis(a, c)
    d3 = cal_dis(a, d)
    d4 = cal_dis(b, c)
    d5 = cal_dis(b, d)
    d6 = cal_dis(c, d)

    sort_dis = sorted([d1, d2, d3, d4, d5, d6])

    if sort_dis[0] == sort_dis[1] == sort_dis[2] == sort_dis[3] and sort_dis[4] == sort_dis[5]:
        # print(sort_dis)
        # print(points)
        return True
    else:
        return False


def cal_fn(n, nums):
    """
    计算机正方形个数
    :param n: 坐标点数
    :param nums:  坐标点数组
    :return:
    """

    if n < 4:
        return False
    count = 0
    point_combinations = list(itertools.combinations(nums, 4))
    for ps in point_combinations:
        if is_cude(ps):
            count += 1

    print(count)


nums = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1,1], [2, 1], [3, 1], [0,2], [1, 2], [2,2]]
cal_fn(11, nums)

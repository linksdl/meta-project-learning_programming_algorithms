"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 15:20
@File        : 最优选址类问题.py
"""



def optimalSelection(nums):  # 仓库最优选址, 到达各个商店的距离之和最小

    n = len(nums)

    # 按仓库位置递增排序

    nums.sort()

    # 仓库位置的中位数 (仓库数量为奇数时, 中位数为中间位置; 否则, 中位数为中间两个仓库位置的平均值)

    mid = nums[n // 2] if (n & 1) else (nums[n // 2 - 1] + nums[n // 2]) // 2

    # 所求结果 (仓库到各个商店距离之和的最小值)

    res = 0

    # 遍历 n 个商店, 它们到中间位置 mid 的绝对值之和, 即为所求

    for i in range(n):

        res += abs(nums[i] - mid)

    return res

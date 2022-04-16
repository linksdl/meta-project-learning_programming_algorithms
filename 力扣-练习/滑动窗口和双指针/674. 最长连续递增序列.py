"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 08:36
@File        : 674. 最长连续递增序列.py
"""


def findLengthOfLCIS(nums):
    """
    最长连续递增序列
    :param nums:
    :return:
    """

    l = len(nums)
    j = 0
    i = 0
    res = 0
    while j < l:
        if nums[j-1] >= nums[j]:
            i = j
        j += 1
        res = max(res, j-i)

    return res





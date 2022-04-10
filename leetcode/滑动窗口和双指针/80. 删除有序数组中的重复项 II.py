"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 09:56
@File        : 80. 删除有序数组中的重复项 II.py
"""


# 删除排序数组中的重复项 II

def removeDuplicates(nums):
    """
    删除排序数组中的重复项 II
    :param nums:
    :return:
    """

    l = len(nums)
    if l <= 2:
        return l

    j = 2
    for i in range(2, l):
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1
    return j


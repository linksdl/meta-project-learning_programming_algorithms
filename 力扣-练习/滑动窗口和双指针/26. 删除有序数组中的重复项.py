"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 08:16
@File        : 26. 删除有序数组中的重复项1.py
"""

# 26. 删除有序数组中的重复项


def removeDuplicates(nums):

    l = len(nums)
    if l < 2:
        return l

    j = 1
    pre = nums[0]
    for i in range(1, l):
        if nums[i] != pre:
            nums[j] = nums[i]
            pre = nums[j]
            j += 1
    return j


# 循环不变量，双指针
def removeDuplicates1(nums):
    l = len(nums)

    if l < 2:
        return l

    j = 0
    for i in range(1, l):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j+1





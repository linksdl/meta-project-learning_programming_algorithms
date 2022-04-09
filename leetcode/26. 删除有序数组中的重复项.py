"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 23:26
@File        : 26. 删除有序数组中的重复项.py
"""


# 删除有序数组中的重复项


def removeDuplicates(nums):
    """
    removeDuplicates
    :param nums:
    """

    if not nums:
        return 0

    n = len(nums)
    fast = slow = 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow

res = removeDuplicates([1,1,2])
print(res)





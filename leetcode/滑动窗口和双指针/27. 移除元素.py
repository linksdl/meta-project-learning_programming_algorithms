"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 09:00
@File        : 27. 移除元素.py
"""


def removeElement(nums, val):
    """
    移除元素
    :param nums:
    :param val:
    :return:
    """

    l = len(nums)
    i = 0
    j = 0
    while i < l:
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1

    return j



nums = [3,2,2,3]
val = 3
res = removeElement(nums, val)
print(res)


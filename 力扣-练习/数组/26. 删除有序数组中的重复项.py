"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/5/12 10:34
@File        : 26. 删除有序数组中的重复项.py
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)

        if l < 2:
            return l

        j = 0
        for i in range(1, l):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1

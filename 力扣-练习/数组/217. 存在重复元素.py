"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/5/12 11:05
@File        : 217. 存在重复元素.py
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True

        return False

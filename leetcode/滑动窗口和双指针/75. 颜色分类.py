"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 11:07
@File        : 75. 颜色分类.py
"""

# 75. 颜色分类
# https://leetcode-cn.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(nums, m, n):
            temp = nums[m]
            nums[m] = nums[n]
            nums[n] = temp

        l = len(nums)
        zero = -1
        two = l - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                zero += 1
                swap(nums, i, zero)
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, two)
                two -= 1

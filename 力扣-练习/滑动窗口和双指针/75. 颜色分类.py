"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 11:07
@File        : 75. 颜色分类.py
"""

# 75. 颜色分类
# https://leetcode-cn.com/problems/sort-colors/


def sortColors(nums) -> None:
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

    print(nums)

nums = [2,0,2,1,1,0]
sortColors(nums)

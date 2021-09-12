#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/8 6:08 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 双指针-977（有序数组的平方) simple.py

'''
977. 有序数组的平方
https://leetcode-cn.com/problems/squares-of-a-sorted-array/
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
'''


class Solution:
    def sortedSquares(self, nums):
        length = len(nums)
        i, j, pos = 0, length-1, length-1
        ans = [0] * length
        while i <= j:
            if nums[i] * nums[i]  > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1
        return ans





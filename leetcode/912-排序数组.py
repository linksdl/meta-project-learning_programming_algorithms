#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/15 6:04 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 912-排序数组.py

'''
912. 排序数组
给你一个整数数组 nums，请你将该数组升序排列。
https://leetcode-cn.com/leetbook/read/sort-algorithms/ewrwt6/
输入：nums = [5,2,3,1]
输出：[1,2,3,5]
'''

class Solution:
    def sortArray(self, nums):
        minIndex = maxIndex = -1
        # asc order
        for i in range(len(nums) // 2):
            minIndex = i
            maxIndex = i
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[minIndex]:
                    minIndex = j
                if nums[j] >= nums[maxIndex]:
                    maxIndex = j
            if minIndex == maxIndex: break
            self.swap(nums, i, minIndex)

            if maxIndex == i:
                maxIndex = minIndex
            self.swap(nums,len(nums)-1-i, maxIndex)
            return nums

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         return nums

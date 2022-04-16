#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/10/31 5:53 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode_python
# @File        : 34-二分查找（在排序数组中查找元素的一个和最后一个位置）.py


'''
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
'''



class Solution:
    def binarySearch(self, nums, target, flag):
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (flag and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.binarySearch(nums, target, flag=True)
        right_index = self.binarySearch(nums, target, flag=False) - 1
        if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
            return [left_index, right_index]
        return [-1, -1]

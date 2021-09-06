#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/6 5:14 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 35.py

'''
搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
'''

class Soluction:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)
        position = len(nums)
        while low <= high:
            mid = (high - low) // 2 + low
            if target <= nums[mid]:
                position = mid
                high = mid - 1
            else:
                low = mid + 1
        return position


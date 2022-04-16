#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/6 3:47 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 704-二分查找-力扣-练习 simple.py


'''
标签：二分查找
过程：
设定左右指针
找出中间位置，并判断该位置值是否等于 target
nums[mid] == target 则返回该位置下标
nums[mid] > target 则右侧指针移到中间
nums[mid] < target 则左侧指针移到中间
时间复杂度：O(logN)
O(logN)
https://leetcode-cn.com/problems/binary-search/
'''
class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2 + low
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                high = mid -1
            else:
                low = mid + 1
        return -1


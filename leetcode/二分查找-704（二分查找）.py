#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/6 3:27 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 二分查找-704（二分查找）.py
'''二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
力扣（LeetCode）
https://leetcode-cn.com/problems/binary-search'''


def search(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    return -1









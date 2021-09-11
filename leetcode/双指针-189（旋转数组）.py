#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/8 7:15 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 双指针-189（旋转数组）.py

'''
189 旋转数组
https://leetcode-cn.com/problems/rotate-array/
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
'''


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1



#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/11 10:27 上午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 283-双指针（移动零）simple.py

'''
283 双指针-移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
https://leetcode-cn.com/problems/move-zeroes/
'''


class Solution:
    # 双指针
    def move_zeros(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l_point = r_point = 0
        while r_point < n:
            if nums[r_point] != 0:
                nums[l_point], nums[r_point] = nums[r_point], nums[l_point]
                l_point += 1
            r_point += 1

    # 冒泡排序
    def move_zeros1(self, nums):
        zeroscount, n = 0, len(nums)
        for i in range(n - zeroscount):
            if nums[i] == 0:
                for j in range(i, n - zeroscount -1):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                zeroscount += 1
                i -= 1

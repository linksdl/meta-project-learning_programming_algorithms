#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/11/5 7:19 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode_python
# @File        : 268-丢失的数字.py

'''
268. 丢失的数字 easy
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

https://leetcode-cn.com/problems/missing-number/
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # the range of nums
        n = len(nums)
        total = n * (n+1) // 2
        arr_sum = sum(nums)
        ans = total - arr_sum
        return ans

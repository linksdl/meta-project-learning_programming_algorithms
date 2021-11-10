#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/16 4:35 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 46-全排列（回溯）middle.py

'''
46. 全排列
https://leetcode-cn.com/problems/permutations/
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

class Solution:
    def permute(self, nums):
        ans = []
        def backtrack(nums, temp):
            if not nums:
                ans.append(temp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], temp + [nums[i]])
        backtrack(nums, [])
        return ans

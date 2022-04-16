#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/14 2:57 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 15-双指针（三数之和）middle.py

'''
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
https://leetcode-cn.com/problems/3sum

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
'''

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = []
        if n < 3:
            return ans
        # a + b + c = 0
        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            c = n - 1
            target = -nums[a]
            for b in range(a + 1, n):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                while b < c and nums[b] + nums[c] > target:
                    c -= 1
                if b == c:
                    break
                if nums[b] + nums[c] == target:
                    ans.append([nums[a], nums[b], nums[c]])
        return ans

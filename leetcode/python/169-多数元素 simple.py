#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/14 2:35 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 169-多数元素 simple.py

'''
169. 多数元素
https://leetcode-cn.com/problems/majority-element
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
输入：[3,2,3]
输出：3
'''

class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        return nums[len(nums) // 2]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/13 8:42 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 136-位运算（只出现一次的数字）simple.py

'''
136. 只出现一次的数字
https://leetcode-cn.com/problems/single-number/
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
输入: [2,2,1]
输出: 1
'''

import math

class Solution:
    def singleNumber(self, nums):
        num = math.reduce(lambda x, y: x^y, nums)
        return num

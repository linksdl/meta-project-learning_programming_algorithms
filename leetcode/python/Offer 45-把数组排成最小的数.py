#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/14 8:54 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : Offer 45-把数组排成最小的数.py

'''
剑指 Offer 45. 把数组排成最小的数
https://leetcode-cn.com/leetbook/read/sort-algorithms/oshq72/
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
输入: [10,2]
输出: "102"
'''


class Solution:
    def minNumber(self, nums):
        n = len(nums)
        swapped = True
        for i in range(0, n):
            if not swapped: break
            swapped = False
            for j in range(0, n-i-1):
                num1 = int(str(nums[j])+str(nums[j+1]))
                num2 = int(str(nums[j+1])+str(nums[j]))
                if num2 < num1:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    swapped = True
        ans = ''
        for n in nums:
            ans += str(n)
        return ans

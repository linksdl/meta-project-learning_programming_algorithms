#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/15 5:26 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 215-数组中的第K个最大元素 simple.py

'''
215. 数组中的第 K 个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
https://leetcode-cn.com/leetbook/read/sort-algorithms/osxtdc/
'''

class Solution:
    def findKthLargest(self, nums, k):
        # selction sort
        maxIndex = 0
        for i in range(k):
            maxIndex = i
            for j in range(i+1, len(nums)):
                if nums[maxIndex] < nums[j]:
                    maxIndex = j

            temp = nums[i]
            nums[i] = nums[maxIndex]
            nums[maxIndex] = temp
        return nums[k-1]

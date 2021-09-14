#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/14 3:29 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 75-颜色分类 middle.py

'''
75. 颜色分类
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
https://leetcode-cn.com/problems/sort-colors
'''


class Solution:

    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        point0 = point1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[point1] = nums[point1], nums[i]
                point1 += 1
            elif nums[i] == 0:
                nums[i], nums[point0] = nums[point0], nums[i]
                if point0 < point1:
                    nums[i], nums[point1] = nums[point1], nums[i]
                point0 += 1
                point1 += 1

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/11 11:22 上午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 167.py

'''
167- https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
双指针: 两数之和 II - 输入有序数组

给定一个已按照 非递减顺序排列  的整数数组 numbers ，
请你从数组中找出两个数满足相加之和等于目标数 target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
'''


class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

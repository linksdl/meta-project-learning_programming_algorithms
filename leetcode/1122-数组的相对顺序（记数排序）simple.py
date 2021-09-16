#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/16 7:28 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 1122-数组的相对顺序（记数排序）simple.py
'''
1122. 数组的相对排序
https://leetcode-cn.com/problems/relative-sort-array/
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

'''

class Solution:
    def relativeSortArray(self, arr1, arr2):
        upper = 0
        for x in arr1:
            upper = max(upper, x)

        frequency = [0] * (upper +1)
        for x in arr1:
            frequency[x] += 1
        ans = [0] * len(arr1)
        index  = 0
        for x in arr2:
            for i in range(frequency[x]):
                ans[index] = x
                index += 1
            frequency[x] = 0
        for x in range(upper+1):
            for i in range(frequency[x]):
                ans[index] = x
                index += 1
        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/14 4:29 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 56-合并区间 middle.py

'''
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
https://leetcode-cn.com/problems/merge-intervals
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
'''


class Solution:
    def merge(self, intervals):
        # sort this intervals
        intervals.sort(key=lambda x: x[0])
        ans = []
        for nums in intervals:
            if not ans or ans[-1][1] < nums[0]:
                ans.append(nums)
            else:
                ans[-1][1] = max(ans[-1][1], nums[1])
        return ans

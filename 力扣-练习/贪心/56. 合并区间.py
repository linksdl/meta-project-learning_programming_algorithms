"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 15:29
@File        : 56. 合并区间.py
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        ans = []
        for num in intervals:
            if not ans or ans[-1][1] < num[0]:
                ans.append(num)
            else:
                ans[-1][1] = max(ans[-1][1], num[1])
        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/11/4 6:43 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode_python
# @File        : 1218-动态规划（最长定差子序列）.py

'''
1218. 最长定差子序列 中等

给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference
'''

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for v in arr:
            if  v - difference in dp:
                dp[v] = dp[v-difference] + 1
                if v != v - difference:
                    del dp[v-difference]
            else:
                if v not in dp:
                    dp[v] = 1
        return max(dp.values())

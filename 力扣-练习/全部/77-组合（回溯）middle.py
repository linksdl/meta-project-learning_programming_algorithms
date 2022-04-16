#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/16 4:14 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 77-组合（回溯）middle.py

'''
77. 组合
https://leetcode-cn.com/problems/combinations/
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    def combine(self, n: int, k: int):
        ans = []
        path = []
        def backtrack(n, k, index):
            if len(path)  == k:
                ans.append(path[:])
                return
            for i in range(index, n-(k-len(path))+2):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/16 5:21 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 784-字母大小写全排列(回溯 or 递归) middle.py

'''
784. 字母大小写全排列
https://leetcode-cn.com/problems/letter-case-permutation/
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]
'''

class Solution:
    def letterCasePermutation(self, s: str):
        ans = []
        def dfs(t, s):
            if len(s) == 0:
                return ans.append(t)
            c = s[0]
            nextStr = s[1:]
            if c.isalpha():
                dfs(t + c.upper(), nextStr)
                dfs(t + c.lower(), nextStr)
            else:
                dfs(t + c, nextStr)

        dfs('', s)
        return ans

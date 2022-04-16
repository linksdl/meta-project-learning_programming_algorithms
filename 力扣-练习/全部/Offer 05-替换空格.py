#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/14 6:48 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : Offer 05-替换空格.py

'''
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
输入：s = "We are happy."
输出："We%20are%20happy."
https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/50ywkd/
'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res

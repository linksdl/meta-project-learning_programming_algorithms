#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/17 11:35 上午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 119-杨辉三角（数组）simple.py

'''
119. 杨辉三角 II
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
输入: rowIndex = 3
输出: [1,3,3,1]
https://leetcode-cn.com/problems/pascals-triangle-ii/
'''

class Solution:
    def getRow(self, rowIndex: int):
        ans =[1]
        for i in range(1, rowIndex+1):
            ans.append(int(ans[i-1] * (rowIndex - i + 1) / i))
        return ans

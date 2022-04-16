#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/18 11:28 上午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 231-2的幂（位运算）simple.py

'''
231. 2 的幂
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
https://leetcode-cn.com/problems/power-of-two
输入：n = 1
输出：true
解释：20 = 1
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

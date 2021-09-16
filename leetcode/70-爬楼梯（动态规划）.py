#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/16 5:39 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 70-爬楼梯（动态规划）.py

'''
70. 爬楼梯
https://leetcode-cn.com/problems/climbing-stairs/
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        ans, a, b = 0, 1, 2
        for i in range(3, n+1):
            # 超出时间限制
            # return self.climbStairs(n-1) + self.climbStairs(n-2)
            ans = a + b
            a = b
            b = ans
        return ans

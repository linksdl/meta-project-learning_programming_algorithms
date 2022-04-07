"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 22:52
@File        : 70. 爬楼梯.py
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[-1]

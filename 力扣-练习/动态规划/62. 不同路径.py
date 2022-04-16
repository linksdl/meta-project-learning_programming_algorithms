"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 22:00
@File        : 62. 不同路径.py
"""


# 62. 不同路径
# https://leetcode-cn.com/problems/unique-paths/

def uniquePaths(m, n):
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
    :param m:
    :param n:
    :return:
    """

    dp = [[1] * (n+1) for _ in range(m+1)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


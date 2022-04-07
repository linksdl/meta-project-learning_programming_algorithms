"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 21:13
@File        : 64. 最小路径和.py
"""


# 64. 最小路径和


def minPathSum(grid):
    """
    最小路径和 动态规划
    :param grid:
    :return:
    """
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])
    print(m, n)
    dp = [[0] * (n) for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    print(dp[m-1][n-1])


grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
minPathSum(grid)



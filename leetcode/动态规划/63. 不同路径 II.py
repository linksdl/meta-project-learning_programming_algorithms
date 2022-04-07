"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 22:13
@File        : 63. 不同路径 II.py
"""


# 不同路径 II

def uniquePathsWithObstacles(obstacleGrid):
    """
    不同路径 II
    :param obstacleGrid:
    :return:
    """

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0] * (n) for _ in range(m)]

    for i in range(m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break

    for i in range(n):
        if obstacleGrid[0][i] == 0:
            dp[0][i] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]



obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
res = uniquePathsWithObstacles(obstacleGrid)
print(res)

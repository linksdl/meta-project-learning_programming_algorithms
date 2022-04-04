"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 16:41
@File        : HJ91 走方格的方案数.py
"""


# 请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
#
# 注：沿棋盘格之间的边缘线行走
#
# 数据范围： 1 \le n,m \le 8 \1≤n,m≤8

# 输入描述：
# 输入两个正整数n和m，用空格隔开。(1≤n,m≤8)
# 输出描述：
# 输出一行结果

def girdDynamic(n, m):
    """
    HJ91 走方格的方案数
    :param n:
    :param m:
    :return:
    """

    dp = [[1]*(m+1) for _ in range((n+1))]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    print(dp)
    print(dp[-1][-1])


girdDynamic(2, 2)

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 16:20
@File        : HJ61-放苹果.py
"""


def appleDynamic(m, n):
    """
    HJ61 放苹果
    把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
    注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。
    :param m:
    :param n:
    :return:
    """
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][1] = 1  # 如果只有一个盘子则只有一种放置方案

    for i in range(n+1):
        dp[0][i] = 1  # 如果没有苹果则只有一种放置方案
        dp[1][i] = 1  # 如果只有一个苹果也相当于只有一种方案

    for i in range(2, m+1):
        for j in range(2, n+1):
            if i < j:
                dp[i][j] = dp[i][i]  # 如果苹果数量少，则盘子一定会空，所以去除那些空的盘子其实不影响方案数
            else:
                # 如果苹果数量多，则考虑是否要装够j个盘子，如果不装够则有dp[i][j-1]，
                # 如果装够则相当于从所有盘子同时去掉一个苹果无影响，则有dp[i-j][j]
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]

    print(dp[-1][-1])


appleDynamic(7, 3)



"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 15:35
@File        : 0-1背包问题.py
"""




def maxBackpack(n, m, ws, vs):
    """
    0-1背包问题
    :param n:
    :param w:
    :return:
    """
    dp = [[0]*(m+1) for _ in range(n+1)]
    ws.insert(0,0)
    vs.insert(0,0)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if ws[i] <= j:
                dp[i][j] = max(dp[i-1][j-ws[i]] + vs[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]



n = 5
weight_most=10
weight=[2,2,6,5,4]
value=[3,6,5,4,6]
res = maxBackpack(n, weight_most, weight, value)
print(res)

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 15:21
@File        : HJ16 购物单.py
"""


# HJ16 购物单
# 其实这题就是0-1背包问题


def maxHappy(total, ws, vs):
    # print(total, ws, vs)
    """
    0-1背包问题的 变形
    :param total 总额
    :param ws: 主件单价-相当与重量
    :param vs: 满意度-相当于价值
    :return:
    """
    m = len(ws)  # 物品个数
    n = total
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # print(m, n)
    for i in range(1, m + 1):
        w0 = ws[i - 1][0]
        w1 = ws[i - 1][1]
        w2 = ws[i - 1][2]
        v0 = vs[i - 1][0]
        v1 = vs[i - 1][1]
        v2 = vs[i - 1][2]
        for j in range(1, n + 1):
            # 1，不放入
            dp[i][j] = dp[i - 1][j]
            # 2, 放1个主件
            if j - w0 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w0] + v0)

            # 3. 1个主件+附件1
            if j - w0 - w1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w0 - w1] + v0 + v1)

            # 4. 1个主件+附件2
            if j - w0 - w2 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w0 - w2] + v0 + v2)

            # 4. 一个主件+附件1+附件2
            if j - w0 - w1 - w2 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w0 - w1 - w2] + v0 + v1 + v2)

    print(int(dp[-1][-1]) * 100)


while True:
    try:

        total, n = list(map(int, input().split(' ')))
        W = {}
        V = {}
        for i in range(1, n + 1):
            W[i] = [0, 0, 0]
            V[i] = [0, 0, 0]
        main_key = []
        total = int(total / 100)
        for i in range(n):
            v, p, q = list(map(int, input().split(" ")))
            if q == 0:
                W[i + 1][0] = int(v / 100)
                V[i + 1][0] = int(v * p / 100)
                main_key.append(i + 1)
            else:
                if W[q][1] == 0:
                    W[q][1] = int(v / 100)
                    V[q][1] = int(v * p / 100)
                else:
                    W[q][2] = int(v / 100)
                    W[q][2] = int(v * p / 100)
        W_lst = []
        V_lst = []
        for key in W.keys():
            if key in main_key:
                W_lst.append(W[key])
                V_lst.append(V[key])
        # print(W_lst, V_lst)
        maxHappy(total, W_lst, V_lst)

    except:
        break

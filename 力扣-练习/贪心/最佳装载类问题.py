"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 15:13
@File        : 最佳装载类问题.py
"""


def minBoats(weights, limit):  # 承载所有人过河所需的最小船数

    n = len(weights)

    # n 个人的体重递增排序

    weights.sort()

    # 初始化: 双指针 left 和 right 分别指向最轻和最终的人, res 表示所求的最小船数

    left, right, res = 0, n - 1, 0

    # left 和 right 未相遇时, 循环

    while left < right:

        # 当前最轻和最终的两个人体重之和 <= limit, 可将他们安排到同一艘船上

        # left 和 right 相向移动一位, res + 1

        if weights[left] + weights[right] <= limit:

            left += 1; right -= 1; res += 1

        # 否则, 上述两个人不能安排在同一艘船

        # 将体重为 weights[right] 的人单独安排在一艘船上

        # 不过可以为体重为 weights[left] 的那个人寻找安排在同一艘船上的人(自然的, 这个人体重更轻)

        # 因此, right 向左移动一位, res + 1

        else:

            right -= 1; res += 1

    # 若两指针相遇, 说明体重为 weights[left] 的人还未被安排, 应将其单独安排在一艘船上

    if left == right:

        res += 1

    # 最终, res 即为所求

    return res



def partialMaxValue(goods, limit):  # 部分背包问题

    n = len(goods)

    # 所求的物品最大总价值

    res = 0

    # n 件物品按性价比(总价值/总重量)递减排序

    goods = sorted(goods, key=lambda k: -k[1] / k[0])

    # 按性价比递减的顺序, 遍历上述 n 件物品

    for i in range(n):

        # 第 i 件物品可以完全装入背包, 将其完全装入, 对所求结果的贡献为该物品的总价值

        if limit - goods[i][0] >= 0:

            res += goods[i][1]

            limit -= goods[i][0]

        # 否则, 第 i 件物品仅装入 limit 重量, 对所求结果的贡献为 limit * 该物品的性价比

        else:

            res += limit * (goods[i][1] / goods[i][0])

            limit = 0

        # 背包恰好装满, res 即为所求

        if limit == 0:

            return res

    # 否则, 该问题无解, 返回 -1

    return -1

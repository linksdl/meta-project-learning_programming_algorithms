"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 12:07
@File        : HJ103 Redraiment的走法.py
"""


# HJ103 Redraiment的走法


def stpes(n, nums):
    """
    描述
    Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，但只能从低处往高处的桩子走。
    他希望走的步数最多，你能替Redraiment研究他最多走的步数吗？
    数据范围：每组数据长度满足 1 \le n \le 200 \1≤n≤200  ， 数据大小满足 1 \le val \le 350 \1≤val≤350
    :param n:
    :param nums:
    :return:
    """
    # 从某位置开始的 最长递增子序列长度
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)

    max_len = max(dp)
    print(max_len)


stpes(6, [2, 5, 1, 5, 4, 5])

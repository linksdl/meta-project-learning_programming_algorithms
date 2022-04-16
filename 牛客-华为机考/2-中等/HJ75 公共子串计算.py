"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 17:44
@File        : HJ75 公共子串计算.py
"""


# HJ75 公共子串计算


# 描述
# 给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
#
# 注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
# 数据范围：字符串长度：1\le s\le 150\1≤s≤150
# 进阶：时间复杂度：O(n^3)\O(n
# 3
#  ) ，空间复杂度：O(n)\O(n)
# 输入描述：
# 输入两个只包含小写字母的字符串
#
# 输出描述：
# 输出一个整数，代表最大公共子串的长度


def longestStr(s1, s2):
    """
    HJ75 公共子串计算
    :return:
    """
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n+1) for _ in range(m+1)]
    max_len = 0
    for i in range(0, m):
        for j in range(0, n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                if dp[i+1][j+1] > max_len:
                    max_len = dp[i+1][j+1]

    print(max_len)


longestStr('asdfas', 'werasdfaswer')

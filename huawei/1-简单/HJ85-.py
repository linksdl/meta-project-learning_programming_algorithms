"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 22:22
@File        : HJ85-.py
"""

# HJ85 最长回文子串

# 描述
# 给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
# 所谓回文串，指左右对称的字符串。
# 所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
# 数据范围：字符串长度1\le s\le 350\1≤s≤350
# 进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)
# 输入描述：
# 输入一个仅包含小写字母的字符串
#
# 输出描述：
# 返回最长回文子串的长度



def subString(str):
    """
    HJ85 最长回文子串
    :param str:
    """

    window_l_min = 2
    window_l_max = len(str)
    max = 1
    for i in range(window_l_min, window_l_max+1):
        for j in range(0, len(str) - i+1):
            ss = str[j:j+i]
            l = int(i // 2)
            if ss[:l] == ss[:(-l-1):-1]:
                if len(ss) > max:
                    max = i
                # print(ss, max)

    print(max)


# subString('cdabbacc')

# s = 'abcdba'
# print(s[:2])
# print(s[:-3:-1])



def dynamic(str):
    l = len(str)

    if l < 2:
        return l

    max_len = 1

    dp = [[False] * l for _ in range(l)]
    # print(dp)
    for i in range(l):
        dp[i][i] = True

    # print(dp)

    for win_size in range(2, l+1):
        for i in range(l):
            j = win_size + i - 1
            if j >= l:
                break

            if str[i] != str[j]:
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j] and j-i+1 > max_len:
                max_len = j - i + 1

    print(max_len)


dynamic('cdabbacc')




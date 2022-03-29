"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/29 21:15
@File        : HJ71-字符串通配符.py
"""


# HJ71 字符串通配符


def rexStr(s, rex):
    """
    问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。
    现要求各位实现字符串通配符的算法。
    实现如下2个通配符：
    *：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
    ？：匹配1个字符

    注意：匹配时不区分大小写。
    :param rex: 模式
    :param s: 字符串
    :return:
    """

    n = len(s)
    m = len(rex)

    s = s.lower()
    rex = rex.lower()

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    # print(len(dp), len(dp[0]))

    # 1, dp[0][0] = True，即当字符串 s 和 模式p均为空时，匹配成功；
    dp[0][0] = True
    # 2, dp[i][0] = False，即空模式无法匹配非空字符串；
    # 3, dp[0][j] 需要分情况讨论：因为星号才能匹配空字符串，所以只有当模式p的前j个字符均为星号时,dp[0][j]才为真。
    for i in range(1, m + 1):
        if rex[i-1] == '*':
            dp[0][i] = True
        else:
            break

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if rex[j - 1] == '*' and (s[i - 1].isdigit() or s[i - 1].isalpha()):
                dp[i][j] = dp[i - 1][j] | dp[i][j - 1] | dp[i - 1][j - 1]
            elif rex[j-1] == '?' and (s[i-1].isdigit() or s[i-1].isalpha()):
                dp[i][j] = dp[i - 1][j - 1]
            if rex[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[-1][-1]


# print(rexStr('h*?*a', 'h#a'))
# print(rexStr('te?t*.*', 'txt12.xls'))
# print(rexStr('?*Bc*?', 'abcd'))
print(rexStr('txt12.xls', 't?t*1*.*'))

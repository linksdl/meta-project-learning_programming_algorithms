"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 14:26
@File        : HJ32 密码截取.py
"""


# HJ32 密码截取

# 描述
# Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
# 比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
# 比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
# 因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
# Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？


# 密码截取#最长回文子串
def subLoopStr(s):
    """
    #密码截取#最长回文子串
    :param s:
    :return:
    """
    is_palindromic_string = lambda s: s == s[::-1]

    l = len(s)
    cur_length = 0
    start_index = 0
    for i in range(l):
        cur_start_index = i - cur_length - 1
        cur_substr = s[cur_start_index: cur_start_index + cur_length + 2]

        if cur_start_index >= 0 and is_palindromic_string(cur_substr):
            start_index = cur_start_index
            cur_length += 2

        else:
            cur_start_index = i - cur_length
            cur_substr = s[cur_start_index: cur_start_index + cur_length + 1]
            if cur_start_index >= 0 and is_palindromic_string(cur_substr):  # 判断扩展后的子串是否回文
                start_index = cur_start_index  # 更新子串起始下标
                cur_length += 1

    print(cur_length)

subLoopStr('12HHHHA')
subLoopStr('ABBBA')
subLoopStr('ABBA')


# 方案1：暴力求解
def longestPalindrome(s):
    is_palindromic_string = lambda s: s == s[::-1]  # 回文串判定函数
    max_len, max_substr = 0, ''

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            cur_substr = s[i:j]  # 取当前子串
            print(cur_substr)
            if is_palindromic_string(cur_substr):
                cur_len = len(cur_substr)  # 当前子串长度
                if cur_len > max_len:
                    max_len = cur_len
                    max_substr = cur_substr  # 当前最长子串
    return max_substr



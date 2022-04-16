"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/29 23:45
@File        : HJ27 查找兄弟单词.py
"""


# HJ27 查找兄弟单词


def brotherWord(n, strs, s, k):
    """
    HJ27 查找兄弟单词
    :param n:
    :param strs:
    :param i:
    """
    new_strs = sorted(strs)
    brother_words = []
    for w in strs:
        if w == s:
            continue
        elif sorted(w) == sorted(s):
            brother_words.append(w)

    sorted_brother_words = sorted(brother_words)
    n = len(brother_words)
    print(n)
    if k <= n:
        print(sorted_brother_words[k-1])


brotherWord(6, ['cab', 'ad', 'abcd', 'cba', 'abc', 'bca'], 'abc', 1)


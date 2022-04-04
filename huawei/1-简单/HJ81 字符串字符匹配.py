"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 23:35
@File        : HJ81 字符串字符匹配.py
"""


# HJ81 字符串字符匹配

# 判断短字符串S中的所有字符是否在长字符串T中全部出现。
# 请注意本题有多组样例输入。
# 数据范围:1\le len(S),len(T)\le200\1≤len(S),len(T)≤200
# 进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)
# 输入描述：
# 输入两个字符串。第一个为短字符串，第二个为长字符串。两个字符串均由小写字母组成。
#
# 输出描述：
# 如果短字符串的所有字符均在长字符串中出现过，则输出字符串"true"。否则输出字符串"false"。

def matchingStr(str1, str2):
    """
    HJ81 字符串字符匹配
    :param str:
    """
    if set(str1) & set(str2) == set(str1):
        return True

    return False

str1 = 'okekwgktczxeposiirjmquypjbohexyinlktaunjyhkjw'
str2 = 'yjynxoawaobtbpyxhbqpzdqjehydzfistxtlzrqzdotglpcunfmpvaparnxkmsybwo'

print(matchingStr(str1, str2))

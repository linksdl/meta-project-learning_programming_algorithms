"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 21:53
@File        : HJ31 单词倒排.py
"""


def reverseStence(str):
    """
    描述
    对字符串中的所有单词进行倒排。

    说明：

    1、构成单词的字符只有26个大写或小写英文字母；

    2、非构成单词的字符均视为单词间隔符；

    3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；

    4、每个单词最长20个字母；

    数据范围：字符串长度满足 1 \le n \le 10000 \1≤n≤10000
    输入描述：
    输入一行，表示用来倒排的句子

    输出描述：
    输出句子的倒排结果
    :param str:
    :return:
    """
    str = str.strip()
    new_str = ''
    str = ' '+ str
    r = 0
    ss = ''
    for i in range(len(str)-1, -1, -1):
        s = str[i]
        if s.isalpha():
            r += 1
            ss = str[i:i+r]
        else:
            new_str += ss + ' '
            r = 0
            ss = ''

    return new_str

print(reverseStence('I am a student'))

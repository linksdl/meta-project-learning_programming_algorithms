"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 18:27
@File        : HJ13 句子逆序.py
"""

# 描述
# 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
#
# 所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
#
# 数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000
#
# 注意本题有多组输入
# 输入描述：
# 输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。
#
# 输出描述：
# 得到逆序的句子

str = input()
strs = str.split()

for i in range(len(strs)-1, -1, -1):
    print(strs[i], end=" ")

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/29 23:24
@File        : HJ63-DNA序列.py
"""


# HJ63 DNA序列

# 一个 DNA 序列由 A/C/G/T 四个字母的排列组合组成。 G 和 C 的比例（定义为 GC-Ratio ）
# 是序列中 G 和 C 两个字母的总的出现次数除以总的字母数目（也就是序列长度）。
# 在基因工程中，这个比例非常重要。因为高的 GC-Ratio 可能是基因的起始点。
#
# 给定一个很长的 DNA 序列，以及限定的子串长度 N ，
# 请帮助研究人员在给出的 DNA 序列中从左往右找出 GC-Ratio 最高且长度为 N 的第一个子串。
# DNA序列为 ACGT 的子串有: ACG , CG , CGT 等等，但是没有 AGT ， CT 等等
#
# 数据范围：字符串长度满足 1 \le n \le 1000 \1≤n≤1000  ，
# 输入的字符串只包含 A/C/G/T 字母

# 输入描述：
# 输入一个string型基因序列，和int型子串的长度
#
# 输出描述：
# 找出GC比例最高的子串,如果有多个则输出第一个的子串


def getHighestRationDNA(s, n):
    """
    HJ63 DNA序列
    :param s: 输入一个string型基因序列，和int型子串的长度
    :param n:
    :return: 找出GC比例最高的子串,如果有多个则输出第一个的子串
    """
    # G C
    l = len(s)
    if n >= l:
        print(s)
    max_n = 0
    gc = ''
    for i in range(0, l-n):
        ss = s[i:(i+n)]
        cc = [x for x in ss if x=='C' or x=='G']
        if len(cc) > max_n:
            max_n = len(cc)
            gc = ss
            # print(ss, max_n)
            # print(ss)

    print(gc)


getHighestRationDNA('AACTGTGCACGACCTGA', 5)



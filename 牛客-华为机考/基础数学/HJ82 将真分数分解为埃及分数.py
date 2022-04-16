"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/2 12:27
@File        : HJ82 将真分数分解为埃及分数.py
"""

# HJ82 将真分数分解为埃及分数

# 描述
# 分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
# 注：真分数指分子小于分母的分数，分子和分母有可能gcd不为1！
# 如有多个解，请输出任意一个。

# 输入描述：
# 输入一个真分数，String型
#
# 输出描述：
# 输出分解后的string


def fenshu(s):

    a = int(s.split('/')[0])
    b = int(s.split('/')[1])

    c = 0
    # b/(a+b)
    # a/b = 1/c + m
    # m = a/b - 1/c
    o_s = ''
    while a != 1:
        if (b % (a-1)) == 0:
            o_s += '1/' + str(int(b/(a-1))) + '+'
            a = 1
            print(o_s)
        else:
            c = int(b / a + 1)
            o_s += '1/' + str(c) + '+'
            a = int(a * c - b)
            b *= c
            if b % a == 0:
                b = int(b / a)
                a = 1 # 直接跳出循环

    o_s += '1/'+str(b)
    print(o_s)


fenshu('8/11')
fenshu('2/4')
fenshu('4/31')


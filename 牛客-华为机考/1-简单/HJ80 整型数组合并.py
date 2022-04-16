"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 13:50
@File        : HJ80 整型数组合并.py
"""


# 描述
# # 题目标题：
# #
# # 将两个整型数组按照升序合并，并且过滤掉重复数组元素。
# # 输出时相邻两数之间没有空格。
# #
# # 输入描述：
# # 输入说明，按下列顺序输入：
# # 1 输入第一个数组的个数
# # 2 输入第一个数组的数值
# # 3 输入第二个数组的个数
# # 4 输入第二个数组的数值
# #
# # 输出描述：
# # 输出合并之后的数组


def mergeInteger(m, a, n, b):
    """
    HJ80 整型数组合并
    将两个整型数组按照升序合并，并且过滤掉重复数组元素。
    :param m:
    :param a:
    :param n:
    :param b:
    :return:
    """
    a = sorted(a)
    b = sorted(b)
    # print(a)
    # print(b)

    c = []
    if a[0] <= b[0]:
        c.append(a[0])
    else:
        c.append(b[0])

    i = 0
    j = 0
    while i <m and j < n:
        print('---',i, j, c)
        if a[i] < b[j]:
            if a[i] != c[-1]:
                c.append(a[i])
            i += 1
        elif a[i] == b[j]:
            if a[i] != c[-1]:
                c.append(a[i])
            i += 1
            j += 1
        else:
            if b[j] != c[-1]:
                c.append(b[j])
            j += 1
        print('+++',i, j, c)

    if i < m:
        c.extend(a[i:])
    if j < n:
        c.extend(b[j:])

    s = [str(x) for x in c]
    print(''.join(s))


mergeInteger(3, [1,2,5], 4, [-1,0,3,2])
mergeInteger(6, [2,8,3,6,3,2], 6, [6,3,6,2,8,11])

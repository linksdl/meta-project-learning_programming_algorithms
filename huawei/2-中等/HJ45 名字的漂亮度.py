"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 14:36
@File        : HJ45 名字的漂亮度.py
"""


# HJ45 名字的漂亮度

def calScore(n, names):
    """
    HJ45 名字的漂亮度
    :param n:
    :param s:
    :return:
    """

    record = {}
    for s in names:
        record[s] = record.get(s, 0) + 1
    # print(record)
    r = sorted(record.items(), key=lambda x:x[1], reverse=True)

    scores = {}
    i = 0
    for k,v in r:
        scores[k] = 26-i
        i += 1

    total = 0
    for s in names:
        total += scores.get(s)

    print(total)






calScore(2, 'zhangsan')
#
# while True:
#     try:
#         n = int(input())
#         for i in range(n):
#             s = input()
#             calScore(n, s)
#     except:
#         break

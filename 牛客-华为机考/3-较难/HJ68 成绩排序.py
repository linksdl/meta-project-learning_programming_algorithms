"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:23
@File        : HJ68 成绩排序.py
"""


def sortScore(scores, flag):

#     sort_s = sorted(scores.items(), key=lambda x:x[1], reverse=flag)
    scores.sort(key=lambda x:x[1], reverse = flag )
    for s in scores:
        print(s[0], s[1])


while 1:
    try:
        n = int(input())
        if input() == "0":
            flag = True
        else:
            flag = False
        scores = []
        for i in range(n):
            name, score = input().split()
            scores.append((name,int(score)))
        sortScore(scores, flag)
    except:
        break

# nums = {'jack': 70,'peter':96, 'Tome': 70, 'smith': 67}
# sortScore(nums)

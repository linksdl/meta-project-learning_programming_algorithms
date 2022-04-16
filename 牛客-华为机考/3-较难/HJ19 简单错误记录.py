"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:47
@File        : HJ19 简单错误记录.py
"""


l = []
ll = []
while 1:
    try:
        s = input().split('\\')[-1]
        data = s.split(' ')[0][-16:] + ' ' + s.split(' ')[1]
        if data not in l:
            l.append(data)
            ll.append(1)
        else:
            ll[l.index(data)] += 1
    except:
        break

for i in range(len(l[-8:])):
    print(l[-8:][i], ll[-8:][i])

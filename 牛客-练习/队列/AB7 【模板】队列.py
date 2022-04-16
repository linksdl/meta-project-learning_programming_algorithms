"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 16:24
@File        : AB7 【模板】队列.py
"""


while True:
    try:
        n = int(input())
        q = list()
        for _ in range(n):
            a = input()
            if a.split()[0] == 'push':
                b = a.split()[1]
                q.append(int(b))
            elif a == 'pop':
                if len(q) == 0:
                    print('error')
                else:
                    print(q.pop(0))
            if a == 'front':
                if len(q) == 0:
                    print('error')
                else:
                    print(q[0])
    except:
        break

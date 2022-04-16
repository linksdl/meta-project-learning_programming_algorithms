"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 16:19
@File        : AB1 【模板】栈.py
"""

while True:

    try:
        n = int(input())

        q = list()
        for _ in range(n):
            cstr = input().split()
            #         c, x = cstr[0], int(cstr[1])
            q = []
            if len(cstr) == 2:
                n = int(cstr[1])
                q.append(n)
                print(n)

            if len(cstr) == 1 and cstr[0] == 'pop':
                if len(q) >= 1:
                    n = q.pop()
                    print(n)
                else:
                    print('error')

            if len(cstr) == 1 and cstr[0] == 'top':
                if len(q) >= 1:
                    q.top()
                else:
                    print('error')

    except:
        break

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 23:50
@File        : 好朋友1.py
"""

while True:
    N = int(input())
    height = list(map(int, input().split()))
    friend = []

    for i in range(N):
        for j in range(i + 1, N):
            if height[j] > height[i]:
                friend.append(j)
                break
            # else:
            #     friend.append(0)
    # 这里感觉写复杂了
    ans = ''.join(str(x) for x in friend)
    # 这里最后只得到‘126556‘所以为了补齐，选择用ljust
    print(' '.join(ans.ljust(N, '0')))
    # print(ans)


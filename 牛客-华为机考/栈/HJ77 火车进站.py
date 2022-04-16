"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 09:41
@File        : HJ77 火车进站.py
"""

# HJ77 火车进站


# 描述
# 给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
# 要求输出所有火车出站的方案，以字典序排序输出。
# 数据范围：1\le n\le 10\1≤n≤10
# 进阶：时间复杂度：O(n!)\O(n!) ，空间复杂度：O(n)\O(n)
# 输入描述：
# 第一行输入一个正整数N（0 < N <= 10），第二行包括N个正整数，范围为1到10。
#
# 输出描述：
# 输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。


result = []


def dfs(wait, stack, out):
    if not wait and not stack:
        result.append(' '.join(map(str, out)))
    if wait:
        dfs(wait[1:], stack + [wait[0]], out)
    if stack:
        dfs(wait, stack[:-1], out+[stack[-1]])



n = 3
nums = [1, 2, 3]

dfs(nums, [], [])
for i in sorted(result):
    print(i)


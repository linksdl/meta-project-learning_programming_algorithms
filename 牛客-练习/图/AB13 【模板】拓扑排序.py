"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 17:51
@File        : AB13 【模板】拓扑排序.py
"""


n, m = map(int, input().split())
graph = dict((str(i),[]) for i in range(1, n+1))
# print(graph)
for i in range(m):
    j, k = input().split()
    graph[j].append(k)
# print(graph)

in_degree = dict((i, 0) for i in graph)
for i in graph:
    for j in graph[i]:
        in_degree[j] += 1

lis = [i for i in in_degree if in_degree[i]==0]
res = []
while lis:
    c = lis.pop()
    res.append(c)
    for i in graph[c]:
        in_degree[i] -= 1
        if in_degree[i]==0:
            lis.append(i)
if len(res) == n:
    print(' '.join(res))
else:
    print(-1)

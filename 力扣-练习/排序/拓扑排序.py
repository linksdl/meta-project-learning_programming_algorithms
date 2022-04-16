"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 23:53
@File        : 拓扑排序.py
"""



import collections

def topoSort(edges):  # 拓扑排序

    n = len(edges)

    # 有向图

    graph = collections.defaultdict(list)

    # 节点入度数组

    inDeg = [0] * n

    # 建立有向图, 并将有向边指向节点的入度 + 1

    for edge in edges:

        a, b = edge

        graph[a].append(b)

        inDeg[b] += 1

    # 队列, 用于求解拓扑排序序列 (对应多源 BFS 过程)

    que = collections.deque([])

    # 所求的拓扑排序序列

    res = []

    # 初始化: 将入度为 0 的节点入队

    for i in range(n):

        if inDeg[i] == 0:

            que.append(i)

    # 队列不为空时, 循环

    while que:

        # 取出队头节点, 并记为 curNode

        curNode = que.popleft()

        # 加入所求的拓扑排序结果中

        res.append(curNode)

        # 遍历 curNode 的邻接节点 nxtNode

        for nxtNode in graph[curNode]:

            # 将nxtNode的入度 - 1

            inDeg[nxtNode] -= 1

            # 若nxtNode的入度减为 0, 则将其入队

            if inDeg[nxtNode] == 0:

                que.append(nxtNode)

    # 当且仅当所求的拓扑排序序列的长度为 n 时, 该拓扑排序序列才是合法的, 并将其返回

    # 否则, 拓扑排序序列不存在, 直接返回空

    return res if len(res) == n else []

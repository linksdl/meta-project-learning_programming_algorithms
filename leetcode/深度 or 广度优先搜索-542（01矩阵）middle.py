#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/13 7:44 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 深度 or 广度优先搜索-542（01矩阵）middle.py

'''
542. 01 矩阵
https://leetcode-cn.com/problems/01-matrix
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
'''
import collections


class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        dis = [[0] * n for _ in range(m)]
        zeros = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        q = collections.deque(zeros)
        visited = set(zeros)

        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    dis[ni][nj] = dis[i][j] + 1
                    q.append((ni, nj))
                    visited.add((ni, nj))
        return dis

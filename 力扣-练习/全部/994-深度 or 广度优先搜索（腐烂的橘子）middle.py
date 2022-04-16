#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/13 8:24 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 994-深度 or 深度优先搜索（腐烂的橘子）middle.py

'''
994. 腐烂的橘子
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
https://leetcode-cn.com/problems/rotting-oranges

输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
'''


class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        mins = 0
        while fresh:
            if not bad: return -1
            bad = {(i + di, j + dj) for i, j in bad for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if (i + di, j + dj) in fresh}
            fresh -= bad
            mins += 1
        return mins

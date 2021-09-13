#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/13 4:29 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 深度 or 广度优先搜索-695（岛屿的最大面积）middle.py

'''
695. 岛屿的最大面积
https://leetcode-cn.com/problems/max-area-of-island
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        area, row, col = 0, len(grid), len(grid[0])

        def dfs(x, y):
            if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                grid[x][y] == 0
                return 1 + dfs(x-1, y) + dfs(x, y+1) + dfs(x+1, y) + dfs(x, y-1)
            else:
                return 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    area = max(dfs(x, y), area)

        return area



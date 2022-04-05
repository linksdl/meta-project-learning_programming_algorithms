"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 18:50
@File        : HJ43 迷宫问题.py
"""


# HJ43 迷宫问题


def mingong(nums):
    """
    定义一个二维数组 N*M ，如 5 × 5 数组下所示：
    输入描述：
    输入两个整数，分别表示二维数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
    输出描述：
    左上角到右下角的最短路径，格式如样例所示。
    :return:
    """
    m = len(nums)
    n = len(nums[0])

    path = []
    visited = set()
    def dfs_1(i, j):
        """
        深度搜索
        :param i:
        :param j:
        """
        if (i,j) in visited or i < 0 or i >= m or j < 0 or j >= n or nums[i][j]:
            return False

        visited.add((i, j))
        path.append('({},{})'.format(i, j))

        if (i, j) == (m-1, n-1) or dfs_1(i+1, j) or dfs_1(i, j+1) or dfs_1(i-1, j) or dfs_1(i, j-1):
            return True

        path.pop()
        return False

    dfs_1(0, 0)
    for l in path:
        print(l)


# nums = [[0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0]]
nums = [[0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0]]
mingong(nums)

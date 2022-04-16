"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 18:09
@File        : 104. 二叉树的最大深度.py
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0

        def dfs_max_depth(node, depth):
            # global max_depth
            if not node:
                return 0
            if not node.left and not node.right:
                return max(max_depth, depth)

            return max(dfs_max_depth(node.left, depth + 1), dfs_max_depth(node.right, depth + 1))

        return dfs_max_depth(root, 1)

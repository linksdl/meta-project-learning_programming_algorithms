"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 20:30
@File        : 112. 路径总和.py
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs_path(root, target):
            if not root:
                return False

            if not root.left and not root.right:
                # print(root.val, target)
                return root.val == target

            return dfs_path(root.left, target - root.val) or dfs_path(root.right, target - root.val)

        return dfs_path(root, targetSum)

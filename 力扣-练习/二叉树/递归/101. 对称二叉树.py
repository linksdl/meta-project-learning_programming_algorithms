"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 20:05
@File        : 101. 对称二叉树.py
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSame(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False

            if tree1.val == tree2.val and isSame(tree1.left, tree2.right) and isSame(tree1.right, tree2.left):
                return True
            else:
                return False

        return isSame(root, root)

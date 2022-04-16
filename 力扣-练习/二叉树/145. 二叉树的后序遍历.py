"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 17:25
@File        : 145. 二叉树的后序遍历.py
"""


# 二叉树的后序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postOrder(root):
            if not root:
                return

            postOrder(root.left)
            postOrder(root.right)
            res.append(root.val)

        postOrder(root)
        return res

#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/13 5:49 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 116-深度 or 深度优先搜索（填充每个节点的下一个右侧节点指针）middle.py

'''
116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
'''

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node'):
        if not root:
            return root

        lefthead = root
        while lefthead.left:
            head = lefthead
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            lefthead = lefthead.left
        return root





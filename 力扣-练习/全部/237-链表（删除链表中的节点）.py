#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/11/1 7:20 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode_python
# @File        : 237-链表（删除链表中的节点）.py

'''
237. 删除链表中的节点
请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。

题目数据保证需要删除的节点 不是末尾节点 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 16:08
@File        : AB12 删除链表的节点.py
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param val int整型
# @return ListNode类
#
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # write code here

        if head == None:
            return head

        res = head
        if head.val == val:
            head = head.next
            return head

        while head.next.val != val:
            head = head.next

        head.next = head.next.next

        return res

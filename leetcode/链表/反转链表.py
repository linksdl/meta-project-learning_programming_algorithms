"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 23:56
@File        : 反转链表.py
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        p = dummy.next

        dummy.next = None

        while p:
            q = p.next
            p.next = dummy.next
            dummy.next = p
            p = q

        return dummy.next

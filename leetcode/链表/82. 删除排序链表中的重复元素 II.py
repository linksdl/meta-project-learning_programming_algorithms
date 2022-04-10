"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 23:56
@File        : 82. 删除排序链表中的重复元素 II.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def deletezDuplicates(self, head:ListNode):
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

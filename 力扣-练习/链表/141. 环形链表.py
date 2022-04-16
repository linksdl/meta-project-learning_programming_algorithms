"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 11:10
@File        : 141. 环形链表.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 方法一：哈希表
    def hasCycle(self, head: ListNode):
        seen = set()
        while head:
            if head in seen:
                return True

            seen.add(head)
            head = head.next
        return False

    # 方法二：快慢指针
    def hasCycle1(self, head: ListNode):
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True






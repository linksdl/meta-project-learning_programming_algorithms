"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 11:19
@File        : 相交链表.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 方法一：哈希表
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        if not headA or not headB:
            return None

        seen = set()
        temp1 = headA
        while temp1:
            seen.add(temp1)
            temp1 = temp1.next

        temp2 = headB
        while temp2:
            if temp2 in seen:
                return temp2

            temp2 = temp2.next

        return None

    # 方法二：双指针
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode):
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        while pA and pB:
            if pA == pB:
                return pA

            pA = pA.next
            pB = pB.next

            if pA is None and pB is None:
                return None
            if pA is None:
                pA = headB
            if pB is None:
                pB = headA











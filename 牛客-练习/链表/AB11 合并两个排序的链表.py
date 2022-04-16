"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 15:57
@File        : AB11 合并两个排序的链表.py
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        if pHead1 is None and pHead2 is None:
            return None

        head = cur = ListNode(0)
        cur1 = pHead1
        cur2 = pHead2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        cur.next = cur1 if cur1 else cur2
        return head.next

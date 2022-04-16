"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 15:29
@File        : AB10 反转链表.py
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        prev = None
        temp = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

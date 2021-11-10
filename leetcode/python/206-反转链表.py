#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/15 8:44 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 206-反转链表.py

'''
206. 反转链表
https://leetcode-cn.com/problems/reverse-linked-list/
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        while head:
            temp = head.next
            head.next = ans
            ans = head
            head = temp

        return ans

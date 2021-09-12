#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/12 1:48 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 双指针-19（删除链表的倒数第N个节点）middle.py

'''
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Soluction:
    def removeNthFromEnd(self, head: ListNode, n):
        dummy = ListNode(0, head)
        first = head
        second = dummy

        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

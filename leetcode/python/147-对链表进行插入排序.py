#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/15 6:50 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 147-对链表进行插入排序.py

'''
147. 对链表进行插入排序
对链表进行插入排序。
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
https://leetcode-cn.com/leetbook/read/sort-algorithms/euvypr/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummyNode = ListNode(0)
        dummyNode.next = head
        sortedNode = head
        currentNode = head.next
        while currentNode:
            if sortedNode.val <= currentNode.val:
                sortedNode = sortedNode.next
            else:
                previousNode = dummyNode
                while previousNode.next.val <= currentNode.val:
                    previousNode = previousNode.next
                sortedNode.next = currentNode.next
                currentNode.next = previousNode.next
                previousNode.next = currentNode
            currentNode = sortedNode.next
        return dummyNode.next

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 08:25
@File        : HJ48 从单向链表中删除指定值的节点.py
"""


class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SingleLinkedList():
    def __init__(self):
        self.head = Node()
        self.length = 0

    def insert(self, val1, val2):
        """
        构造链表 插入节点
        :param val1:
        :param val2:
        :return:
        """
        cur = self.head
        node = Node(val2)

        while cur:
            if cur.val == val1:
                node.next = cur.next
                cur.next = node
                break
            else:
                cur = cur.next

    def remove(self, val):
        """
        删除节点
        :param val:
        :return:
        """
        cur = self.head
        pre = None
        while cur:
            if cur.val == val:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def walkthrough(self):
        """
        遍历链表
        :return:
        """
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()


def removeFromLinkedList(n, nums, k):
    """
    # HJ48 从单向链表中删除指定值的节点
    :param n:
    :param nums:
    :return:
    """

    L = SingleLinkedList()
    L.length = n
    L.head.val = nums[0]
    # print(L.head.val)
    lst = nums[1:]
    # print(lst)
    i, j, pairs = 0, 1, []
    while i < len(lst):
        pairs.append((lst[i], lst[j]))
        i += 2
        j += 2
    # print(pairs)
    for p in pairs:
        L.insert(p[1], p[0])
    L.remove(k)
    L.walkthrough()


removeFromLinkedList(5, [2, 3, 2, 4, 3, 5, 2, 1, 4], 3)
removeFromLinkedList(6, [2, 1, 2, 3, 2, 5, 1, 4, 5, 7, 2], 2)

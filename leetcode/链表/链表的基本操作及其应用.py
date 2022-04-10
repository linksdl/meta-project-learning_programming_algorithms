"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 23:25
@File        : 链表的基本操作及其应用.py
"""


class ListNode: # 单链表数据结构定义

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 插入一个节点 node 至链表 head 头部, 并返回操作后的链表
    def insertNodeAsFirst(self, head, node):
        # 初始化虚拟头节点 dummy
        dummy = ListNode(0, head)

        # 待插入节点 node 指向 dummy 指向的节点(第一个数据节点)
        node.next = dummy.next

        # dummy 指向 node, 完成插入操作
        dummy.next = node

        # dummy.next 即为操作后的链表
        return dummy.next

    def deleteFirstNode(head):  # 删除链表 head 中的第一个数据节点, 并返回操作后的链表

        dummy = ListNode(0, head)

        # 指针 p 指向待删除的节点(第一个数据节点)

        p = dummy.next

        # dummy 指向待删除节点的后继节点

        dummy.next = p.next

        # 释放节点 p 占有的内存, 完成删除操作

        del p

        return dummy.next


def reverseListRecur(head):  # 反转链表 head (递归)

    # 当前链表 head 为空, 或 head 无后继节点 (链表长度为 1), 直接返回head

    if not head or not head.next:
        return head

    # 自顶向下递归, 反转链表 head.next, 结果记为 res

    res = reverseListRecur(head.next)

    # 自底向上回溯, 该过程中: 将 head 头插到 res

    head.next.next = head

    head.next = None

    # 最终, res即为所求

    return res


def reverseListIter(head):  # 反转链表 head (迭代)

    dummy = ListNode(0, head)

    # 指针 p 指向第一个数据节点

    p = dummy.next

    # dummy 的指针域置空 (与第一个数据节点断开连接), 从而将数据节点依次头插到 dummy 后面

    dummy.next = None

    # 指针 p 未指向空节点时, 循环

    while p:
        # 指针 q 指向 p 的后继节点

        q = p.next

        # 将指针 p 指向的节点头插到 dummy 后面

        p.next = dummy.next

        dummy.next = p

        # 指针 p 指向 q, 即 p 的后继节点

        p = q

    return dummy.next


def removeElementsRecur(head, val):  # 删除链表中所有节点值为 val 的元素 (递归)

    # 当前链表 head 为空, 直接返回 head

    if not head:
        return head

    # 自顶向下递归, 删除链表 head.next 所有节点值为 val 的元素

    head.next = self.removeElements(head.next, val)

    # 自底向上回溯, 若当前节点值 head.val 恰好为 val, 则返回以 head.next 为头节点的链表作为最终结果

    # 否则, 返回以 head 为头节点的链表作为最终结果

    return head.next if head.val == val else head


def removeElementsIter(head, val):  # 删除链表中所有节点值为 val 的元素 (迭代)

    dummy = ListNode(0, head)

    # 伴随指针: 指针 p 指向第一个数据节点, pre 指向 p 的前驱节点

    pre, p = dummy, dummy.next

    # 指针 p 未指向空节点时, 循环

    while p:

        # 若 p.val 恰好为 val, 将节点 p 删除

        if p.val == val:

            # 指针 q, 指向指针 p 指向的节点

            q = p

            # 指针 p 指向其后继

            p = p.next

            # 原指针 p 的前驱节点指向原指针 p 的后继节点 (当前指针 p)

            pre.next = p

            # 释放指针 q 指向的节点占有的内存, 完成删除操作

            del q

        # 否则, pre 和 p 伴随移动, 均指向其后继节点

        else:

            pre = p

            p = p.next

    return dummy.next


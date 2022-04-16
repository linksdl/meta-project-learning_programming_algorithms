"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 23:36
@File        : 链表中的双指针问题.py
"""


class ListNode:  # 单链表数据结构定义

    def __init__(self, val=0, next=None):
        self.val = val

        self.next = next


def searchKthFromEnd(head, k):  # 寻找链表head中的倒数第k个节点

    # 初始化快慢指针slow和fast, 二者均指向head的第一个数据节点

    slow, fast = head, head

    # 快指针fast先向右移动k步

    while k:
        fast = fast.next

        k -= 1

    # 快指针fast未指向空节点时, 慢指针slow和快指针fast同时向右移动一步

    while fast:
        slow = slow.next

        fast = fast.next

    # 最终, 慢指针slow指向的节点, 即为所求

    return slow


def detectCycle(head):  # 判断链表head中是否存在环，若存在环则返回环的入口节点

    # 初始化快慢指针slow和fast, 二者均指向head的第一个节点

    slow, fast = head, head

    # 快指针未指向空节点, 且未指向链表最后一个节点时, 循环

    while fast and fast.next:

        # 慢指针每次向右移动1步, 而快指针每次向右移动2步

        slow = slow.next

        fast = fast.next.next

        # 快慢指针相遇时, 跳出循环

        if slow == fast:

            break

    # 若上述移动过程中, 快指针指向空节点或指向链表最后一个节点

    # 则链表不存在环, 自然也就不存在环的入口节点

    if not fast or not fast.next:

        return None

    # 否则, 重新初始化快指针, 指向head的第一个节点

    fast = head

    # 快慢指针未相遇时, 二者每次均向右移动1步

    while slow != fast:

        slow = slow.next

        fast = fast.next

    # 直到快慢指针相遇, 它们指向的节点即为所求

    return slow


def mergeSortedList(head1, head2):  # 合并两个有序链表head1和head2, 并返回合并后的新链表

    # 两有序链表合并后的结果

    dummy = ListNode(0, None)

    # 尾指针, 指向dummy的尾节点

    r = dummy

    # 初始化双指针

    left, right = head1, head2

    # left或right未指向各自链表末尾时, 循环

    while left or right:

        # left和right均未指向各自数组末尾时

        # 将二者中节点值较小的一者添加到结果, 并将对应指针向右移动一位

        # 特殊地, 二者节点值相等时, 移动left或right均可, 对结果无影响

        if left and right:

            if left.val < right.val:

                r.next = left

                r = left

                left = left.next

            else:

                r.next = right

                r = right

                right = right.next

        # right已指向链表head2的末尾, 则将head1中的剩余节点添加到结果

        elif left:

            r.next = left

            r = left

            left = left.next

        # left已指向数组nums1的末尾, 则将head2中的剩余节点添加到结果

        elif right:

            r.next = right

            r = right

            right = right.next

    # 尾节点后没有其它节点, 其指针域置空

    dummy.next = None

    # 最终, 返回合并后的结果

    return dummy.next

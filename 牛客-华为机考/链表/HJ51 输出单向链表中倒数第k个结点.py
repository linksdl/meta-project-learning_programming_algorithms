"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/25 15:34
@File        : HJ51 输出单向链表中倒数第k个结点.py
"""


# HJ51 输出单向链表中倒数第k个结点
# 描述
# 输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。
#
# 链表结点定义如下：
# struct ListNode
# {
#     int m_nKey;
#     ListNode* m_pNext;
# };
# 正常返回倒数第k个结点指针，异常返回空指针.
# 要求：
# (1)正序构建链表;
# (2)构建后要忘记链表长度。
# 数据范围：链表长度满足 1 \le n \le 1000 \1≤n≤1000  ， k \le n \k≤n  ，链表中数据满足 0 \le val \le 10000 \0≤val≤10000
#
# 本题有多组样例输入。
# 输入描述：
# 输入说明
# 1 输入链表结点个数
# 2 输入链表的值
# 3 输入k的值
#
# 输出描述：
# 输出一个整数

class Node():
    def __init__(self, val=0):
        self.val = val
        self.next = None


def searchLinkedNode(count, nums, k):
    """

    :param count:
    :param nums:
    :param k:
    """
    head = Node()
    l = len(nums)
    while k:
        head.next = Node(nums.pop())
        head = head.next
        k -= 1
    print(head.val)


while True:
    try:
        count, nums, k = int(input()), list(map(int, input().split())), int(input())
        searchLinkedNode(count, nums, k)

    except EOFError:
        break

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 12:55
@File        : 704. 二分查找.py
"""


# https://leetcode-cn.com/problems/binary-search/

# 给定一个n个元素有序的（升序）整型数组 nums 和一个目标值 target，
# 写一个函数搜索nums 中的 target，如果目标值存在返回下标，否则返回 -1。


# 二分查找 O(logn)
def binary_search(nums, target):
    """
     二分查找 O(logn)
    :param nums:
    :param target:
    :return:
    """

    l = len(nums)
    l_point, r_point = 0, l - 1
    while l_point <= r_point:
        mid = (r_point - l_point) // 2 + l_point
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l_point = mid + 1
        else:
            r_point = mid - 1
    return -1


res = binary_search([-1, 0, 3, 5, 9, 12], 9)
print(res)

# https://leetcode-cn.com/leetbook/read/binary-search/xe5fpe/

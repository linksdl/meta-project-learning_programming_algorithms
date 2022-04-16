"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 13:03
@File        : 二分查找模板 I.py
"""


# https://leetcode-cn.com/leetbook/read/binary-search/xe5fpe/

# 模板
# #1 是二分查找的最基础和最基本的形式。
# 这是一个标准的二分查找模板，大多数高中或大学会在他们第一次教学生计算机科学时使用。
# 模板 #1 用于查找可以通过访问数组中的单个索引来确定的元素或条件。

# 关键属性
# 二分查找的最基础和最基本的形式。
# 查找条件可以在不与元素的两侧进行比较的情况下确定（或使用它周围的特定元素）。
# 不需要后处理，因为每一步中，你都在检查是否找到了元素。如果到达末尾，则知道未找到该元素。

# 区分语法
# 初始条件：left = 0, right = length-1
# 终止：left > right
# 向左查找：right = mid-1
# 向右查找：left = mid+1

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

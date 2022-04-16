"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 17:17
@File        : 34. 在排序数组中查找元素的第一个和最后一个位置.py
"""


# 34. 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/


def searchRange(nums, target):
    """
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    :param nums:
    :param target:
    """

    if not nums:
        return [-1, -1]

    n = len(nums)

    def leftBinarySearch():
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1

    def rightBinarySearch():
        """
        右边搜索
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l+1)//2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return l if nums[l] == target else -1

    return [leftBinarySearch(), rightBinarySearch()]








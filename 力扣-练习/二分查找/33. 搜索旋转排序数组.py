"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 14:51
@File        : 33. 搜索旋转排序数组.py
"""


def search(nums, target):
    """
    搜索旋转排序数组
    :param nums:
    :param target:
    :return:
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[mid] > target >= nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

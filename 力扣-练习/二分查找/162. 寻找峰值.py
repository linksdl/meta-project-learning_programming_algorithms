"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 16:03
@File        : 162. 寻找峰值.py
"""


# 162. 寻找峰值
# https://leetcode-cn.com/problems/find-peak-element/

# 模版2
def findPeakElement(nums):
    """
    寻找峰值
    :param nums:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


def findPeakElement1(nums):
    """
    寻找峰值
    :param nums:
    """
    left, right = 0, len(nums) - 1
    while left < right - 1:
        mid = left + (right-left)//2
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid

    if nums[left] > nums[right]:
        return left
    else:
        return right

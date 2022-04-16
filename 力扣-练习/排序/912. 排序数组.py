"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 18:03
@File        : 912. 排序数组.py
"""


# 912. 排序数组
import random


def sortArray(nums):
    """
    快速排序
    :param nums:
    :return:
    """

    def random_partition(nums, left, right):
        """

        :param nums:
        :param left:
        :param right:
        :return:
        """
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]
        i = right - 1
        for j in range(left, right):
            if nums[j] < nums[right]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1

        nums[i], nums[right] = nums[right], nums[i]
        return i



nums = [5,1,1,2,0,0]

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 21:40
@File        : 136. 只出现一次的数字.py
"""


# https://leetcode-cn.com/leetbook/read/top-interview-questions/xm0u83/
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 示例 1:
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4

# 数组，位运算，哈希，排序

# 暴力查找，建立haseset 表，map O(n) O（n）
# 排序,O(nlogn)
# 数学知识 减法
# 位运算 亦或

# 方法：位预算 时间 O(n), 空间 O(1)
def singleInteger(nums):
    """
    查找一个数组中只出现一次的数字
    :param nums:
    :return:
    """

    if len(nums) == 1:
        return nums[0]

    res = nums[0]
    for i in range(1, len(nums)):
        res ^= nums[i]
    return res


# 方法：暴力查找 时间 O(n^2), 空间 O(1)
def singleInteger1(nums):
    """
    查找一个数组中只出现一次的数字
    :param nums:
    :return:
    """

    if len(nums) == 1:
        return nums[0]

    for i in range(0, len(nums)):
        if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
            return nums[i]




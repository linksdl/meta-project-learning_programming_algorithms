"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 22:19
@File        : 137. 只出现一次的数字 II.py
"""

# https://leetcode-cn.com/problems/single-number-ii/

# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。
# 请你找出并返回那个只出现了一次的元素。
#
# 示例 1：
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
# 提示：
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次


# 方法一：有限状态自动机
from random import randint


def singleNumber(nums):
    """
    有限状态自动机
    :param nums:
    :return:
    """
    ones, twos = 0, 0
    for num in nums:
        ones = ones ^ num & ~twos
        twos = twos ^ num & ~ones
    return ones


# 方法二：遍历统计
def singleNumber1(nums):
    """
    只出现一次的数字
    :param nums:
    :return:
    """
    counts = [0] * 32
    for num in nums:
        for j in range(32):
            counts[j] += num & 1
            num >>= 1
    res, m = 0, 3
    for i in range(32):
        res <<= 1
        res |= counts[31 - i] % m
    return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)



# 方法： 快速选择分治算法
def singleNumber2(nums):
    """
    快速选择分治算法
    :param nums:
    :return:
    """
    n = len(nums)
    l, r = 0, n - 1
    while l < r:
        k = randint(l, r)
        nums[r], nums[k] = nums[k], nums[r]
        i, j = l, r - 1
        while i <= j:
            while i < r and nums[i] <= nums[r]:
                i += 1
            while j >= l and nums[j] > nums[r]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[i], nums[r] = nums[r], nums[i]
        if (i - l + 1) % 3 != 0:
            r = i
        else:
            l = i + 1
    return nums[l]

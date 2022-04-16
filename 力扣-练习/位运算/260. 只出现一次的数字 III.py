"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 22:33
@File        : 260. 只出现一次的数字 III.py
"""

# 260. 只出现一次的数字 III
# https://leetcode-cn.com/problems/single-number-iii/


# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
# 示例 1：
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 示例 2：
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 示例 3：
# 输入：nums = [0,1]
# 输出：[1,0]


# 方法一：哈希表 O（n）， O（n）


# 方法二：位运算 O（n）， O（1）
def singleNumber(nums):
    """
    方法二：位运算
    :param nums:
    :return:
    """
    xorsum = 0
    for num in nums:
        xorsum ^= num

    lsb = xorsum & (-xorsum)
    type1 = type2 = 0
    for num in nums:
        if num & lsb:
            type1 ^= num
        else:
            type2 ^= num

    return [type1, type2]

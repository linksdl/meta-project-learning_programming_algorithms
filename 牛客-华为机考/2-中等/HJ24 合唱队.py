"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 14:58
@File        : HJ24 合唱队.py
"""


# HJ24 合唱队
# 此题是最长递增子序列的变体，基本思路是对原序列从左到右和从右到左分别求出到每个元素的最长递增子序列的长度。
import bisect

def inc_max(s):
    dp = [1] * len(s)
    arr = [s[0]]

    for i in range(1, len(s)):
        if s[i] > arr[-1]:
            arr.append(s[i])
            dp[i] = len(arr)
        else:
            # 用二分法找到arr中第一个比ele_i大（或相等）的元素的位置
            pos = bisect.bisect_left(arr, s[i])
            arr[pos] = s[i]
            dp[i] = pos + 1
    return dp

def fn_sub(n, nums):
    """
    方法二：借助二分查找
    具体方法
    由于直接使用动态规划，需要两次遍历数组，借助之前求解最长递增子序列的优化思想，借助二分查找来求解。
    用一个num数组记录以i为终点的从左向右和从右向走的子序列元素个数。
    :param n:
    :param nums:
    :return:
    """

    left_s = inc_max(nums)
    right_s = inc_max(nums[::-1])[::-1]
    sum_s = [left_s[i] + right_s[i] - 1 for i in range(len(nums))]
    print(str(n-max(sum_s)))



fn_sub(8, [186,186,150,200,160,130,197,200])


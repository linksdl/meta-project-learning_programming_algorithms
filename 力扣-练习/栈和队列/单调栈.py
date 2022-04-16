"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 13:38
@File        : 单调栈.py
"""



def nextSmallerNum1(nums):  # 求 nums 中各元素右侧 第一个严格小于当前元素的 元素下标 (法一: 暴力)

    n = len(nums)

    # 所求结果

    res = [-1] * n

    # 遍历数组 nums

    for i in range(n):

        # 遍历 nums[i] 右侧的元素, 找第一个严格小于 nums[i] 的元素位置

        for j in range(i + 1, n):

            if nums[i] > nums[j]:

                res[i] = j

                break

    # 返回所求结果

    return res



def nextSmallerNum2(nums):  # 求 nums 中各元素右侧 第一个严格小于当前元素的 元素下标 (法二: 单调栈)

    n = len(nums)

    # 单调栈 (自栈顶向栈底单调减少)

    stack = []

    # 所求结果

    res = [-1] * n

    # 遍历数组 nums

    for i in range(n):

        # 单调栈不为空, 则找到了当前栈顶元素右侧第一个严格小于当前栈顶元素的下标

        # 将其存储到 res 数组, 并出栈

        while stack and nums[stack[-1]] > nums[i]:

            res[stack[-1]] = i

            stack.pop()

        # 当前元素下标入栈

        stack.append(i)

    # 返回所求结果

    return res

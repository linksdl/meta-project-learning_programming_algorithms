"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 14:07
@File        : 84. 柱状图中最大的矩形.py
"""



def largestRectangleArea(heights):

    n = len(heights)
    left, right = [0] * n, [n] * n

    mono_stack = list()
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            right[mono_stack[-1]] = i
            mono_stack.pop()

        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)

    ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
    return ans




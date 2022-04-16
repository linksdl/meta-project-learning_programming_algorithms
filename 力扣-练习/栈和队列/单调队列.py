"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 13:44
@File        : 单调队列.py
"""

import collections


def maxSlidingWindow1(nums, k):  # 滑动窗口的最大值 (法一: 暴力)

    n = len(nums)

    # 所求结果

    res = []

    # 遍历数组 nums

    for i in range(k - 1, n):

        # 维护窗口 [i - k + 1...i] 内的元素最大值 maxv

        maxv = nums[i]

        for j in range(i - 1, i - k, -1):
            maxv = max(maxv, nums[j])

        # maxv 添加到结果中

        res.append(maxv)

    # 最终, res 即为所求

    return res


def maxSlidingWindow2(nums, k):  # 滑动窗口的最大值 (法二: 单调队列)

    n = len(nums)

    # 单调队列 (存储元素下标, 且自队头向队尾, 下标对应的元素值单调减少)

    que_dec = collections.deque([])

    # 所求结果

    res = []

    # 遍历数组 nums

    for i in range(n):

        # 单调性维护: 若当前队尾下标对应的元素值 nums[que_dec[-1]] < 当前遍历的元素 nums[i]

        # 单调队列队尾元素出队

        while que_dec and nums[que_dec[-1]] < nums[i]:
            que_dec.pop()

        # 元素有效性维护: 由于长度为 k 的滑动窗口右边界为 i 时, 其左边界为 i - k + 1

        # 因此, 若当前下标 - 当前队头下标 >= k

        # 则当前队头已经在滑动窗口的左侧, 后面将不再问题求解中使用

        # 需将其出队

        while que_dec and i - que_dec[0] >= k:
            que_dec.popleft()

        # 当前遍历的元素下标 i 入队

        que_dec.append(i)

        # 若当前单调队列不为空, 且当前遍历的元素下标 i >= k - 1

        # 将当前滑动窗口中的最大值添加到结果, 即 nums[que_dec[0]]

        if que_dec and i >= k - 1:
            res.append(nums[que_dec[0]])

    # 最终, res 即为所求

    return res

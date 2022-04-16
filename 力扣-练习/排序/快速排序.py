"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 21:56
@File        : 快速排序.py
"""

import random
import heapq
def partition(nums, left, right):  # 快速排序中的划分过程
    # 随机化初始划分依据的下标 pivotPos
    pivotPos = random.randint(left, right)
    # 将下标 left 和 pivotPos 的元素交换
    nums[left], nums[pivotPos] = nums[pivotPos], nums[left]
    # 从而, 待排序区间首元素作为划分依据
    target = nums[left]
    # 双指针 i 和 j, 分别初始化为待排序区间的首元素和次首元素下标
    i, j = left, left + 1
    # 右指针 j 未指向待排序区间末尾时, 循环
    while j <= right:
        # nums[j] > target, 将其与 nums[i + 1] 交换, 并将左指针 i 向右移动一位
        if nums[j] > target:
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1
        # 右指针向右移动一位
        j += 1
    # 将下标 left 和 i 的元素交换
    nums[left], nums[i] = nums[i], nums[left]
    # 最终, 下标 i 及左侧的元素 <= target, 下标 i 及右侧的元素 >= target
    # 将其返回, 作为一次划分操作后的划分位置
    return i

def quickSelect(nums, left, right, k):  # 快速选择算法
    # 一次划分操作后的划分位置 pivotPos
    # 该位置保证左半区间 [left...pivotPos - 1] 中的元素均 <= a[pivotPos]
    # 右半区间 [pivotPos + 1...right] 中的元素均 >= a[right]
    # 不要求左半和右半区间中的元素必须有序
    pivotPos = partition(nums, left, right)
    # pivotPos == k - 1, 则此时nums[pivotPos]即为所求的第k大元素
    if pivotPos == k - 1:
        return nums[pivotPos]
    # pivotPos > k - 1, 则此时 nums[pivotPos] 比目标的第 k 大元素更大
    # 应在左半区间 [left...pivotPos - 1] 中继续查找
    elif pivotPos > k - 1:
        return quickSelect(nums, left, pivotPos - 1, k)
    # pivotPos < k - 1, 则此时 nums[pivotPos] 比目标的第 k 大元素更小
    # 应在右半区间 [pivotPos + 1...right] 中继续查找
    else:
        return quickSelect(nums, pivotPos + 1, right, k)

def findKthLargest1(nums, k):  # 返回数组 nums 中的第 k 大元素(法一: 基于快速排序 - 快速选择算法)
    # 在对 nums 快速排序的同时求解第 k 大元素, 初始化待排序区间为 [0, n - 1], 其中 n 为数组 nums 的长度
    return quickSelect(nums, 0, len(nums) - 1, k)

def findKthLargest2(nums, k):  # 返回数组 nums 中的第 k 大元素(法二: 基于堆排序算法)
    n = len(nums)
    # 小根堆
    pq = []
    # 遍历数组 nums 中的各个元素
    for i in range(n):
        # 当前小根堆中元素个数 < k, 则 nums[i] 插入小根堆
        if len(pq) < k:
            heapq.heappush(pq, nums[i])
        # 否则 (当前小根堆中元素个数为 k)
        else:
            # 记当前的堆顶元素为 top
            top = pq[0]
            # 若 top < nums[i], 则 top 不再是当前小根堆中第 k 大或更大的元素
            # top 出堆, 并将 nums[i] 插入小根堆
            if top < nums[i]:
                heapq.heappop(pq)
                heapq.heappush(pq, nums[i])
    # 遍历结束后, 小根堆的堆顶元素 pq[0] 即为所求
    return pq[0]

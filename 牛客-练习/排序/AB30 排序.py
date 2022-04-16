"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 17:53
@File        : AB30 排序.py
"""

class Solution:
    def MySort(self, arr):
        # write code here
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr

    def quick_sort(self, arr, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = arr[(start + end) // 2]

        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1

            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        self.quick_sort(arr, start, right)
        self.quick_sort(arr, left, end)

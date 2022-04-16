"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 20:52
@File        : 两个数组的交集 II.py
"""
import collections


def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        return self.intersect(nums2, nums1)

    m = collections.Counter()
    for num in nums1:
        m[num] += 1

    intersection = list()
    for num in nums2:
        if (count := m.get(num, 0)) > 0:
            intersection.append(num)
            m[num] -= 1
            if m[num] == 0:
                m.pop(num)

    return intersection

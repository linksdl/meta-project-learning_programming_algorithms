"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/6 20:29
@File        : 744. 寻找比目标字母大的最小字母.py
"""

# 744. 寻找比目标字母大的最小字母


def nextGreatestLetter(letters, target):
    """

    :param letters:
    :param target:
    :return:
    """
    def binarySearch(letters, target):
        l = len(letters)
        left, right = 0, l - 1
        while left < right:
            mid = left + (right - left) // 2
            if target < letters[mid]:
                right = mid
            else:
                left = mid + 1

        return letters[left]

    return binarySearch(letters, target) if target < letters[-1] else letters[0]


nextGreatestLetter(["c","f","j"], "a")

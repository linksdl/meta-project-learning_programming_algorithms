"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:00
@File        : HJ93 数组分组.py
"""


def splitArr(n, nums):
    """
    HJ93 数组分组
    :param n:
    :param nums:
    :return:
    """
    def fn_split(sum3, sum5, arr):
        """
        递归
        :param sum3:
        :param sum5:
        :param arr:
        :return:
        """
        if len(arr) == 0:
            if sum3 == sum5:
                return True
            else:
                return False
        else:
            return fn_split(sum3 + arr[0], sum5, arr[1:]) or fn_split(sum3, sum5 + arr[0], arr[1:])

    nums5 = []
    nums3 = []
    temp = []
    for n in nums:
        if n % 5 == 0:
            nums5.append(n)
        elif n % 3 == 0:
            nums3.append(n)
        else:
            temp.append(n)

    flag = fn_split(sum(nums3), sum(nums5), temp)
    if flag:
        print('true')
    else:
        print('false')

n = 4
nums = [1, 5, -5, 1]
splitArr(n, nums)
# print(nums[:2])
# print(nums[2:])

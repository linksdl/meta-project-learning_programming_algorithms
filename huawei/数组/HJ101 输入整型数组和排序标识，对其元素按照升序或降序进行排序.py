"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 15:53
@File        : HJ101 输入整型数组和排序标识，对其元素按照升序或降序进行排序.py
"""


def sortIntegerNums(n, nums, acs):
    """
    描述
    输入整型数组和排序标识，对其元素按照升序或降序进行排序
    数据范围： 1 \le n \le 1000 \1≤n≤1000  ，元素大小满足 0 \le val \le 100000 \0≤val≤100000
    输入描述：
    第一行输入数组元素个数
    第二行输入待排序的数组，每个数用空格隔开
    第三行输入一个整数0或1。0代表升序排序，1代表降序排序
    输出描述：
    输出排好序的数字
    :param n:
    :param nums:
    :param acs:
    :return:
    """
    # 升
    if acs == 0:
        d = sorted(nums)
        return ' '.join( [str(x) for x in d] )
    else:
        d = sorted(nums, reverse=True)
        return ' '.join( [str(x) for x in d] )


print(sortIntegerNums(8, [1, 2, 4, 9, 3, 55, 64, 25], 1))

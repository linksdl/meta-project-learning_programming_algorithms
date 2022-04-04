"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/30 20:31
@File        : HJ73 计算日期到天数转换.py
"""


# HJ73 计算日期到天数转换
# 根据输入的日期，计算是这一年的第几天。
# 保证年份为4位数且日期合法。
# 进阶：时间复杂度：O(n) ，空间复杂度：O(1)

# 输入描述：
# 输入一行，每行空格分割，分别是年，月，日
#
# 输出描述：
# 输出是这一年的第几天

def computeDay(year, month, day):
    """
    HJ73 计算日期到天数转换
    :param year:
    :param month:
    :param day:
    """

    #
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    days_feb = 28
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                days_feb = 29
        else:
            days_feb = 29
    else:
        days_feb = 28

    day_th = 0
    for m in range(1, month):
        if m in days_30:
            day_th += 30
        elif m in days_31:
            day_th += 31
        elif m == 2:
            day_th += days_feb

        print(day_th, m)

    day_th += day
    print(day_th)


computeDay(2012, 12, 31)
# computeDay(1982, 3, 4)


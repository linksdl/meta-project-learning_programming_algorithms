"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 15:06
@File        : HJ7-RoundInteger.py
"""


def maxInteger(num):
    """
    写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
    数据范围：保证输入的数字在 32 位浮点数范围内
    """
    num = float(num)

    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

print(maxInteger(2.3))

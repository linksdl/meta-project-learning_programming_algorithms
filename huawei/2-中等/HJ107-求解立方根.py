"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 10:14
@File        : HJ107-求解立方根.py
"""


# HJ107 求解立方根

# 描述
# 计算一个浮点数的立方根，不使用库函数。
# 保留一位小数。
#
# 数据范围：|val| \le 20 \∣val∣≤20
#
# 输入描述：
# 待求解参数，为double类型（一个实数）
#
# 输出描述：
# 输出参数的立方根。保留一位小数。


def doubleRoot(n):
    """
    计算一个浮点数的立方根，不使用库函数。保留一位小数。
    :param n:
    :return:
    """

    esp = 0.00001
    t = n
    # 牛顿法求解
    while abs(t ** 3 - n) > esp:
        t = t - (t*t*t - n) * 1.0 / (3 * t * t)
    print("%.1f" % t)


doubleRoot(216)


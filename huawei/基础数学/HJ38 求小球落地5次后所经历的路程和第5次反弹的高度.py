"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/2 11:02
@File        : HJ38 求小球落地5次后所经历的路程和第5次反弹的高度.py
"""

# 假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？



def bollHight(n):
    """
    HJ38 求小球落地5次后所经历的路程和第5次反弹的高度

    输入描述：
    输入起始高度，int型

    输出描述：
    分别输出第5次落地时，共经过多少米以及第5次反弹多高。
    注意：你可以认为你输出保留六位或以上小数的结果可以通过此题。
    :param n:
    :return:
    """

    # f(1) = n
    # f(2) = f(1) + f(1)/2
    def gethight(n, m):
        """
        第m次的反弹高度,
        :param n:
        :param m:
        """

        return n/(2 ** m) * 2

    total = n
    for i in range(2, 6):
        total += gethight(n, i-1)

    print(total)
    print(gethight(n, 6))


bollHight(1)

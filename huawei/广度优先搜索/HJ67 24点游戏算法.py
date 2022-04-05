"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 18:19
@File        : HJ67 24点游戏算法.py
"""


# HJ67 24点游戏算法


def dfs_24points(nums):
    """
    描述
    给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,
    运算符仅允许出现在两个数字之间,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且需考虑括号运算
    此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，
    但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。

    输入描述：
    读入4个[1,10]的整数，数字允许重复，测试用例保证无异常数字。

    输出描述：
    对于每组案例，输出一行表示能否得到24点，能输出true，不能输出false
    :param nums:
    :return:
    """

    if not nums:
        return False
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6

    visited = [False] * len(nums)

    def fn_dfs(n, total):
        """
        dfs 递归
        :param n:
        :param total:
        :return:
        """
        if n == 4 and total == 24:
            return True
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                if fn_dfs(n + 1, total + nums[i]) or fn_dfs(n + 1, total - nums[i]) or fn_dfs(n + 1, total * nums[i]) or fn_dfs(n + 1, total / nums[i]):
                    return True

                visited[i] = False

        return False

    if fn_dfs(0, 0):
        print('true')
    else:
        print('false')


dfs_24points([7, 2, 1, 10])
dfs_24points([2, 9, 9, 5])

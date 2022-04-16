"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/7 13:53
@File        : 796. 旋转字符串.py
"""

# https://leetcode-cn.com/problems/rotate-string/

# 方法一：模拟 暴力匹配 O（n^2）


# 方法二：搜索子字符串  O(n), O(n) - KMP算法用于子串配问题 goal in s + s
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        796. 旋转字符串
        :param s:
        :param goal:
        :return:
        """

        return len(s) == len(goal) and goal in s + s

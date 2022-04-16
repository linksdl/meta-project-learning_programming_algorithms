"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 17:35
@File        : AB2 栈的压入、弹出序列.py
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pushV int整型一维数组
# @param popV int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsPopOrder(self, pushV: List[int], popV: List[int]) -> bool:
        # write code here

        j = 0
        stack = []
        for x in pushV:
            stack.append(x)
            while stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1

        return j == len(popV)

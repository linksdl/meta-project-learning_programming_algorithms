"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 15:37
@File        : 402. 移掉 K 位数字.py
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        numStack = []
        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)

        finalStack = numStack[:-k] if k else numStack

        return "".join(finalStack).lstrip('0') or "0"



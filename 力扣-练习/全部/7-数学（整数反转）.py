#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/11/1 3:32 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode_python
# @File        : 7-数学（整数反转）.py

'''
7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
'''


class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        ans = 0
        while x != 0:
            # check the value of ans
            if ans < MIN_INT // 10 + 1 or ans > MAX_INT // 10:
                return 0
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10

            x = (x-digit) // 10
            ans = ans * 10 + digit
        return ans

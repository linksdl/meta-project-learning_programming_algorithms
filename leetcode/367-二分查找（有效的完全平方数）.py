#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/11/3 10:47 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode_python
# @File        : 367-二分查找（有效的完全平方数）.py


'''
367. 有效的完全平方数 easy

给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/11 11:52 上午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 双指针-344（反转字符串）simple.py

'''
344-反转字符串
https://leetcode-cn.com/problems/reverse-string
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
'''


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1

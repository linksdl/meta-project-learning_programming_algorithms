#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/12 1:02 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 双指针-557（反转字符串中的单词III）simple.py

'''
557. 反转字符串中的单词 III
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
给定一个字符串，你需要反转字符串中每个单词的字符顺序，
同时仍保留空格和单词的初始顺序。
示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
'''


class Solution:
    def reverseWords(self, s):
        new_s = ' '.join([w[::-1] for w in s.split(' ')])
        return new_s

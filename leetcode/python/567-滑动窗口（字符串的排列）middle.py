#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/12 4:19 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 567-滑动窗口（字符串的排列）middle.py

'''
567. 字符串的排列
https://leetcode-cn.com/problems/permutation-in-string/
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，s1 的排列之一是 s2 的 子串 。

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        cnt = [0] * 26
        ascii_a = ord('a')
        for i in range(0, n):
            cnt[ord(s1[i]) - ascii_a]  += 1
            cnt[ord(s2[i]) - ascii_a]  -= 1

        for i in range(n, m):
            if self.isEqual(cnt):
                return True
            cnt[ord(s2[i-n]) - ascii_a] += 1
            cnt[ord(s2[i]) - ascii_a] -= 1

        return self.isEqual(cnt)


    def isEqual(self, cnt):
        return not any(cnt)

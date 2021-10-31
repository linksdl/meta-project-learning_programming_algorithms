#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/10/31 5:15 下午
# @Author      : linksdl
# @ProjectName : leetcode
# @File        : 575-贪心（分糖果）.py

'''
575. 分糖果
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。
返回妹妹可以获得的最大糖果的种类数。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-candies
'''

class Solution:
    def distributeCandies(self, candyType):
        m = len(set(candyType))
        n = len(candyType)

        return min(m, n//2)


#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/6 4:24 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 278-二分查找（第一个错误的八版本）simple.py

'''
278. 第一个错误的版本
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
'''

class Solution:
    def firstBadVersion(self, n):
        '''
        :param n:
        :return:
        '''
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left



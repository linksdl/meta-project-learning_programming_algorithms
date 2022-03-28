"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/29 00:13
@File        : number_color.py
"""

# # 数字涂色
# 【编程 | 100分】数字涂色
# 题目描述
#
# 疫情过后，希望小学终于又重新开学了，三年二班开学第一天的任务是将后面的黑板报重新制作。
#
# 黑板上已经写上了N个正整数，同学们需要给这每个数分别上一种颜色。
#
# 为了让黑板报既美观又有学习意义，老师要求同种颜色的所有数都可以被这种颜色中最小的那个数整除。
#
# 现在请你帮帮小朋友们，算算最少需要多少种颜色才能给这N个数进行上色。
#
# 输入描述:
# 第一行有一个正整数N，其中1≤N≤100。
# 第二行有N个int型数(保证输入数据在[1,100]范围中)，表示黑板上各个正整数的值。
# 输出描述:
# 输出只有一个整数，为最少需要的颜色种数。
# 示例1
# 输入
# 3
# 2 4 6
# 输出

# 1
# 说明
# 所有数都能被2整除。
#
# 示例2
# 输入
# 4
# 2 3 4 9
# 输出
# 2
# 说明
#
# 2与4涂一种颜色，4能被2整除；3与9涂另一种颜色，9能被3整除。
# 不能4个数涂同一个颜色，因为3与9不能被2整除。
# 所以最少的颜色是两种。

aa = [] # 获取 100 以内的质数。
i = 2
for i in range(2,100):
   j = 2
   for j in range(2,i):
      if i%j==0:
         break
   else:
      aa.append(i)


def colorNumber(n, nums):
    """
    数字涂色
    :param n:
    :param nums:
    """

    min_color = 0
    if n == 1:
        min_color = 1

    new_nums = nums
    cc = [1] * n
    if n >= 2:
        for a in aa:
            # print(new_nums)
            for i in range(n):
                if new_nums[i] % a == 0 and new_nums[i] != 0:
                    new_nums[i] = 0
                    cc[i] = a

    # print(cc)
    c = set(cc)
    min_color = len(c)
    if 1 in new_nums and 1 not in c:
        min_color += 1

    print(min_color)


colorNumber(22, [1,11,22,2,31,42,54,11,12,34,35,37,22,24,12,53,34,12,25,67,87,98])
colorNumber(9,  [1, 2,3,4,9,15, 25,33,67,99])
colorNumber(4,  [2,3,4,9])
colorNumber(3,  [2,4,6])
colorNumber(2,  [1,2])
colorNumber(1,  [2])
colorNumber(1,  [1])
colorNumber(2,  [1,3])


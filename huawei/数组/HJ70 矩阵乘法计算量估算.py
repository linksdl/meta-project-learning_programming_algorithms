"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 13:21
@File        : HJ70 矩阵乘法计算量估算.py
"""


# HJ70 矩阵乘法计算量估算

# 描述
# 矩阵乘法的运算量与矩阵乘法的顺序强相关。
# 例如：
#
# A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵
#
# 计算A*B*C有两种顺序：((AB)C)或者(A(BC))，前者需要计算15000次乘法，后者只需要3500次。
#
# 编写程序计算不同的计算顺序需要进行的乘法次数。
#
# 数据范围：矩阵个数：1\le n\le 15 \1≤n≤15 ，行列数：1\le row_i,col_i\le 100\1≤row
# i
# ​
#  ,col
# i
# ​
#  ≤100 ，保证给出的字符串表示的计算顺序唯一。
# 进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)
#
# 输入描述：
# 输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则
# 计算的法则为一个字符串，仅由左右括号和大写字母（'A'~'Z'）组成，保证括号是匹配的且输入合法！
#
# 输出描述：
# 输出需要进行的乘法次数

def calu(c1, c2):
    n = c2[1] * c2[0] * c1[1]
    temp = [c2[0], c1[1]]
    return n, temp


def computeNumberofMulti(n, matrix, s):
    """
    输入描述：
    输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则
    计算的法则为一个字符串，仅由左右括号和大写字母（'A'~'Z'）组成，保证括号是匹配的且输入合法！
    输出描述：
    输出需要进行的乘法次数
    :param n:
    :param matrix:
    :param s:
    :return:
    """

    # c = 'A'
    # alpha = {}
    # i = 0
    # for c in range(ord(c), ord(c) + len(matrix)):
    #     alpha[chr(c)] = matrix[i]
    #     i += 1
    # # print(alpha)

    # 双栈操作
    # chars = []  # 括号
    mats = []  # 矩阵值
    total = 0
    for ss in s:
        if ss.isalpha():
            mats.append(matrix[ord(ss) - 65])
        elif ss == ')' and len(mats) >= 2:
            num, temp = calu(mats.pop(), mats.pop())
            total += num
            mats.append(temp)

        print(mats, '=====', total)
        # print(chars, mats, total)

    print(total)


computeNumberofMulti(3, [[50, 10], [10, 20], [20, 5]], '(A(BC))')

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 13:36
@File        : 栈的基本操作及其应用.py
"""


def match1(s):  # 判断给定的括号串 s 是否括号匹配 (法一)

    n = len(s)

    # 栈

    stack = []

    # 遍历括号串

    for i in range(n):

        # 当前字符为左括号, 将其入栈

        if s[i] == "(":

            stack.append(s[i])

        # 当前字符为右括号

        else:

            # 栈为空, 说明没有左括号与当前的右括号匹配, 括号匹配失败

            if not stack:
                return False

            # 否则, 栈顶元素出栈 (与当前的右括号匹配)

            stack.pop()

    # 遍历结束, 且栈为空, 才说明括号匹配成功

    return not stack


def match2(s):  # 判断给定的括号串 s 是否括号匹配 (法二)

    n = len(s)

    # 平衡因子, 记录括号匹配过程中的 (左括号数量 - 右括号数量)

    bal = 0

    for i in range(n):

        if s[i] == "(":

            bal += 1

        else:

            bal -= 1

        if bal < 0:
            return False

    return bal == 0

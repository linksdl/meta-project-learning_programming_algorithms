"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 13:45
@File        : 20. 有效的括号.py
"""


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 1:
            return False

        myStack = []
        n = len(s)

        for i in range(n):
            s1 = s[i]
            # print(s1)
            if s1 in '([{':
                myStack.append(s[i])

            else:
                if not myStack:
                    return False
                s2 = myStack.pop()
                if s1 == ')' and s2 != '(':
                    return False
                elif s1 == ']' and s2 != '[':
                    return False
                elif s1 == '}' and s2 != '{':
                    return False
            # print(myStack)

        return not myStack

s = '()'
f = isValid('()')
print(f)

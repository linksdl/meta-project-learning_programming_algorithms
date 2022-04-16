"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/28 20:38
@File        : HJ54 表达式求值.py
"""


# HJ54 表达式求值

def applyOp(v1, v2, op):
    v1 = int(v1)
    v2 = int(v2)
    if op == '+': return v1 + v2
    if op == '-': return v1 - v2
    if op == '*': return v1 * v2
    if op == '/': return v1 // v2

def opr_fn(str):
    stack = []
    oprs = []
    nums  = []
    prior = {'+':1, '-':1, '*':2, "//":2}
    cc = []
    for s in str:
        if s.isdigit():
            cc.append(s)
        else:
            cc.append(s)
        if len(cc) == 3:
            n = applyOp(cc[0], cc[2], cc[1])
            cc.append(n)
            print(n)


opr_fn('9+4')


str = input()

print(eval(str))

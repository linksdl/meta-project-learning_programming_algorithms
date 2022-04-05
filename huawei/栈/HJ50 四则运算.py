"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 09:58
@File        : HJ50 四则运算.py
"""


# HJ50 四则运算

# 描述
# 输入一个表达式（用字符串表示），求这个表达式的值。
# 保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。
#
# 数据范围：表达式计算结果和过程中满足 |val| \le 1000 \∣val∣≤1000  ，字符串长度满足 1 \le n \le 1000 \1≤n≤1000
#
# 输入描述：
# 输入一个算术表达式
#
# 输出描述：
# 得到计算结果

def oper_fn(val1, val2, oper):
    """
    数学运算
    :param val1:
    :param val2:
    :param oper:
    :return:
    """
    # print(val1, val2, oper)
    if oper == '+':
        return val2 + val1
    elif oper == '-':
        return val2 - val1
    elif oper == '*':
        return val2 * val1
    elif oper == '/':
        return val2 // val1


def compOper(char1, char2):
    """
    比较运算符优先级
    :param char1:
    :param char2:
    :return:
    """
    # print(char1,'========', char2)
    if char1 == '(' or char1 == '[' or char1 == '{':
        return False
    elif (char1 == '+' or char1 == '-') and (char2 == '*' or char2 == '/'):
        return False

    return True


def main_fn(s):
    """
    输入描述：
    输入一个算术表达式

    输出描述：
    得到计算结果
    :param s:
    :return:
    """
    opers = '+-*/)]}'
    nums = []
    oprs = ['(']
    s += ')'
    flag = False
    i = 0
    while i < len(s):
        ss = s[i]
        if ss == '(' or ss == '[' or ss == '{':
            oprs.append('(')
            i += 1

        elif ss == ')' or ss == ']' or ss == '}':
            while oprs[-1] != '(':  # 弹出开始计算直到遇到左括号
                res = oper_fn(nums.pop(), nums.pop(), oprs.pop())
                nums.append(res)
            oprs.pop()  # 弹出左括号
            i += 1

        elif flag:  # 运算符
            while compOper(oprs[-1], ss):
                res = oper_fn(nums.pop(), nums.pop(), oprs.pop())
                nums.append(res)
            oprs.append(ss)  # 需要将现阶段加入栈中等待运算
            flag = False
            i += 1
        else:  # 数字
            count = 0
            if s[i] == '-' or s[i] == '+': # 正负号
                count += 1

            while s[i+count].isdigit():
                count += 1

            t = s[i:i+count]
            # print(t)
            nums.append(int(t))
            # i -= 1
            flag = True # 数字结束，下一次flag为true就是运算符了
            i += count

        # print(oprs, nums)
        # print(nums[-1])

    print(nums[-1])

main_fn('3+2*{1+2*[-4/(8-6)+7]}')


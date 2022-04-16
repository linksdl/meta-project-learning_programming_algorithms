"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 15:54
@File        : 子串匹配.py
"""

# https://www.nowcoder.com/subject/index/17330dc434cb49ca866bdb1d5bc92383

# 给定两个字符串A、B 两个字符串长度相等，A字符串中有一段连续字符，在B字符串中也有一段长度相同位置相同的连续字符串
# 要求| [A [ i ] -B [ i ] ] | 小于等于给定数值V 。
# 输入要求：
# 第一行 字符串A
# 第二行 字符串B
# 第三行 给定数字 V
# 1
# 2
# 3
# xxcdefg
# cdefghi
# 5
# 输出 满足 | [A [ i ] -B [ i ] ] | 小于等于给定数值V 的A中连续字符串的长度
# 1
# 2
# 解释 有对应的。cd->ef,de->fg,ef->gh,fg->hi
# 所以输出2


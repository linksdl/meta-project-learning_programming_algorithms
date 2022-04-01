"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 15:17
@File        : HJ20-密码验证合格程序.py
"""

# HJ20 密码验证合格程序

def checkPassword(s):
    """
    密码要求:
    1.长度超过8位
    2.包括大小写字母.数字.其它符号,以上四种至少三种
    3.不能有长度大于2的不含公共元素的子串重复 （注：其他符号不含空格或换行）
    :param s:
    :return:
    """

    flag = True
    checks = [0,0,0,0]
    # 判断密码长度
    if len(s) <= 8:
        return False

    checks = [0, 0, 0, 0]
    for c in s:
        if c.isupper():  # 大写字母
            checks[0] = 1
        elif c.islower():       # 小写字母
            checks[1] = 1
        elif c.isdigit():       # 数字
            checks[2] = 1
        else:                   # 其他字符
            checks[3] = 1

    if sum(checks) < 3:
        return False

    for i in range(len(s) -2):
        if s[i:i+3] in s[i+3:]:
            return False

    return True







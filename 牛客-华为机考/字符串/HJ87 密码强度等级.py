"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/30 21:00
@File        : HJ87 密码强度等级.py
"""

# HJ87 密码强度等级

# 描述
# 密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。


def strongPassword(s):
    """
    HJ87 密码强度等级
    :param s:
    :return:
    """
    score = 0
    if s is None or s== '':
        score = 0

    scores = []
    l = len(s)
    # 一、密码长度:
    if l <= 4:
        scores.append(5)
    elif 5 <= l <=7:
        scores.append(10)
    elif l >= 8:
        scores.append(25)

    # 二、字母:
    # 三、数字:
    # 四、符号:
    chars = '!"#$%&\'()*+,-./:;<=>?@:;<=>?@{|}~'
    count_digit = 0
    count_char = 0
    count_alpha = 0
    is_upper_alpha = False
    is_lower_alpha = False
    for c in s:
        if c.isdigit():
            count_digit += 1
        if c.isalpha():
            count_alpha += 1
            if c.isupper():
                is_upper_alpha = True
            if c.islower():
                is_lower_alpha = True
        if c in chars:
            count_char += 1

    # 二、字母:
    if count_alpha > 0:
        if is_upper_alpha and is_lower_alpha:
            scores.append(20)
        else:
            scores.append(10)
    else:
        scores.append(0)

    # 三、数字:
    if count_digit == 1:
        scores.append(10)
    elif count_digit > 1:
        scores.append(20)
    else:
        scores.append(0)

    # 四、符号:
    if count_char == 1:
        scores.append(10)
    elif count_char > 1:
        scores.append(25)
    else:
        scores.append(0)

    # 五、奖励（只能选符合最多的那一种奖励）:
    if count_digit > 0 and count_alpha > 0:
        if count_char == 0:
            scores.append(2)
        else:
            print(count_char)
            if is_upper_alpha and is_lower_alpha:
                # print('----')
                scores.append(5)
            else:
                scores.append(3)
    else:
        scores.append(0)

    print(scores)
    score = sum(scores)
    if score < 25:
        print('VERY_WEAK')
    elif 25 <= score < 50:
        print('WEAK')
    elif 50 <= score < 60:
        print('AVERAGE')
    elif 60 <= score < 70:
        print('STRONG')
    elif 70 <= score < 80:
        print('VERY_STRONG')
    elif 80 <= score < 90:
        print('SECURE')
    else:
        print('VERY_SECURE')


strongPassword('38$@NoNoN')
strongPassword('Jl)M:+')
strongPassword('Aa1(')
strongPassword('Aa12(')


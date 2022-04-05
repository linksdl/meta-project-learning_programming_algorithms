"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/29 20:56
@File        : HJ90 合法IP.py
"""


# HJ90 合法IP

def fn_ip(s):
    """
    IPV4地址可以用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此正号不需要出现），
    如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。
    现在需要你用程序来判断IP是否合法。
    数据范围：数据组数：1\le t\le 18\1≤t≤18
    进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)
    :param str:
    :return:
    """
    s = s.strip()
    strs = s.split('.')

    if len(strs) == 4:
        flags = ['YES'] * 4
        ips = [str(p) for p in range(0,256)]
        for i in range(len(strs)):
            n = strs[i]
            if n is None or n == '':
                flags[i] = 'NO'
                break
            else:
                if n in ips:
                    flags[i] = 'YES'
                else:
                    flags[i] = 'NO'
                    break
        if 'NO' in flags:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')


fn_ip('255.255.255.1000')
fn_ip('.1.3.8')
fn_ip('01.2.3.8')

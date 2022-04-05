"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/2 10:23
@File        : HJ33 整数与IP地址间的转换.py
"""


# HJ33 整数与IP地址间的转换

#
# 原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
# 一个长整数。
# 举例：一个ip地址为10.0.3.193
# 每段数字             相对应的二进制数
# 10                   00001010
# 0                    00000000
# 3                    00000011
# 193                  11000001
#
# 组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
#
# 数据范围：保证输入的是合法的 IP 序列

def covertIP(ip, num):
    """
    HJ33 整数与IP地址间的转换
    :param ip:
    :param num:
    """

    ips = ip.split('.')

    ip_int = 0
    ip_str = ''
    for p in ips:
        c = str(bin(int(p)))
        c = c[2:len(c)]
        if len(c) < 8:
            c = '0'*(8-len(c)) + c
        ip_str += c
    # print(ip_str)
    # 00001010000000000000001111000001
    # 00001010000000000000001111000001

    for i in range(len(ip_str)-1, -1, -1):
        ip_int += int(ip_str[i]) * 2 ** (32-i-1)

    print(ip_int)

    # print(bin(num))
    cc = str(bin(num))[2:]
    cc = '0'*(32-len(cc)) + cc
    # 00001010000000110000001111000001
    # print(cc)
    o_ips = [0] * 4
    for i in range(0, len(cc), 8):
        # print(i)
        ip_ = cc[i:(i+8)]
        # print(ip_)
        for j in range(8):
            o_ips[i//8] += int(ip_[j]) * 2 ** (8-j-1)

    print('.'.join([str(x) for x in o_ips]))



covertIP('10.0.3.193', 167969729)

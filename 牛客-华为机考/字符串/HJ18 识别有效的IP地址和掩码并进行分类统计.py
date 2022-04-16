"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:41
@File        : HJ18 识别有效的IP地址和掩码并进行分类统计.py
"""


# HJ18 识别有效的IP地址和掩码并进行分类统计


import sys

res = [0, 0, 0, 0, 0, 0, 0]


def puip(ip):
    if 1 <= ip[0] <= 126:  # A类地址判断条件
        res[0] += 1
    elif 128 <= ip[0] <= 191:  # B类地址判断条件
        res[1] += 1
    elif 192 <= ip[0] <= 223:  # C类地址判断条件
        res[2] += 1
    elif 224 <= ip[0] <= 239:  # D类地址判断条件
        res[3] += 1
    elif 240 <= ip[0] <= 255:  # E类地址判断条件
        res[4] += 1
    return


def prip(ip):  # 私有IP地址判断条件
    if (ip[0] == 10) or (ip[0] == 172 and 16 <= ip[1] <= 32) or (ip[0] == 192 and ip[1] == 168):
        res[6] += 1
    return


def ym(msk):  # 判断掩码合法性
    val = (msk[0] << 24) + (msk[1] << 16) + (msk[2] << 8) + msk[3]  # 转换成32位
    if val == 0:  # 排除全0的情况
        return False
    if (val + 1) == (1 << 32):  # 排除全1的情况
        return False
    flag = 0
    while (val):
        digit = val & 1  # 逐位判断
        if digit == 1:
            flag = 1
        if flag == 1 and digit == 0:  # flag=1表示已经不允许再出现0
            return False
        val >>= 1
    return True


def judge(line):
    ip, msk = line.strip().split('~')
    ips = [int(x) for x in filter(None, ip.split('.'))]  # 获得表示IP的列表，理论上应该包含四个元素
    msks = [int(x) for x in filter(None, msk.split('.'))]  # 获得表示掩码的列表，理论上应该包含四个元素
    if ips[0] == 0 or ips[0] == 127:  # 排除非法IP不计数
        return
    if len(ips) < 4 or len(msks) < 4:  # 判断错误掩码或错误IP
        res[5] += 1
        return
    if ym(msks) == True:  # 通过掩码判断的可以进行IP判断
        puip(ips)
        prip(ips)
    else:
        res[5] += 1
    return


for line in sys.stdin:
    judge(line)
# judge("192.168.0.2~255.255.255.0")

res = [str(x) for x in res]
print(" ".join(res))

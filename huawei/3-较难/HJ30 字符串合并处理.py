"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:35
@File        : HJ30 字符串合并处理.py
"""



import re

# 构造函数加密字符，如果是[0-9A-Fa-f]则按规则返回加密值，否则返回原始值
def encrypt(x):
    if re.search(r'[0-9A-Fa-f]', x):
        return hex(int(bin(int(x, 16))[2:].rjust(4, '0')[::-1], 2))[2:].upper()
        """
        1. int(x, 16) - 将字符x转成16进制
        2. bin(int(x, 16))[2:].rjust(4,'0')[::-1] - 继续将十六进制转成二进制，并去除二进制开头"0b"，如果二进制长度小于4，则在前面补0至四位,然后再倒序。
        比如bin(int('7', 16))输出0b111,[2:]去除0b后为111，rjust(4,'0')左侧补0则变为0111，[::-1]倒序后变为二进制的1110
        3. hex(int(i,2)[2:].upper() - 其中i表示注释2的内容。这一步是将上一步获取的二进制转成十六进制，并去除开头的"0x",最后再将其转成大写。
        """
    else:
        return x

while True:
    try:
        a = list(input().replace(" ", "")) # 去除输入中的空格，并将输入的字符处理成列表
        a[::2] = sorted(a[::2])  # 奇数位置从小到大排序
        a[1::2] = sorted(a[1::2])  # 偶数位置从小到大排序
        res = ""
        for i in a:
            res += encrypt(i) # 调用加密函数，遍历输出结果
        print(res)
    except:
        break

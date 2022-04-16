"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 17:18
@File        : 报文解压缩.py
"""


def unzip(str):

    mystack_char = []
    mystack_num  = []
    ans = ''
    for s in str:
        if s == '[':
            mystack_char.append(s)

        elif s.isdigit():
            mystack_num.append(s)

        elif s.isalpha():
            mystack_char.append(s)

        elif s == ']':
            cc = []
            while mystack_char[-1] != '[':
                cc.append(mystack_char.pop())
            n = int(mystack_num.pop())
            ccc = ''.join(cc[::-1])
            # print(ccc)
            ccc *= n

            mystack_char.pop() # 弹出 '['
            mystack_char.append(ccc)
            print(ccc)


s = '3[m2[c]]'
s = '3[k]2[mn]'
unzip(s)

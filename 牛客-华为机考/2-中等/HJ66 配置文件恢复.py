"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/2 12:19
@File        : HJ66 配置文件恢复.py
"""


while True:
    try:
        n=input().strip().split()
        key=["reset","reset board","board add","board delete","reboot backplane","backplane abort"]
        value=["reset what","board fault","where to add","no board at all","impossible","install first"]
        if len(n) < 1 or len(n) > 2:
            print("unknown command")
        elif len(n) == 1:
            if n[0] == key[0][0:len(n[0])]:
                print(value[0])
            else:
                print("unknown command")
        else:
            b=[]
            for i in key[1:]:
                a=i.split()
                if n[0] == a[0][0:len(n[0])] and n[1] == a[1][0:len(n[1])]:
                    b.append(key.index(i))
            if len(b) != 1:
                print("unknown command")
            else:
                print(value[b[0]])
    except:
        break

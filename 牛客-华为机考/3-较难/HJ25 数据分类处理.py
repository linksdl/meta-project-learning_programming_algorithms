"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:51
@File        : HJ25 数据分类处理.py
"""


while True:
    try:
        a=input().split()[1:]
        b=map(str,sorted(map(int,set(input().split()[1:]))))
        totalNum=0
        res=""
        for num in b:
            singleRes,count="",0
            for i,v in enumerate(a):
                if num in v:
                    singleRes+=str(i)+" "+v+" "
                    totalNum+=2
                    count+=1
            if count:
                singleRes=num+" "+str(count)+" "+singleRes
                totalNum+=2
            res+=singleRes
        print((str(totalNum)+" "+res).rstrip())

    except:
        break

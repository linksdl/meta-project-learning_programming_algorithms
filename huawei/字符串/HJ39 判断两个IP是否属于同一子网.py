"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:44
@File        : HJ39 判断两个IP是否属于同一子网.py
"""


while True:
    try:
        x=input().split(".")
        y=input().split(".")
        z=input().split(".")
        m=[]
        n=[]
        for i in range (len(x)):
            x[i]=int(x[i])
            y[i] = int(y[i])
            z[i] = int(z[i])
        if x[0]!=255 or x[3]!=0 or max(x+y+z)>255 or min(x+y+z)<0:
            print("1")
        else:
            for i in range (len(x)):
                x[i]=bin(x[i]).replace("0b","")
                y[i] = bin(y[i]).replace("0b","")
                z[i] = bin(z[i]).replace("0b","")
                m.append(int(x[i],2)&int(y[i],2))
                #m[i]=m[i].replace("0b","")
                n.append(int(x[i],2)&int(z[i],2))
                #n[i] = n[i].replace("0b", "")
            if m==n:
                print("0")
            else:
                print("2")
    except:
        break

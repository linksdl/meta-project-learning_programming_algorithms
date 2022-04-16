"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 12:32
@File        : HJ17 坐标移动.py
"""


# HJ17 坐标移动
# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
# 从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
#

def cordinate(s):
    """
    HJ17 坐标移动
    :param s:
    :return:
    """

    ss = s.split(';')
    print(ss)
    x, y = 0, 0
    for z in ss:
        if z is not None:
            if len(z) >= 2 and z[0] in ['A', 'D', 'S', 'W']:
                if z[1:len(z)].isdigit():
                    direction = z[0]
                    step = int(z[1:len(z)])
                    print(direction, step)
                    if direction == 'A':
                        x -= step
                    elif direction == 'D':
                        x += step
                    elif direction == 'W':
                        y += step
                    elif direction == 'S':
                        y -= step

    print(str(x)+','+str(y))





cordinate('A10;S20;W10;D30;X;A1A;B10A11;;A10;')
cordinate('ABC;AKL;DA1;')

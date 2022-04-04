"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/4 08:55
@File        : HJ64 MP3光标位置.py
"""


# 描述
# MP3 Player因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，用户要通过上下键才能浏览所有的歌曲。为了简化处理，假设每屏只能显示4首歌曲，光标初始的位置为第1首歌。
# 现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：
#
# 歌曲总数<=4的时候，不需要翻页，只是挪动光标位置。
#
# 光标在第一首歌曲上时，按Up键光标挪到最后一首歌曲；光标在最后一首歌曲时，按Down键光标挪到第一首歌曲。


# 输入描述：
# 输入说明：
# 1 输入歌曲数量
# 2 输入命令 U或者D
#
# 输出描述：
# 输出说明
# 1 输出当前列表
# 2 输出当前选中歌曲


def moveTarget(n, c):
    """
    输入描述：
    输入说明：
    1 输入歌曲数量
    2 输入命令 U或者D

    输出描述：
    输出说明
    1 输出当前列表
    2 输出当前选中歌曲
        :param n:
    :param c:
    :return:
    """
    page_size = 4
    lst = []
    if n <= 4:
        point = 1
        for m in c:
            if m == 'U':
                if point == 1:
                    point = n
                else:
                    point -= 1
            if m == 'D':
                if point == n:
                    point = 1
                else:
                    point += 1
        lst = ' '.join([str(i) for i in range(1, n+1)])
        print(lst)
        print(point)
    else:
        point = 1
        page_point = 1
        for m in c:
            if m == 'U':
                if point == 1:
                    point = n
                    page_point = n - (page_size-1)
                elif point == page_point:
                    point -= 1
                    page_point -= 1
                else:
                    point -= 1
            if m == 'D':
                if point == n:
                    point = 1
                    page_point = 1
                elif point == page_point + (page_size-1):
                    point += 1
                    page_point += 1
                else:
                    point += 1
            # print(point, page_point)
        lst = ' '.join([str(i) for i in range(page_point, page_point+page_size)])
        print(lst)
        print(point)


# moveTarget(10, 'UUUU')
moveTarget(83, 'UUDUDDDDUDUUDDDDUDD')

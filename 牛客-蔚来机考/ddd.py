"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/10 19:47
@File        : OJ在线编程常见输入输出练习.py
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param point float浮点型一维数组 The point in the format of [x,y]
# @param triangle float浮点型二维数组 The triangle in the format of [[x1, y1], [x2, y2], [x3, y3]​].
# @return float浮点型
#

def calculateDistance(point, triangle):
    # write code here
    x = point[0]
    y = point[1]
    x_r = []
    y_r = []
    for i in range(len(triangle)):
        p = triangle[i]
        x_r.append(p[0])
        y_r.append(p[1])
    x_r.sort()
    y_r.sort()
    # print(x, y)
    if x_r[0] <= x <= x_r[2] or y_r[0] <= y <= y_r[2]:

        print(0)


    def cal_dis(c1, c2):
        return ( (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 )

    point1 = triangle[0]
    point2 = triangle[1]
    point3 = triangle[2]

    d1 = cal_dis(point, point1)
    d2 = cal_dis(point, point2)
    d3 = cal_dis(point, point3)

    distance = [d1, d2, d3]
    distance.sort()

    p = []
    if d1 == distance[0]:
        p.append(point1)
    elif d2 == distance[0]:
        p.append(point2)
    elif d3 == distance[0]:
        p.append(point3)

    print(distance)
    if d1 == distance[1]:
        p.append(point1)
    elif d3 == distance[1]:
        p.append(point3)
    elif d2 == distance[1]:
        p.append(point2)


    print(p)
    d = cal_dis(p[0], p[1])
    print(d)

    print(distance)

point = [0,-2]
triangle = [[0,1],[1,-1],[-1,-1]]

# point = [0,0]
# triangle = [[0,1],[1,-1],[-1,-1]]
calculateDistance(point, triangle)



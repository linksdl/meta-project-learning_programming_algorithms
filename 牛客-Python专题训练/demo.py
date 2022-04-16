#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/11/1 10:32 上午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode_python
# @File        : demo.py



a = [1, 2]
b = a

print(b)

c = b

if a == b:
    print("a == b")

if a is c:
    print('a is c')
else:
    print('a is not c')

if b is c:
    print('c is b')

# [[10], [20], [], [], [], 30]

# list[1] = [20]
#
# [[10,20],[], 30]

list = [[]]* 5

list[0].append(10)
print(list)

list[1] = [20]
print(list)

list[2].append(30)
print(list)

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/12 10:25
@File        : dmeo.py
"""


import random
def foo(n):
    random.seed()
    c1 = 0
    c2 = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        r1 = x * x + y * y
        r2 = (1 - x) * (1 - x) + (1 - y) * (1 - y)
        if r1 <= 1 and r2 <= 1:
           c1 += 1
        else:
           c2 += 1

    print(c1 / c2)

# foo(150)
a=[1, 2, 3, 4, 5]
print(map(lambda x: x + 3, a[1::3]))
sums = sum(map(lambda x: x + 3, a[1::3]))
print(sums)

a = [['1','2'] for i in range(2)]

b = [['1','2']]*2

a[0][1] = '3'

b[0][0] = '4'

print(a,b)

for i in range(5):
    if i == 2:
        pass
    print(i)


a = range(100)
print(a[-3])
print(a[2:13])
print(a[::3])
print(a[2-3])

def fun(a,*,b):

    print(b)

# fun(1,2,3,4)

a = (1, 2, 3)
print(a[1:-1])


num = 1

strs = 'I like 全部 and java'
print(strs.replace('I', 'Your'))
print(strs.replace('a', '*', 2))

strs = 'I like 全部 and java'
one = strs.find('n')
print(one)
two = strs.rfind('n')
print(two)

strs = ['a', 'ab', 'abc', '全部']
y = filter(lambda s: len(s) > 2, strs)
tmp = list(map(lambda s: s.upper(), y))
print(tmp)

func = lambda x:x%2
result = filter(func, [1, 2, 3, 4, 5])
print(list(result))

one = (1, 2, 3)
two = ('a', 'b')
print(one+two)

lists = [1, 1, 2, 3, 4, 5, 6]
lists.remove(1)
lists.append(7)
print(lists)


dividend = 1

lists = [1, 2, 3, 4, 5, 6]
print(lists[6:])

list = ['1', '2', '3', '4', '5']
print(list[10:])

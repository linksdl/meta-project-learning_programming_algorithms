"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 15:01
@File        : HJ88 扑克牌大小.py
"""


dic = {
    '3' : 1, '4' : 2, '5' : 3, '6' : 4, '7' : 5, '8': 6,
    '9' : 7, '10' : 8, 'J' : 9, 'Q' : 10, 'K' : 11, 'A' : 12,
    '2' : 13, 'joker' : 14, 'JOKER' : 15
}

def isboom(lst):
    if len(lst) == 4 and len(set(lst)) == 1:
        return True
    return False

while True:
    try:
        s1, s2 = input().split('-')
        lst1, lst2 = s1.split(), s2.split()
        L1, L2 = len(lst1), len(lst2)
        if L1 == L2:
            if dic[lst1[0]] > dic[lst2[0]]:
                print(s1)
            else:
                print(s2)
        else:
            if 'joker JOKER' in (s1, s2):
                print('joker JOKER')
            elif isboom(lst1):
                print(s1)
            elif isboom(lst2):
                print(s2)
            else:
                print('ERROR')
    except:
        break

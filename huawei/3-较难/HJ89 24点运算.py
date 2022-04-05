"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:57
@File        : HJ89 24点运算.py
"""

d = {'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
    '10':10, 'J':11, 'Q':12, 'K':13, 'A':1, '2':2}
def f(nums, target):
    if len(nums) == 1:
        if d[nums[0]] == target:
            res.append(nums[0])
            return True
        else:
            return False
    for i in range(len(nums)):
        a = nums[i]
        b = nums[:i] + nums[i+1:]
        if f(b, target + d[a]):
            res.append('-' + a)
            return True
        elif f(b, target - d[a]):
            res.append('+' + a)
            return True
        elif f(b, target * d[a]):
            res.append('/' + a)
            return True
        elif target % d[a] == 0 and f(b, target // d[a]):
            res.append('*' + a)
            return True
    return False
while True:
    try:
        nums = input().strip()
        if 'joker' in nums or 'JOKER' in nums:
            print('ERROR')
        else:
            nums = nums.split()
            res = []
            if f(nums, 24):
                print(''.join(res))
            else:
                print('NONE')
    except:
        break


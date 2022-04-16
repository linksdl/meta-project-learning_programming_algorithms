"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 15:24
@File        : HJ28 素数伴侣.py
"""


def get_primenum(s):
    if s < 4:
        return True
    # 通过从2到它的平方根之间没有可除尽的数来判断这个数是否为素数。原理：一个数与另一个数能除尽则也能除尽这个数的2倍数。若直接判断从2到这个数之间的数则会耗费大量的时间来计算导致超时。
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            return False
    return True


def find_even(evens, previous_select, final_select, odd):
    for i, even in enumerate(evens):
        if get_primenum(even + odd) and previous_select[i] == 0:
            previous_select[i] = 1
            # 判断第i位偶数是否被匹配或者它的匹配奇数是否有其他选择，如果有其他选择，则当前的奇数匹配第i位偶数
            if final_select[i] == 0 or find_even(evens, previous_select, final_select, final_select[i]):
                final_select[i] = odd
                return True
    return False


while True:
    try:
        N = int(input())
        list0 = list(map(int, input().split(' ')))
        count0 = 0
        evens, odds = [], []
        for list1 in list0:
            if list1 % 2 == 0:
                evens.append(list1)
            else:
                odds.append(list1)
        final_select = [0] * len(evens)
        for odd in odds:
            previous_select = [0] * len(evens)
            if find_even(evens, previous_select, final_select, odd):
                count0 += 1
        print(count0)
    except:
        break

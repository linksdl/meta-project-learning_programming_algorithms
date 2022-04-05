"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 13:55
@File        : HJ29 字符串加解密.py
"""



def encodeAndDecodePassword(s1, s2):
    """
    HJ29 字符串加解密
    :param s1:
    :param s2:
    """

    # 加密
    out_s1 = ''
    for s in s1:
        if s.isalpha():
            if s == 'z':
                out_s1 += 'A'
            elif s == 'Z':
                out_s1 += 'a'
            elif s.islower():
                out_s1 += (chr(ord(s) + 1).upper())
            elif s.upper():
                out_s1 += (chr(ord(s) + 1)).lower()
        elif s.isdigit():
            out_s1 += str( (int(s)+1) % 10 )

    print(out_s1)

    # 解密
    out_s2 = ''
    for s in s2:
        if s.isalpha():
            if s == 'a':
                out_s2 += 'Z'
            elif s == 'A':
                out_s2 += 'z'
            elif s.islower():
                out_s2 += (chr(ord(s) - 1).upper())
            elif s.upper():
                out_s2 += (chr(ord(s) - 1)).lower()
        elif s.isdigit():
            out_s2 += str( (int(s)+9) % 10 )

    print(out_s2)


encodeAndDecodePassword('abcdefg', 'BCDEFGH')

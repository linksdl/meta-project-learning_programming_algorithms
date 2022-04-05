"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/1 15:42
@File        : HJ36 字符串加密.py
"""


# HJ36 字符串加密


def encodePassowrd(key, s):
    """
    # HJ36 字符串加密
    :param s:
    :return:
    """
    new_key = ''
    for k in key:
        if k not in new_key:
            new_key += k

    print(new_key)

    # 1 字母表
    list_c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

    new_s = ''
    new_s += new_key
    for c in list_c:
        if c not in new_key:
            new_s += c

    print(new_s)

    encode_s = ''
    for c in s:
        if c.isalpha() and c.islower():
            encode_s += new_s[list_c.index(c)]
        elif c.isalpha() and c.isupper():
            encode_s += (new_s[list_c.index(c.lower())]).upper()
        else:
            encode_s += c

    print(encode_s)






encodePassowrd('nihao', 'ni')

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/25 17:05
@File        : HJ102-.py
"""


# 描述
# 输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
# 数据范围：字符串长度满足 1 \le len(str) \le 1000 \1≤len(str)≤1000
#
# 输入描述：
# 一个只包含小写英文字母和数字的字符串。
#
# 输出描述：
# 一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。
# 输入：
# aaddccdc
#
# 输出：
# cda
# 说明：
# 样例里，c和d出现3次，a出现2次，但c的ASCII码比d小，所以先输出c，再输出d，最后输出a.


def sortStr(str):
    """
    一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。
    :param str:
    """
    count = {}
    ss = sorted(set(str))
    print(ss)
    for s in str:
        count[s] = count.get(s, 0) + 1

    for i in range(len(ss)-1):
        for j in range(len(ss)-i-1):
            if count[ss[j+1]] > count[ss[j]]:
                tmp = ss[j]
                ss[j] = ss[j+1]
                ss[j + 1] = tmp
    print(''.join(ss))
    return ss

print(sortStr('aaddccdc'))

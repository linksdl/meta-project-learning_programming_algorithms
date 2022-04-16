"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 21:56
@File        : 内存分配.py
"""


def aaa(line1, line2):
    ans = []
    if len(line1) < 1:
        for _ in range(0, len(line2)):
            ans.append('false')
    else:
        m_space = {}
        sizes = []
        mm_space = []
        for m in line1:
            mm = m.split(':')
            size = mm[0]
            n = int(mm[1])
            sizes.append(int(size))
            m_space[size] = m_space.get(n, 0) + n
            for i in range(n):
                mm_space.append(int(size))

        mm_space.sort()
        sizes.sort()

        remain = 0
        j = 0
        i = 0
        while i < len(line2) and j < len(mm_space):
            r_m = line2[i]
            size = mm_space[j]
            if remain > r_m:
                while remain > r_m:
                    ans.append('true')
                    remain = remain - r_m
                    i += 1
            else:
                while j < len(mm_space) - 1 and r_m > size:
                    j += 1

                if j < len(mm_space):
                    size = mm_space[j]
                    if size > r_m:
                        ans.append('true')
                        remain = size - r_m
                        i += 1
                    else:
                        j += 1

    for _ in range(i, len(line2)):
        ans.append('false')

    print(','.join(ans))


line1 = ['64:2', '128:1', '32:4', '1:128']
line2 = [50, 36, 64, 128, 127]
aaa(line1, line2)

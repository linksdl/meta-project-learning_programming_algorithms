"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 20:39
@File        : 好朋友.py
"""


def friends(n, nums):

    ans = []
    l = len(nums)
    if l == 1:
        ans = [0]
    elif l <= 2:
        if nums[0] < nums[1]:
            ans = [1, 0]
        else:
            ans = [0, 0]
    else:
        i = 0
        for i in range(l-2):
            # for j in range(i+1, l-1):
            j = i+1
            n = nums[i]
            while j < l and nums[j] <= n:
                j += 1
            if j < l-1:
                ans.append(j)
            else:
                ans.append(0)
            # continue
            #     if nums[j] > nums[i]:
            #         ans.append(j)
            #         break

        if nums[-2] < nums[-1]:
            ans.append(l-1)
        else:
            ans.append(0)
        ans.append(0)

    ss = [str(i) for i in ans]
    # print(ss)
    print(' '.join(ss))



n = 8
nums = [123, 124, 125, 121, 119, 122, 126, 123, 123, 124, 125, 121, 119, 122, 126, 123]
# 123 124 125 121 119 122 126 123 123 124 125 121 119 122 126 123
# nums = [123, 124]
# nums = [100, 95, 95]
# nums = [100]
# nums = [11]
friends(n, nums)

# 1 2 6 5 5 6 0 9 9
# 1 2 6 5 5 6 9 9 1 0 1 4 1 3 1 3 1 4
# 1 2 6 5 5 6 14 9 9 10 14 13 13 14 0 0

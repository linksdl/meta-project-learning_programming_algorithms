"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 15:16
@File        : 区间选择类问题.py
"""



import heapq

def minMeetingRooms(intervals):  # 最小会议室数量

    n = len(intervals)

    # 小根堆, 维护正在进行的会议的结束时间

    pq = []

    # 所求结果(最小会议室数量)

    res = 0

    # 按会议开始时间递增排序(优先安排开始时间早的会议)

    intervals = sorted(intervals, key=lambda k: k[0])

    # 遍历 n 个会议

    for i in range(n):

        # 记当前时间为第 i 个会议的开始时间

        # 在此之前结束的会议应从小根堆中移除

        while pq and pq[0] <= intervals[i][0]:

            heapq.heappop(pq)

        # 将第 i 个会议的结束时间加入小根堆

        heapq.heappush(pq, intervals[i][1])

        # 当前小根堆中的元素最大值, 即为最终结果

        res = max(res, len(pq))

    # 最终, res即为所求

    return res



def maxMeetings(intervals):  # 最大可参加会议数量

    n = len(intervals)

    # 按会议结束时间递增排序(保证当前会议之前存在结束时间 <= 当前会议开始时间的会议)

    intervals = sorted(intervals, key=lambda k: k[1])

    # last: 在当前会议之前选择的最后一个会议下标, res: 所求结果 (最大参加会议数量)

    last, res = 0, 1

    # 从下标为 1 的会议开始遍历

    for i in range(1, n):

        # 若之前参加的最后一个会议结束时间 <= 当前会议的开始时间

        # 则选择当前会议

        if intervals[last][1] <= intervals[i][0]:

            last = i

            res += 1

    # 最终, res即为所求

    return res

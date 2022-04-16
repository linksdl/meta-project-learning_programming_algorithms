"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 16:27
@File        : 2225. 找出输掉零场或一场比赛的玩家.py
"""


def findWinners(matches):
    matches.sort(key=lambda x: x[0])
    # print(matches)
    winner = set()
    loser = list()
    for num in matches:
        winner.add(num[0])
        loser.append(num[1])
    # print(winner)
    # print(loser)

    answer = []
    ws = []
    for w in winner:
        if w not in loser:
            ws.append(w)
    answer.append(ws)

    loser.sort()

    # print(loser)

    loser_r = {}
    for i in loser:
        loser_r[i] = loser_r.get(i, 0) + 1

    ans_loser = []
    for v in loser_r:
       if loser_r[v] == 1:
           ans_loser.append(v)

    answer.append(ans_loser)

    print(answer)








matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
findWinners(matches)

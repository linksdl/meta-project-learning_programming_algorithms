"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/31 15:25
@File        : HJ94-记票统计.py
"""

# 描述
# 请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，请统计每个候选人得票的数量以及不合法的票数。
# （注：不合法的投票指的是投票的名字不存在n个候选人的名字中！！）
#
# 数据范围：每组输入中候选人数量满足 1 \le n \le 100 \1≤n≤100  ，总票数量满足 1 \le n \le 100 \1≤n≤100
# 输入描述：
# 第一行输入候选人的人数n，第二行输入n个候选人的名字（均为大写字母的字符串），第三行输入投票人的人数，第四行输入投票。
#
# 输出描述：
# 按照输入的顺序，每行输出候选人的名字和得票数量（以" : "隔开，注：英文冒号左右两边都有一个空格！），最后一行输出不合法的票数，格式为"Invalid : "+不合法的票数。


def countTickets(n, ps, m, ts):
    """
    第一行输入候选人的人数n，第二行输入n个候选人的名字（均为大写字母的字符串），
    第三行输入投票人的人数，第四行输入投票。
    :param n:
    :param ps:
    :param m:
    :param ts:
    :return:
    """

    record = {'Invalid': 0}
    for p in ps:
        record[p] = 0

    for t in ts:
        if t in ps:
            record[t] = record.get(t, 0) + 1
        else:
            record['Invalid'] = record.get('Invalid') + 1
    # print(record)

    for p in ps:
        print(p + " : " + str(record.get(p)))
    print("Invalid : "+ str(record.get('Invalid')))


countTickets(4, ['A','B','C','D'], 8, ['A','D','E','CF','A','GG','A','B'])

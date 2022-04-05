"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 15:34
@File        : HJ98 自动售货系统.py
"""


def f(pq):
    w10, w5, w2, w1 = 0, 0, 0, 0  # 记录已经找出的零钱
    while pq > 0:  # 循环直到找零完成
        if pq >= 10 and dic_q['10'] >= 1:  # 可以找10元时
            pq -= 10  # 余额减10
            w10 += 1  # 已经找出的零钱+1
            dic_q['10'] -= 1  # 零钱10数量-1
        elif pq >= 5 and dic_q['5'] >= 1:  # 可以找5元时
            pq -= 5
            w5 += 1
            dic_q['5'] -= 1
        elif pq >= 2 and dic_q['2'] >= 1:
            pq -= 2
            w2 += 1
            dic_q['2'] -= 1
        elif pq >= 1 and dic_q['1'] >= 1:
            pq -= 1
            w1 += 1
            dic_q['1'] -= 1
        else:
            pq -= 1  # 耍赖，如果因零钱不足导致不能退币，则尽最大可能退币，以减少用户损失。
    return pq, w1, w2, w5, w10
while True:
    try:
        s = input().split(';')
        dic_m = {'A1': 2, 'A2': 3, 'A3': 4, 'A4': 5, 'A5': 8, 'A6': 6}  # 商品单价字典
        dic_n = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0}  # 商品数量字典
        dic_q = {'10': 0, '5': 0, '2': 0, '1': 0}  # 零钱字典
        pq = 0
        for i in s[:-1]:
            if i[0] == 'r':  # 系统初始化，把商品数量和零钱放入字典
                b = i.split()
                m = b[1].split('-')
                q = b[2].split('-')
                dic_n['A1'], dic_n['A2'], dic_n['A3'], dic_n['A4'], dic_n['A5'], dic_n['A6'] = int(m[0]), int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])
                dic_q['1'], dic_q['2'], dic_q['5'], dic_q['10'] = int(q[0]), int(q[1]), int(q[2]), int(q[3])
                print('S001:Initialization is successful')
            elif i[0] == 'p':  # 投币
                pq1 = int(i.split()[1])
                if pq1 not in [1, 2, 5, 10]:  # 币值非法
                    print('E002:Denomination error')
                elif pq1 not in [1, 2] and pq1 >= (dic_q['1'] + dic_q['2']*2):  # 存钱盒中1元和2元面额钱币总额小于本次投入的钱币面额
                    print('E003:Change is not enough, pay fail')
                elif dic_n['A1'] == 0 and dic_n['A2'] == 0 and dic_n['A3'] == 0 and dic_n['A4'] == 0 and dic_n['A5'] == 0 and dic_n['A6'] == 0:  # 自动售货机中商品全部销售完毕
                    print('E005:All the goods sold out')
                else :
                    dic_q[str(pq1)] += 1  # 字典对应币值零钱数量加一
                    pq += pq1  # 投币余额增加
                    print('S002:Pay success,balance={}'.format(pq))
            elif i[0] == 'b':  # 购买商品
                bn = i.split()[1]
                if bn not in dic_n.keys():  # 购买的商品不在商品列表中
                    print('E006:Goods does not exist')
                elif dic_n[bn] == 0:  # 所购买的商品的数量为0
                    print('E007:The goods sold out')
                elif int(pq) < dic_m[bn]:  # 投币余额小于待购买商品价格
                    print('E008:Lack of balance')
                else:
                    pq = int(pq) - dic_m[bn]  # 余额相应减少
                    print('S003:Buy success,balance={}'.format(pq))
                    dic_n[bn] -= 1  # 贩卖机物品数量减一
            elif i[0] == 'c':
                if pq == 0:  # 币余额等于0
                    print('E009:Work failure')
                else:  # 按照退币原则进行“找零”
                    pq, w1, w2, w5, w10= f(pq)  # f()函数实现过程
                    print('1 yuan coin number={}'.format(w1))
                    print('2 yuan coin number={}'.format(w2))
                    print('5 yuan coin number={}'.format(w5))
                    print('10 yuan coin number={}'.format(w10))
            elif i[0] == 'q':  # 查询功能
                if ' ' not in i:  # 给出的案例中q1之间无空格，非标准输入。为了过示例添加
                    print('E010:Parameter error')
                elif i.split()[1] not in ['0', '1']:  # “查询类别”参数错误
                    print('E010:Parameter error')
                elif i.split()[1] == '0':  # 查询类别0
                    print('A1 2 {}'.format(dic_n['A1']))
                    print('A2 3 {}'.format(dic_n['A2']))
                    print('A3 4 {}'.format(dic_n['A3']))
                    print('A4 5 {}'.format(dic_n['A4']))
                    print('A5 8 {}'.format(dic_n['A5']))
                    print('A6 6 {}'.format(dic_n['A6']))
                elif i.split()[1] == '1':  # 查询类别1
                    print('1 yuan coin number={}'.format(dic_q['1']))
                    print('2 yuan coin number={}'.format(dic_q['2']))
                    print('5 yuan coin number={}'.format(dic_q['5']))
                    print('10 yuan coin number={}'.format(dic_q['10']))
    except:
        break

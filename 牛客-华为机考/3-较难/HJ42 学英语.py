"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 23:49
@File        : HJ42 学英语.py
"""


def transEnglish(num):
    """
        描述
    Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：

    具体规则如下:
    1.在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如12,345 等
    2.每三位数后记得带上计数单位 分别是thousand, million, billion.
    3.公式：百万以下千以上的数 X thousand X, 10亿以下百万以上的数：X million X thousand X, 10 亿以上的数：X billion X million X thousand X. 每个X分别代表三位数或两位数或一位数。
    4.在英式英语中百位数和十位数之间要加and，美式英语中则会省略，我们这个题目采用加上and，百分位为零的话，这道题目我们省略and

    下面再看几个数字例句：
    22: twenty two
    100:  one hundred
    145:  one hundred and forty five
    1,234:  one thousand two hundred and thirty four
    8,088:  eight thousand (and) eighty eight (注:这个and可加可不加，这个题目我们选择不加)
    486,669:  four hundred and eighty six thousand six hundred and sixty nine
    1,652,510:  one million six hundred and fifty two thousand five hundred and ten

    说明：
    数字为正整数，不考虑小数，转化结果为英文小写；
    保证输入的数据合法
    关键字提示：and，billion，million，thousand，hundred。

    数据范围：1 \le n \le 2000000 \1≤n≤2000000


    输入描述：
    输入一个long型整数

    输出描述：
    输出相应的英文写法
    :param num:
    """

    nums1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
             'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
             'eighteen', 'nineteen']
    nums2 = [0, 0, 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
             'seventy', 'eighty', 'ninety']

    word = []

    def minH(num):
        if 1 <= num < 100:
            if num < 20:
                word.append(nums1[num])
            else:
                word.append(nums2[num//10])
                if num%10 != 0:
                    word.append(nums1[num%10])
        # else:
            # print('1111111')
            # word.append(nums1[num])
    # minH(num)
    # print(word)

    def maxH(num):
        if num >= 100:
            word.append(nums1[num // 100])
            word.append('hundred')
            if num % 100 != 0:
                word.append('and')
        minH(num%100)

    # maxH(num)
    # print(word)

    a = num % 1000  # hundred
    b = (num//1000) % 1000 # thousand
    c = (num//1000//1000) % 1000 # million
    d = (num//1000//1000//1000) % 1000 # billion

    if d > 0:
        maxH(d)
        word.append('billion')
    if c > 0:
        maxH(c)
        word.append('million')

    if b > 0:
        maxH(b)
        word.append('thousand')

    if a >= 0:
        maxH(a)

    print(word)

transEnglish(100)





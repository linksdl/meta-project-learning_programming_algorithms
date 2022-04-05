"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/4/5 14:41
@File        : HJ95 人民币转换.py
"""


gewei = ['零', '壹', '贰', '叁', '肆',
         '伍', '陆', '柒', '捌', '玖']
# 个位的所有数字


def main():
    while True:
        try:
            pre, end = input().split('.')
            # 把我们输入的字符串以我们的小数点作为一个分隔
            print('人民币', end="")
            idx = len(pre)
            # 这个是我们每一个字符后面还有多少位
            for i in range(0, len(pre)):
                # 遍历我们所有的字符
                idx -= 1
                if pre[i] != '0' and not(pre[i] == '1' and idx % 4 == 1):
                    print(gewei[int(pre[i])], end="")
                # 这个是需要转换位中文的
                if idx != 0:
                    # 如果不是个位的话
                    if idx % 8 == 0 and idx >= 8:
                        print('亿', end="")
                    if idx % 4 == 0 and idx % 8 != 0:
                        if pre[i + 1] == '0':
                            print('万零', end="")
                        else:
                            print('万', end="")
                    if idx % 4 == 3 and pre[i] != '0':
                        if pre[i + 1] == '0' and pre[i + 2] != '0':
                            print('仟零', end="")
                        else:
                            print('仟', end="")
                    if idx % 4 == 2 and pre[i] != '0':
                        if pre[i + 1] == '0' and pre[i + 2] != '0':
                            print('佰零', end="")
                        else:
                            print('佰', end="")
                    if idx % 4 == 1 and pre[i] != '0':
                        print('拾', end="")
                    # 分别对我们的最后的单位进行一个判断
            if pre != '0':
                print('元', end="")
                # 正常输出
            if end == "00":
                print("整")
            elif end[0] == '0':
                print(gewei[int(end[1])] + "分")
            elif end[1] == '0':
                print(gewei[int(end[0])] + "角")
            else:
                print(gewei[int(end[0])] + "角" + gewei[int(end[1])] + "分")
            # 处理我们的小数点后面的位置
        except:
            break


if __name__ == '__main__':
    main()

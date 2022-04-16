"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 13:40
@File        : 队列的基本操作及其应用.py
"""



class MyQueue:  # 仅使用两个栈实现队列 MyQueue



    def __init__(self):  # 初始化

        self.mainStack = []  # 主栈 mainStack

        self.tmpStack = []  # 辅助栈 tmpStack



    def push(self, x):  # 元素入队

        self.mainStack.append(x)



    def pop(self):  # 元素出队

        # 主栈除栈底外的其它元素入辅助栈

        while len(self.mainStack) > 1:

            self.tmpStack.append(self.mainStack.pop())

        # 记录主栈栈底元素, 并将其出栈

        top = self.mainStack.pop()

        # 辅助栈中的所有元素依次入主栈

        while self.tmpStack:

            self.mainStack.append(self.tmpStack.pop())

        # 返回出栈的元素

        return top



    def peek(self):  # 访问队头元素

        # 主栈栈顶元素

        while len(self.mainStack) > 1:

            self.tmpStack.append(self.mainStack.pop())

        # 记录主栈栈底元素, 但不出栈

        top = self.mainStack[-1]

        while self.tmpStack:

            self.mainStack.append(self.tmpStack.pop())

        return top



    def empty(self):  # 判断当前队列是否为空

        return not self.mainStack



# Your MyQueue object will be instantiated and called as such:

# obj = MyQueue()

# obj.push(x)

# param_2 = obj.pop()

# param_3 = obj.peek()

# param_4 = obj.empty()

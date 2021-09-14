#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/14 4:47 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 706-设计哈希映射 simple.py

'''
706. 设计哈希映射
https://leetcode-cn.com/problems/design-hashmap/
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：

MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

'''

# 解法3：不定长二维数组
class MyHashMap(object):
    def __init__(self):
        self.N = 1009
        self.data = [[] for _ in range(self.N)]

    def getHashKey(self, key):
        return key % self.N

    def put(self, key, value):
        hashKey = self.getHashKey(key);
        for entry in self.data[hashKey]:
            if entry[0] == key:
                entry[1] = value
                return
        self.data[hashKey].append([key, value])

    def get(self, key):
        hashKey = self.getHashKey(key);
        for entry in self.data[hashKey]:
            if entry[0] == key:
                return entry[1]

        return -1

    def remove(self, key):
        hashKey = self.getHashKey(key);
        for index, entry in enumerate(self.data[hashKey]):
            if entry[0] == key:
                self.data[hashKey].pop(index)
                return

"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 14:06
@File        : 429. N 叉树的层序遍历.py
"""

# 429. N 叉树的层序遍历
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        q = [root]
        print(q)
        while q:
            r =
            for i in range(len(q)):
                node = q.pop(0)
                r.append(node.val)
                if node.children:
                    q.append(node.children)

            # res.append[r]
        return res



class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = list()
        q = deque([root])
        while q:
            cnt = len(q)
            level = list()
            for _ in range(cnt):
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            ans.append(level)

        return ans


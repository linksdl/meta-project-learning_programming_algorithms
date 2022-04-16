"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/8 22:07
@File        : 树的创建.py
"""



import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createTree1(nums):  # 建二叉树(法一: 根据先序遍历数组)
    # 剪枝: 若 nums 数组遍历完成, 或值为-1
    # 则当前节点为空节点
    global pos
    if pos >= len(nums) or nums[pos] == -1:
        return None
    # 创建值为当前访问元素的二叉树节点, 并作为根节点 root
    root = TreeNode(nums[pos])
    # 以 root 为根节点, 递归创建左子树
    pos += 1
    root.left = createTree1(nums)
    # 以 root 为根节点, 递归创建右子树
    pos += 1
    root.right = createTree1(nums)
    # 最终, root 即为所求
return root

def createTree2(nums):  # 建二叉树(法二: 根据层序遍历数组)
    # 数组 nums 的首元素即为二叉树根节点的值
    root = TreeNode(nums[0])
    # BFS 队列, 初始化将根节点入队
    que = collections.deque([root])
    # i - 当前访问元素的下标, tot - 数组 nums 的长度
    i, tot = 1, len(nums)
    # 数组 nums 未遍历结束时, 循环
    while i < tot:
        # 队头节点出队
        curNode = que.popleft()
        # 左右子节点的值
        leftVal, rightVal = nums[i], nums[i + 1] if i + 1 < tot else -1
        # 若左子节点值不为 -1, 则插入以 curNode 为根的左子树中
        if leftVal != -1:
            leftNode = TreeNode(leftVal)
            curNode.left = leftNode
            que.append(leftNode)
        # 若右子节点值不为 -1, 则插入以 curNode 为根的右子树中
        if rightVal != -1:
            rightNode = TreeNode(rightVal)
            curNode.right = rightNode
            que.append(rightNode)
        # 访问后续元素
        i += 2
    # 最终, root 即为所求
return root

def preOrder(root):  # 测试二叉树建树结果(以输出先序遍历序列为例)
    if not root:
        Return

print(root.val, end=" ")

    preOrder(root.left)
preOrder(root.right)

if __name__ == '__main__':
    nums1 = list(map(int, input().strip().split()))
    nums2 = list(map(int, input().strip().split()))
    # pos - 记录遍历先序数组时, 当前元素所在的位置
    global pos; pos = 0
    # 根据先序遍历数组创建二叉树
    tree1 = createTree1(nums)
    # 根据层序遍历数组创建二叉树
    tree2 = createTree2(nums)
    # 测试二叉树建树结果
    preOrder(tree1)
    print()
    preOrder(tree2)


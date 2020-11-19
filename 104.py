# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 15:32
# @Author  : Yike Cheng
# @FileName: 104.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 18:36
# @Author  : Yike Cheng
# @FileName: 222.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
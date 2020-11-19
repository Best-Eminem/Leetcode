# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 16:14
# @Author  : Yike Cheng
# @FileName: 226.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

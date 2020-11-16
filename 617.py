# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 15:25
# @Author  : Yike Cheng
# @FileName: 617.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(t,tr):
            if t and tr:
                t.val += tr.val
                t.left = merge(t.left, tr.left)
                t.right = merge(t.right, tr.right)
                return t
            else:
                return t if t else tr
        return merge(t1, t2)
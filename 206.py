# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 15:33
# @Author  : Yike Cheng
# @FileName: 206.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            tp = cur.next
            cur.next = pre
            pre = cur
            cur = tp
        return pre
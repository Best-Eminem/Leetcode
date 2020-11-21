# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 13:20
# @Author  : Yike Cheng
# @FileName: 148.py
# @Software: PyCharm
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        result = sorted(result)
        if len(result) == 0:
            return None
        tp = ListNode(result[0])
        head = tp
        for i in result[1:]:
            tp.next = ListNode(i)
            tp = tp.next
        return head
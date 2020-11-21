# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 17:26
# @Author  : Yike Cheng
# @FileName: 147.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        result = []
        node = head
        while node:
            result.append(node.val)
            node = node.next
        result = sorted(result)
        if len(result) == 0:
            return None
        head = ListNode(result[0])
        tp = head
        for i in result[1 : ]:
            head.next = ListNode(i)
            head = head.next
        return tp
# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 14:52
# @Author  : Yike Cheng
# @FileName: 2.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0;b = 0;i = 0
        while l1!=None:
            a += (l1.val*10**(i))
            l1 = l1.next
            i+=1
        i=0
        while l2 != None:
            b += (l2.val*10**(i))
            l2 = l2.next
            i+=1
        c = a + b;res = []
        if c == 0: res.append(0)
        while c != 0:
            tmp = c % 10
            res.append(tmp)
            c //= 10
        tp = ListNode(res[0])
        result = tp
        for i in res[1:]:
            tp.next = ListNode(i)
            tp = tp.next
        return result

# l1 = ListNode(0)
# # l1.next=ListNode(4)
# # l1.next.next=ListNode(3)
# l2 = ListNode(0)
# # l2.next=ListNode(6)
# # l2.next.next=ListNode(4)
# tp = addTwoNumbers(l1,l2)
# while tp!=None:
#     print(tp.val)
#     tp = tp.next





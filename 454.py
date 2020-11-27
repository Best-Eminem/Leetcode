# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 12:59
# @Author  : Yike Cheng
# @FileName: 454.py
# @Software: PyCharm
import collections
def fourSumCount( A, B, C, D):
    result = 0
    count = collections.Counter(x+y for x in A for y in B) #得到A,B的和的情况
    for i in C:
        for j in D:
            result += count[- (i + j)]
    return result
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 14:07
# @Author  : Yike Cheng
# @FileName: 941.py
# @Software: PyCharm
def a():
    A = [1,2,5,7,8]
    l = len(A)
    if l < 3:
        return False
    Amax = max(A)
    AMaxIndex = A.index(Amax)
    if (AMaxIndex == 0) | (AMaxIndex == l-1):
        return False
    for i in range(0,AMaxIndex):
        if A[i] >= A[i+1]:
            return False
    for i in range(AMaxIndex+1, l):
        if A[i] >= A[i-1]:
            return False
    return True

print(a())
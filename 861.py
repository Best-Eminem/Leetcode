# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 19:37
# @Author  : Yike Cheng
# @FileName: 861.py
# @Software: PyCharm

def matrixScore(A):
    if not A:
        return 0
    n,m = len(A),len(A[0])
    p = 1<<(m-1)
    print(p)
    res = n*p
    print(res)
    for i in range(n):
        if A[i][0]==0:
            for j in range(m):
                A[i][j]^=1
    for j in range(1,m):
        tmp = 0
        p>>=1
        for i in range(n):
            if A[i][j]==1:
                tmp+=1
        res +=p*max(tmp,(n-tmp))
    return res
matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
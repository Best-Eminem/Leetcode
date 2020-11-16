# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 15:22
# @Author  : Yike Cheng
# @FileName: 973.py
# @Software: PyCharm
# 最接近原点的k个点
from math import sqrt


def kClosest(points, K):
    arr = sorted(points, key=lambda x: x[0]**2+x[1]**2)
    print(arr[0:K])
points = [[5,5],[4,4],[3,3],[2,2],[1,1]];K = 2
kClosest(points, K)
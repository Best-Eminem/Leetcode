# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 14:26
# @Author  : Yike Cheng
# @FileName: 1356.py
# @Software: PyCharm

def sortByBits(arr):
    arr = sorted(arr, key=lambda x: (bin(x).count('1')))
    return sorted(arr, key=lambda x:(x))
print(sortByBits([1,2,3,4,5,6,7,8]))
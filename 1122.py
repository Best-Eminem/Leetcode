# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 9:45
# @Author  : Yike Cheng
# @FileName: 1122.py
# @Software: PyCharm
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        for i in arr2:
            tmp = arr1.count(i)
            while tmp != 0:
                arr3.append(i)
                tmp -= 1
        arr4 = [i for i in arr1 if i not in arr2]
        arr4.sort()
        for i in arr4:
            arr3.append(i)
        return arr3

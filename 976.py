# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 17:19
# @Author  : Yike Cheng
# @FileName: 976.py
# @Software: PyCharm
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse = True)
        for i in range(0,len(A)-2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
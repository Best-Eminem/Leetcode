# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 15:31
# @Author  : Yike Cheng
# @FileName: 1030.py
# @Software: PyCharm
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = []
        for i in range(R):
            for j in range(C):
                result.append([i,j])
        result = sorted(result, key = lambda x:abs(r0 - x[0]) + abs(c0 - x[1]))
        return result
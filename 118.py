# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 18:23
# @Author  : Yike Cheng
# @FileName: 118.py
# @Software: PyCharm
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1],[1,1]]
        if numRows<=0:
            return []
        elif numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            for i in range(3, numRows + 1):
                tp = [1]
                pre = result[i-2]
                for l in range(len(pre)-1):
                    tp.append(pre[l] + pre[l + 1])
                tp.append(1)
                result.append(tp)
            return result




#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
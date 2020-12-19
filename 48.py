# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 18:40
# @Author  : Yike Cheng
# @FileName: 48.py
# @Software: PyCharm
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = zip(*reversed(matrix))

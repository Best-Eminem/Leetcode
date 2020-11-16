# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 15:40
# @Author  : Yike Cheng
# @FileName: 461.py
# @Software: PyCharm
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
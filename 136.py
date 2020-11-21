# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 17:24
# @Author  : Yike Cheng
# @FileName: 136.py
# @Software: PyCharm
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        j = 0
        for i in nums:
            j = j^i
        return j
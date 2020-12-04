# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 15:55
# @Author  : Yike Cheng
# @FileName: 1672.py
# @Software: PyCharm
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts)
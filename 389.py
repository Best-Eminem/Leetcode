# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 18:16
# @Author  : Yike Cheng
# @FileName: 389.py
# @Software: PyCharm
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t)-Counter(s))[0]
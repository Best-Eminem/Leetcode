# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:17
# @Author  : Yike Cheng
# @FileName: 242.py
# @Software: PyCharm
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 18:38
# @Author  : Yike Cheng
# @FileName: 387.py
# @Software: PyCharm
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
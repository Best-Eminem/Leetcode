# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 16:59
# @Author  : Yike Cheng
# @FileName: 290.py
# @Software: PyCharm
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1 = defaultdict(str)
        dict2 = defaultdict(str)
        s = s.split(' ')
        if len(pattern) != len(s):return False
        for i in range(len(s)):
            tp1 = dict1[pattern[i]]
            tp2 = dict2[s[i]]
            if tp1 == '':
                dict1[pattern[i]] = s[i]
            elif tp1 != s[i]:
                return False
            if tp2 == '':
                dict2[s[i]] = pattern[i]
            elif tp2 != pattern[i]:
                return False
        return True
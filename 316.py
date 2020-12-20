# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 16:48
# @Author  : Yike Cheng
# @FileName: 316.py
# @Software: PyCharm
class Solution:
    def removeDuplicateLetters(self, s) -> str:
        stack = []
        seen = set()
        remain_counter = collections.Counter(s)
        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)

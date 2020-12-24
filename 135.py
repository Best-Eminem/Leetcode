# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 21:11
# @Author  : Yike Cheng
# @FileName: 135.py
# @Software: PyCharm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        right = result = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            result += max(left[i], right)

        return result
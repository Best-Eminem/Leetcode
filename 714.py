# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 16:25
# @Author  : Yike Cheng
# @FileName: 714.py
# @Software: PyCharm
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell
# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 20:56
# @Author  : Yike Cheng
# @FileName: 122.py
# @Software: PyCharm
def maxProfit(prices):
    result = 0;start = 0;end = 0;i = 0
    while i < len(prices)-1:
        if prices[i] < prices[i+1]:
            start = prices[i]
            end = prices[i + 1]
            i += 1
            while i+1 < len(prices) and prices[i] < prices[i+1]:
                end = prices[i+1]
                i += 1
            result += end - start
            end = 0;start = 0
        else:i += 1
    return result
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
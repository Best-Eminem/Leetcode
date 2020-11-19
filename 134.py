# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 15:22
# @Author  : Yike Cheng
# @FileName: 134.py
# @Software: PyCharm
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas);i = 0
        while i < n:
            sumOfGas = 0;
            sumOfCost = 0
            count = 0
            while count < n:
                j = (i + count) % n
                sumOfGas += gas[j]
                sumOfCost += cost[j]
                if sumOfGas < sumOfCost :
                    break
                count += 1
            if count == n:
                return i
            else:
                i += count + 1
        return -1


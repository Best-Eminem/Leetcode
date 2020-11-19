# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 15:44
# @Author  : Yike Cheng
# @FileName: 283.py
# @Software: PyCharm
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key = bool, reverse = True)
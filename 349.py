# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 20:08
# @Author  : Yike Cheng
# @FileName: 349.py
# @Software: PyCharm
# 给定两个数组，编写一个函数来计算它们的交集。
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
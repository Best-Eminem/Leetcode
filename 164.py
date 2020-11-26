# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 14:58
# @Author  : Yike Cheng
# @FileName: 164.py
# @Software: PyCharm
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        result = 0
        for i in range(len(nums) - 1):
            tp = nums[i+1] - nums[i]
            if tp > result:
                result = tp
        return result
# 啪的一下很快啊， 桶排序是最优解
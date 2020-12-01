# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 12:39
# @Author  : Yike Cheng
# @FileName: 34.py
# @Software: PyCharm
# [5,7,7,8,8,10]
def searchRange(nums, target):
    def binarySearch(nums, target, lower):
        left = 0;right = len(nums) - 1; ans = len(nums)
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] > target or (lower and nums[mid] >= target) :
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
    result = []
    if len(nums) == 0:
        return [-1,-1]
    leftin = binarySearch(nums, target, True)
    rightin = binarySearch(nums, target, False) - 1
    if leftin >= 0 and leftin <= len(nums) - 1 and rightin >= 0 and rightin <= len(nums) - 1 and \
            (nums[leftin] == target and nums[rightin] == target):
        result.append(leftin)
        result.append(rightin)
    else :
        result.append(-1)
        result.append(-1)
    return result
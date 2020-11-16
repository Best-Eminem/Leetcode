# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 14:31
# @Author  : Yike Cheng
# @FileName: 31.py
# @Software: PyCharm
def nextPermutation(nums):
    """
    1,2,3 → 1,3,2
    3,2,1,4 → 3,2,4,1
    1,1,5 → 1,5,1
    Do not return anything, modify nums in-place instead.
    """
    small = -1;s_flag = -1
    for i in reversed(range(len(nums)-1)):
        if nums[i] < nums[i+1]:
            small = nums[i]
            s_flag = i
            break
    if small != -1 and s_flag != -1:
        for j in reversed(range(s_flag+1,len(nums))):
            if nums[j] > small:
                nums[s_flag],nums[j] = nums[j],nums[s_flag]
                break
    left, right = s_flag + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    
nums = [1,3,2]
nextPermutation(nums)
print(nums)

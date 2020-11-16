# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 12:41
# @Author  : Yike Cheng
# @FileName: 5561.py
# @Software: PyCharm
def getMaximumGenerated(n: int) -> int:
    if n == 0: return 0
    nums = [0, 1]
    for i in range(n + 1):
        nums.append(-1)
    for i in range(1, n // 2 + 1):
        if 2 * i >= 2 and 2 * i <= n:
            nums[i * 2] = nums[i]
        if 2 * i + 1 >= 2 and 2 * i + 1 <= n:
            nums[i * 2 + 1] = nums[i] + nums[i + 1]
    return max(nums)
print(getMaximumGenerated(3))

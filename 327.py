# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 15:25
# @Author  : Yike Cheng
# @FileName: 327.py
# @Software: PyCharm
# 解法一 超时
# def countRangeSum(nums, lower, upper):
#     index = []
#     damn = len(nums)
#     for i in range(damn):
#         for j in range(i,damn):
#             index.append([i,j])
#     print(index)
#     result = 0
#     for x,y in index:
#         if x == y:
#             tp = nums[x]
#         else:
#             tp = sum(nums[x:y+1])
#         #print(tp)
#         if tp <= upper and tp >= lower:
#             result += 1
#     return result

#解法二 归并排序
def countRangeSumRecursive(sum, lower, upper, left, right):
    if left == right:
        return 0
    else:
        mid = (left + right) // 2
        n1 = countRangeSumRecursive(sum, lower, upper, left, mid)
        n2 = countRangeSumRecursive(sum, lower, upper, mid + 1, right)
        #print(n1,n2)
        ret = n1 + n2

        #首先统计下标对的数量
        i = left  #0
        l = mid + 1
        r = mid + 1
        while i <= mid:
            while (l <= right and sum[l] - sum[i] < lower): l += 1
            while (r <= right and sum[r] - sum[i] <= upper): r += 1
            ret += (r - l)
            i += 1
        # 随后合并两个排序数组
        tmp_sum = sorted(sum[left:right+1])

        j = 0
        for i in range(left, right+1):
            sum[i] = tmp_sum[j]
            j += 1
        #print(ret)
        return ret
def countRangeSum(nums, lower, upper):
    sum = [];tp = 0;num = 0
    for i in nums:
        if i >= lower and i <= upper:
            num += 1
    for i in nums:
        tp += i
        sum.append(tp)
    return num + countRangeSumRecursive(sum, lower, upper, 0, len(sum)-1)

nums = [-2,5,-1,1,3]
#[-2,3,2]
lower = -2
upper = 2
print(countRangeSum(nums, lower, upper))

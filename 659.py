# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 15:55
# @Author  : Yike Cheng
# @FileName: 659.py
# @Software: PyCharm
import collections
import heapq
def isPossible(nums):
    dic = collections.defaultdict(list)
    for i in nums:
        heap = dic.get(i - 1)
        if heap:
            preLength = heapq.heappop(heap)
            heapq.heappush(dic[i], preLength + 1)
        else:
            heapq.heappush(dic[i], 1)
    return not any(heap and heap[0] < 3 for heap in dic.values())

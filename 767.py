# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 17:20
# @Author  : Yike Cheng
# @FileName: 767.py
# @Software: PyCharm
from heapq import *
import collections
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S

        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""

        queue = [(-x[1], x[0]) for x in counts.items()]

        heapify(queue)
        print(queue)
        ans = []
        while len(queue) > 1:
            _, letter1 = heappop(queue)
            _, letter2 = heappop(queue)
            ans.extend([letter1, letter2])
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heappush(queue, (-counts[letter2], letter2))
        if queue:
            ans.append(queue[0][1])

        return "".join(ans)
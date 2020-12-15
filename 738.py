# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 12:11
# @Author  : Yike Cheng
# @FileName: 738.py
# @Software: PyCharm
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = str(N)
        for i in range(1,len(N)):
            if N[i-1]>N[i] :  break    # 找到不符合的第一个位置
        else : return int(N)    # 若该数本身符合条件，直接返回

        for j in range(i-1,0,-1):
            if N[j-1]<N[j] and N[j]>'0' : break    # 找到可以减1的第一个位置
        else : j = 0    # 都不符合，则只能在开头减1

        return int(N[:j] + str(int(N[j]) - 1) + '9'*(len(N)-j-1))

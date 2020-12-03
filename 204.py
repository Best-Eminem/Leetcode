# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:17
# @Author  : Yike Cheng
# @FileName: 204.py
# @Software: PyCharm
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        def is_prime(x):
            if (x == 2) or (x == 3):
                return True
            if (x % 6 != 1) and (x % 6 != 5):
                return False
            for i in range(5, int(x ** 0.5) + 1, 6):
                if (x % i == 0) or (x % (i + 2) == 0):
                    return False
            return True

        result = 1
        for i in range(3, n, 2):
            if is_prime(i):
                result += 1
        return result



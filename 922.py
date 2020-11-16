# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 13:10
# @Author  : Yike Cheng
# @FileName: 922.py
# @Software: PyCharm
#超时
# def sortArrayByParityII(A):
#     result = [];even = 1
#     while len(result) != len(A):
#         for i in range(len(A)):
#             if A[i] >=0 and even == 1 and A[i]%2 == 0:
#                 result.append(A[i])
#                 even = 0
#                 A[i] = -1
#                 break
#             elif A[i] >=0 and even == 0 and A[i]%2 == 1:
#                 result.append(A[i])
#                 even = 1
#                 A[i] = -1
#                 break
#     return result
def sortArrayByParityII(A):
    result = [];odd = [];even = [];e = 0;o = 0
    for i in A:
        if i%2==1:
            odd.append(i)
        else:even.append(i)
    for i in range(len(A)):
        if i%2 == 0:
            result.append(even[e])
            e += 1
        else:
            result.append(odd[o])
            o += 1
    return result



A = [4,2,5,7]
print(sortArrayByParityII(A))
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 15:15
# @Author  : Yike Cheng
# @FileName: 1370.py
# @Software: PyCharm
def sortString(s):
    s = ''.join(sorted(s))
    result = ''
    # print(s)
    while len(s) > 0:
        tp = ''
        for i in s:
            if i != tp:
                tp = i
                result += i
                s = s.replace(i, '', 1)
        tp = ''
        for i in s[::-1]:
            if i != tp:
                tp = i
                result += i
                s = s.replace(i, '', 1)

    return result

print(sortString('aaaabbbbcccc'))
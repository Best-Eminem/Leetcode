# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 14:38
# @Author  : Yike Cheng
# @FileName: 406.py
# @Software: PyCharm
def reconstructQueue(people):
    people = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
    print(people)
    result = []
    result.append(people[0])
    for i in people[1:]:
        y = i[1]
        result.insert(y,i)
    print(result)

reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])

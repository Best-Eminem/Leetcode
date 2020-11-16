# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 10:31
# @Author  : Yike Cheng
# @FileName: 5601.py
# @Software: PyCharm
class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.dict =[]
        self.length = n

    def insert(self, id: int, value: str):
        self.dict.append([id,value])
        if id == self.ptr:
            result = []
            self.dict = sorted(self.dict,key=lambda x:x[0])
            tp = id
            for x,y in self.dict[id-1:]:
                if x == tp:
                    result.append(y)
                    self.ptr += 1
                    tp += 1
                else:break
            return result
        else:
            return []
obj = OrderedStream(5)
test = [[3,"ccccc"],[1,"aaaaa"],[2,"bbbbb"],[5,"eeeee"],[4,"ddddd"]]
for id,value in test:
    #print(id,value)
    param_1 = obj.insert(id,value)
    print(param_1)


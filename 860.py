# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 9:46
# @Author  : Yike Cheng
# @FileName: 860.py
# @Software: PyCharm
def lemonadeChange(bills):
    money = [0,0,0]
    for i in bills:
        if i == 5:
            money[0] += 1
        elif i == 10:
            money[1] += 1
            if money[0] >= 1:
                money[0] -= 1
            else:return False
        else:
            money[2] += 1
            if money[0] >= 1 and money[1] >= 1:
                money[0] -= 1
                money[1] -= 1
            elif money[0] >= 3:
                money[0] -= 3
            else:return False

    return True

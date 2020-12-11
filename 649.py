# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 15:07
# @Author  : Yike Cheng
# @FileName: 649.py
# @Software: PyCharm
def predictPartyVictory(self, senate: str) -> str:
    n = len(senate)
    radiant = collections.deque()
    dire = collections.deque()

    for i, ch in enumerate(senate):
        if ch == "R":
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        if radiant[0] < dire[0]:
            radiant.append(radiant[0] + n)
        else:
            dire.append(dire[0] + n)
        radiant.popleft()
        dire.popleft()

    return "Radiant" if radiant else "Dire"

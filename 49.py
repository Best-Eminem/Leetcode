# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 18:25
# @Author  : Yike Cheng
# @FileName: 49.py
# @Software: PyCharm
import collections


def groupAnagrams(strs):
    mp = collections.defaultdict(list)
    for st in strs:
        key = "".join(sorted(st))
        print(key)
        mp[key].append(st)
    return list(mp.values())
groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 7:47 下午
# @Author  : MaJiong
# @File    : Leetcode495.py
# @Software: PyCharm
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time = 0
        for i in range(1, len(timeSeries)):
            time += min(timeSeries[i] - timeSeries[i - 1], duration)
        return time + duration


s = Solution()
print(s.findPoisonedDuration([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))

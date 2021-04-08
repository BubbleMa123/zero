#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 8:03 下午
# @Author  : MaJiong
# @File    : Leetcode414.py
# @Software: PyCharm
'''
    python中正无穷负无穷的表示方式
    float('inf') -- 正无穷
    float('-inf') -- 负无穷
'''
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return sorted(set(nums))[-3] if len(set(nums)) > 2 else sorted(set(nums))[-1]


s = Solution()


# print(s.thirdMax([2, 2, 3, 1]))


class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = float('-inf')
        for x in nums:
            if x > a:
                a, b, c = x, a, b
            elif x >= b and x != a:
                b, c = x, b
            elif x > c and x != b and x != a:
                c = x
        print(a, b, c)
        return c if c != float('-inf') else a


s = Solution1()
print(s.thirdMax([1, 2, 2, 5, 3, 5]))

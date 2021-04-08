#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 8:30 下午
# @Author  : MaJiong
# @File    : Leetcode628.py
# @Software: PyCharm
from typing import List

'''
    分析数组内的正负
    python 正无穷负无穷
'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


class Solution1:
    def maximumProduct(self, nums: List[int]) -> int:
        max_a = max_b = max_c = float('-inf')
        min_a = min_b = float('inf')
        for num in nums:
            if num > max_a:
                max_a, max_b, max_c = num, max_a, max_b
            elif num > max_b:
                max_b, max_c = num, max_b
            elif num > max_c:
                max_c = num

            if num < min_a:
                min_a, min_b = num, min_a
            elif num < min_b:
                min_b = num
        return max(max_a * max_b * max_c, max_a * min_a * min_b)


s = Solution1()
print(s.maximumProduct([-1, -2, -3, -4, -5]))

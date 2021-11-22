# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/22
# Description: Leetcode 78. Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start_id) -> None:
            # 收集子集，要先于终止判断
            res.append(path[:])
            # Base Case
            if start_id == len(nums):
                return

            # 单层递归逻辑
            for i in range(start_id, len(nums)):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()     # 回溯

        backtracking(0)
        return res

# from itertools import combinations
#
# [j for i in range(len(nums)) for j in combinations(nums, i)]

# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/22
# Description: Leetcode 90. Subsets II

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start_id):
            res.append(path[:])
            if start_id == len(nums):
                return
            for i in range(start_id, len(nums)):
                if i > start_id and nums[i] == nums[i - 1]:
                    # 当前后元素值相同时，跳入下一个循环，去重
                    continue
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        nums.sort()
        backtracking(0)
        return res

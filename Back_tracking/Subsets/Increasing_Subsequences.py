# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/22
# Description: Leetcode 491. Increasing Subsequences

# Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements.
# You may return the answer in any order.
# The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.

# Example 1:
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

# Example 2:
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]

# Constraints:
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start_id):
            if len(path) >= 2:
                res.append(path[:])
            if start_id == len(nums):
                return
            used = set()
            for i in range(start_id, len(nums)):
                if nums[i] not in used:
                    if len(path) == 0 or nums[i] >= path[-1]:
                        used.add(nums[i])
                        path.append(nums[i])
                        backtracking(i + 1)
                        path.pop()

        backtracking(0)
        return res

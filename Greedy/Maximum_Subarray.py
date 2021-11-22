# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/21
# Description: Leetcode 53. Maximum Subarray

# Given an integer array nums,
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        count = 0
        for x in nums:
            count += x
            res = max(count, res)
            count = max(count, 0)
        return res

    # DP
    # def maxSubArray(self, nums: List[int]) -> int:
    #     best_sum = float('-inf')  # or: float('-inf')
    #     current_sum = 0
    #     for x in nums:
    #         current_sum = max(x, current_sum + x)
    #         best_sum = max(best_sum, current_sum)
    #     return best_sum

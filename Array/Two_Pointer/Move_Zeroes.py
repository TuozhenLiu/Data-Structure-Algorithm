# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/28
# Description: Leetcode 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_p = 0
        for fast_p in range(len(nums)):
            if nums[fast_p] != 0:
                nums[slow_p] = nums[fast_p]  # or directly swap, nums[left], nums[right] = nums[right], nums[left]
                slow_p += 1
        # nums = nums[:slow_p] + [0] * (len(nums) - slow_p)
        # ⬆ leetcode bug, cannot modify
        for i in range(slow_p, len(nums)):
            nums[i] = 0
# time complexity: O(N)
# space complexity: O(1)

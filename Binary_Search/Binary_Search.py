# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/22
# Description: Leetcode 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:
# 1 <= nums.length <= 104           ## if length can be 0, need to add "if not nums: return -1" on the top
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if not nums:
        #     return -1
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
# time complexity: O(logN)
# space complexity: O(1)

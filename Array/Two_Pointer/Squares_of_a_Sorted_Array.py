# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/29
# Description: Leetcode 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_p, right_p = 0, len(nums) - 1
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            left, right = nums[left_p] ** 2, nums[right_p] ** 2
            if left <= right:
                ans[i] = right
                right_p -= 1
            else:
                ans[i] = left
                left_p += 1
        return ans
# time complexity: O(N)
# space complexity: O(1) (besides the answer array) / O(N)


# mySolution = Solution()
# x = [-7, -6, -5, -4, 0, 2, 3, 6]
# print(mySolution.sortedSquares(x))

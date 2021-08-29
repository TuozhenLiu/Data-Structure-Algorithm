# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/29
# Description: Leetcode 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
# of which the sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow_p = fast_p = 0
        sum_sub = 0
        ans = len(nums) + 1
        while fast_p < len(nums):  # move fast_p
            sum_sub += nums[fast_p]
            while sum_sub >= target:  # move slow_p
                ans = min(ans, fast_p - slow_p + 1)
                sum_sub -= nums[slow_p]
                slow_p += 1
            fast_p += 1
        ans = 0 if ans == len(nums) + 1 else ans
        return ans
# time complexity: O(N) (2N: Although 2 loops, both slow_p and fast_p moves N times)
# space complexity: O(1)


Mysolution = Solution()
x = [2, 3, 1, 2, 4, 3]
print(Mysolution.minSubArrayLen(7, x))

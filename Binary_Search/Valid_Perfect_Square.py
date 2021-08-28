# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/28
# Description: Leetcode 367. Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

# Example 1:
# Input: num = 16
# Output: true

# Example 2:
# Input: num = 14
# Output: false

# Constraints:
# 1 <= num <= 2^31 - 1
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            mid_mid = mid * mid
            if mid_mid > num:
                right = mid - 1
            elif mid_mid < num:
                left = mid + 1
            else:
                return True
        return False
# time complexity: O(log(N))
# space complexity: O(1)

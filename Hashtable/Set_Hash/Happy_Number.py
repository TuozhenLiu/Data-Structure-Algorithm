# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/6
# Description: Leetcode 202. Happy Number

# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

# Constraints:
# 1 <= n <= 231 - 1
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(x):
            sum_ = 0
            while x:
                # 当前个位
                sum_ += (x % 10) ** 2
                x //= 10
            return sum_
        # check if sum_ appear duplicately
        record = set()
        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            elif n in record:
                return False
            else:
                record.add(n)
    # time complexity: O(MlogM+NlogN)
    # space complexity: O(logM+logN)

# mysolution = Solution()
# print(mysolution.isHappy(19))

# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/6
# Description: Leetcode 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        return s
    # time complexity: O(N)
    # space complexity: O(1)

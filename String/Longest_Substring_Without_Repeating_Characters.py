# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/7
# Description: Leetcode 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = 0
        max_len = 0
        slide = ""
        while p < len(s):
            if s[p] in slide:
                max_len = max(len(slide), max_len)
                slide = slide[slide.index(s[p]) + 1:]
            slide += s[p]
            p += 1
        max_len = max(len(slide), max_len)
        return max_len
    # time complexity: O(N)
    # space complexity: O(∣Σ∣)

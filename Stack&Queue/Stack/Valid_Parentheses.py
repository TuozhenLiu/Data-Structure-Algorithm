# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/7
# Description: Leetcode 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in s:
            if i in "([{":
                stack.append(i)
            elif not stack:
                return False
            else:
                popped = stack.pop()
                if (popped == "{" and i == "}") or (popped == "[" and i == "]") or (popped == "(" and i == ")"):
                    continue
                else:
                    return False
        return False if stack else True
    # time complexity: O(N)
    # space complexity: O(N+∣Σ∣)



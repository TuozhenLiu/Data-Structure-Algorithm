# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/28
# Description: Leetcode 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a##c", t = "#a#c"
# Output: true
# Explanation: Both s and t become "c".

# Example 4:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

# Constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = len(s) - 1, len(t) - 1
        skip_s = skip_t = 0
        while s_pointer >= 0 or t_pointer >= 0:
            # do backspace
            while s_pointer >= 0:
                if s[s_pointer] == "#":
                    s_pointer -= 1
                    skip_s += 1
                elif skip_s > 0:
                    s_pointer -= 1
                    skip_s -= 1
                else:
                    break
            while t_pointer >= 0:
                if t[t_pointer] == "#":
                    t_pointer -= 1
                    skip_t += 1
                elif skip_t > 0:
                    t_pointer -= 1
                    skip_t -= 1
                else:
                    break
            # check equal
            if s_pointer >= 0 and t_pointer >= 0 and s[s_pointer] == t[t_pointer]:
                s_pointer -= 1
                t_pointer -= 1
            elif s_pointer != -1 or t_pointer != -1:
                return False
        # s_pointer == t_pointer == -1
        return True
# time complexity: O(N+M)
# space complexity: O(1)


# mySolution = Solution()
# s = "ab#c"
# t = "ad#c"
# print(mySolution.backspaceCompare(s, t))

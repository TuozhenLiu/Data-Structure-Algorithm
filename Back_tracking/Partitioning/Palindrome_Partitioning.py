# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/22
# Description: Leetcode 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtracking(s, start_id):
            if start_id == len(s):
                res.append(path[:])
                return
            for i in range(start_id, len(s)):
                if self.is_palindrome(s, start_id, i):
                    path.append(s[start_id: (i + 1)])
                    backtracking(s, i + 1)
                    path.pop()

        backtracking(s, 0)
        return res

    def is_palindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# 回文数的判断也可以通过DP的方法全部事先算好
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         n = len(s)
#         f = [[True] * n for _ in range(n)]
#
#         for i in range(n - 1, -1, -1):
#             for j in range(i + 1, n):
#                 f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]
#
#         ret = list()
#         ans = list()
#
#         def dfs(i: int):
#             if i == n:
#                 ret.append(ans[:])
#                 return
#
#             for j in range(i, n):
#                 if f[i][j]:
#                     ans.append(s[i:j + 1])
#                     dfs(j + 1)
#                     ans.pop()
#
#         dfs(0)
#         return ret

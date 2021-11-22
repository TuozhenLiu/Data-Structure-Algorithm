# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/21
# Description: Leetcode 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

# Constraints:
# 0 <= n <= 30
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    # DP
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q
        return r
    # time complexity: O(N)
    # space complexity: O(1)

# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return n
#         else:
#             return self.fib(n-1) + self.fib(n-2)
    # time complexity: O(N^2)
    # space complexity: O(N)

# class Solution:
# def fib(self, n: int) -> int:
#     if n < 2:
#         return n

#     q = [[1, 1], [1, 0]]
#     res = self.matrix_pow(q, n - 1)
#     return res[0][0]

# def matrix_pow(self, a: List[List[int]], n: int) -> List[List[int]]:
#     ret = [[1, 0], [0, 1]]
#     while n > 0:
#         if n & 1:
#             ret = self.matrix_multiply(ret, a)
#         n >>= 1
#         a = self.matrix_multiply(a, a)
#     return ret

# def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
# c = [[0, 0], [0, 0]]
# for i in range(2):
#     for j in range(2):
#         c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
# return c

# class Solution:
#     def fib(self, n: int) -> int:
        # sqrt5 = 5**0.5
        # fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        # return round(fibN / sqrt5)

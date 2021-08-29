# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/29
# Description: Leetcode 59. Spiral Matrix II

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, up, down = 0, n - 1, 0, n - 1
        matrix = [[0] * n for _ in range(n)]
        num = 1
        while left <= right:
            for i in range(left, right + 1):
                matrix[up][i] = num
                num += 1
            for j in range(up + 1, down + 1):
                matrix[j][right] = num
                num += 1
            for i in range(right - 1, left - 1, -1):
                matrix[down][i] = num
                num += 1
            for j in range(down - 1, up, -1):
                matrix[j][left] = num
                num += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        return matrix
# time complexity: O(N^2)
# space complexity: O(1) (besides the answer array)

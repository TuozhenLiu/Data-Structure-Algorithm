# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/29
# Description: 剑指 Offer 29. 顺时针打印矩阵

# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]

# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

# 限制：
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0]) if n != 0 else 0
        left, right, up, down = 0, m - 1, 0, n - 1
        ans = []
        while left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            if len(ans) == n*m:
                break
            for j in range(up + 1, down + 1):
                ans.append(matrix[j][right])
            if len(ans) == n*m:
                break
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[down][i])
            if len(ans) == n*m:
                break
            for j in range(down - 1, up, -1):
                ans.append(matrix[j][left])
            if len(ans) == n*m:
                break
            left += 1
            right -= 1
            up += 1
            down -= 1
        return ans
# time complexity: O(N^2)
# space complexity: O(1) (besides the answer array)

# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/6
# Description: Leetcode 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20
# 1 <= k <= n
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(n, k, start_id):
            # 终止条件
            if len(path) == k:
                res.append(path[:])  # 对于一维列表浅拷贝就够
                return
            # 横向遍历
            for i in range(start_id, n-k+len(path)+2):  # 剪枝：不够k-len(path)个就停止了
                path.append(i)
                # 纵向递归
                backtracking(n, k, i + 1)
                # 回退
                path.pop()

        backtracking(n, k, 1)
        return res
# time complexity: O(C(N K) * K)  C(N, k)个组合，记录答案需要K（拷贝）
# space complexity: O(N + K)


solution = Solution()
print(solution.combine(4, 2))

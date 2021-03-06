# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/17
# Description: Leetcode 216. Combination Sum III

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations.
# The list must not contain the same combination twice, and the combinations may be returned in any order.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.

# Example 3:
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

# Example 4:
# Input: k = 3, n = 2
# Output: []
# Explanation: There are no valid combinations.

# Example 5:
# Input: k = 9, n = 45
# Output: [[1,2,3,4,5,6,7,8,9]]
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
# There are no other valid combinations.

# Constraints:
# 2 <= k <= 9
# 1 <= n <= 60
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []  # 存放结果集
        path = []  # 符合条件的结果

        def findallPath(n, k, sum, startIndex):
            if sum == n and len(path) == k:  # 如果path.size() == k 但sum != n 直接返回
                return res.append(path[:])
            minIndex = max(startIndex, (n - sum) - (k - len(path) - 1) * 9)  # 剪枝操作：提前预知sum太小
            maxIndex = min(9 - (k - len(path) - 1), (n - sum) - (k - len(path) - 1) * startIndex)  # 剪枝操作：预留出987...，提前预知sum太大
            # if new_startIndex>startIndex:
            #     print("剪枝")
            for i in range(minIndex, maxIndex + 1):
                path.append(i)
                sum += i
                findallPath(n, k, sum, i+1)  # 注意i+1调整startIndex
                sum -= i  # 回溯
                path.pop()  # 回溯

        findallPath(n, k, 0, 1)
        return res
# time complexity: O(C(M K) * K)  C(M, k)个组合，记录答案需要K（拷贝）本例 M = 9
# space complexity: O(M + K)

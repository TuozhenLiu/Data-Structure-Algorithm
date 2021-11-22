# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/19
# Description: Leetcode 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]

# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(target, sum, start_id):
            if sum == target:
                res.append(path[:])
                return
            for i in range(start_id, len(candidates)):
                cand = candidates[i]
                if i > start_id and candidates[i] == candidates[i - 1]:
                    continue
                if sum + cand > target:
                    return
                sum += cand
                path.append(cand)
                backtracking(target, sum, i + 1)
                sum -= cand
                path.pop()

        candidates.sort()
        backtracking(target, 0, 0)
        return res
    # time complexity: O(2^N * N)
    # space complexity: O(N)


mysolution = Solution()
mysolution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

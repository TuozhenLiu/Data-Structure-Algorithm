# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/11
# Description: Leetcode 912. Sort an Array

# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def max_heapify(self, heap, root, length):
        p = root
        while p * 2 + 1 < length:
            l = p * 2 + 1
            r = p * 2 + 2
            if r == length or heap[l] > heap[r]:
                cache = l
            else:
                cache = r
            if heap[p] < heap[cache]:
                heap[p], heap[cache] = heap[cache], heap[p]
                p = cache
            else:
                break

    def build_heap(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            self.max_heapify(nums, i, len(nums))
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        self.build_heap(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.max_heapify(nums, 0, i)
        return nums
    # time complexity: O(N+NlogN)
    # space complexity: O(1)


mySolution = Solution()
print(mySolution.sortArray([1, 3, 2, 5, 7, 8]))

# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/11
# Description: Leetcode 

# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def max_heapify(self, heap, root):
        length = len(heap)
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
            self.max_heapify(nums, i)
        return nums


mySolution = Solution()
print(mySolution.build_heap([4, 6, 8, 5, 9]))

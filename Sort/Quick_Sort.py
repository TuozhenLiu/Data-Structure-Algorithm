# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/11
# Description: Leetcode 912. Sort an Array

# ----------------------------------------------------------------------------------------------------------------------
import random
from typing import List


class Solution:
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]

        left = l - 1
        for right in range(l, r):
            if nums[right] < nums[r]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
        left += 1
        nums[left], nums[r] = nums[r], nums[left]
        return left

    def randomized_quicksort(self, nums, l, r):
        if r > l:
            mid = self.randomized_partition(nums, l, r)
            self.randomized_quicksort(nums, l, mid - 1)
            self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums
    # time complexity: O(NlogN)
    # space complexity: O(logN)


mySolution = Solution()
print(mySolution.sortArray([5, 2, 3, 1]))

# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/11
# Description: Leetcode 912. Sort an Array

# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def merge_sort(self, nums, l, r):
        if l < r:
            mid = (r + l) // 2
            self.merge_sort(nums, l, mid)
            self.merge_sort(nums, mid + 1, r)
            point_l, point_r = l, mid + 1
            tmp = []
            while point_l <= mid:
                if point_r > r:
                    tmp.extend(nums[point_l:(mid + 1)])
                    break
                if nums[point_l] < nums[point_r]:
                    tmp.append(nums[point_l])
                    point_l += 1
                else:
                    tmp.append(nums[point_r])
                    point_r += 1
            else:
                if point_r <= r:
                    tmp.extend(nums[point_r:(r + 1)])
            nums[l:(r + 1)] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums
    # time complexity: O(NlogN)
    # space complexity: O(N)


mySolution = Solution()
print(mySolution.sortArray([1, 3, 2, 5, 7, 8]))

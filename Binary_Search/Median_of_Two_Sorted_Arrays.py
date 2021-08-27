# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/23
# Description: Leetcode 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthSortedArrays(nums1: List[int], nums2: List[int], k: float) -> int:
            k = int(k)  # divide operator return float -> int
            while k > 0:
                #  bound
                if len(nums1) == 0:
                    return nums2[k - 1]
                if len(nums2) == 0:
                    return nums1[k - 1]
                #  normal
                if k == 1:
                    return min(nums1[0], nums2[0])
                else:
                    if nums1[min(k // 2, len(nums1)) - 1] <= nums2[min(k // 2, len(nums2)) - 1]:
                        l = len(nums1)
                        nums1 = nums1[k // 2:]
                    else:
                        l = len(nums2)
                        nums2 = nums2[k // 2:]
                    k = k - min(k // 2, l)

        lens = len(nums1) + len(nums2)
        if lens % 2 == 0:
            a = findKthSortedArrays(nums1, nums2, lens / 2)
            b = findKthSortedArrays(nums1, nums2, lens / 2 + 1)
            return (a + b) / 2
        else:
            return findKthSortedArrays(nums1, nums2, (lens + 1) / 2)
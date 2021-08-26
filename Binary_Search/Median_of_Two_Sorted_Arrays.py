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

# Input: nums1 = [1,3,5], nums2 = [2,4]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthSortedArrays(nums1: List[int], nums2: List[int], k) -> int:
            k = int(k)
            n, m = len(nums1), len(nums2)
            assert 1 <= k <= n + m
            if n == 0:
                return nums2[k - 1]
            elif m == 0:
                return nums1[k - 1]
            elif n == m == 1:
                if k == 1:
                    return min(nums1 + nums2)
                else:
                    return max(nums1 + nums2)
            elif n < m:
                nums1, nums2 = nums2, nums1
                n, m = m, n
            pointer1 = (k - 1) // 2
            pointer2 = k - 2 - pointer1
            while True:
                flag1 = True
                flag2 = True
                if pointer2 < 0:
                    return nums1[pointer1]
                elif pointer1 < 0:
                    return nums2[pointer2]
                if pointer1 + 1 >= n:
                    flag1 = False
                if pointer2 + 1 >= m:
                    flag2 = False
                if pointer2 >= m:
                    pointer2 = (pointer2 - 1) // 2
                    pointer1 = k - 2 - pointer2
                elif pointer1 >= n:
                    pointer1 = (pointer1 - 1) // 2
                    pointer2 = k - 2 - pointer1
                elif flag1 and nums1[pointer1 + 1] < nums2[pointer2]:
                    pointer2 = min((pointer2) // 2, pointer2 - 1)
                    pointer1 = k - 2 - pointer2
                elif flag2 and nums1[pointer1] > nums2[pointer2 + 1]:
                    pointer1 = min((pointer1) // 2, pointer1 - 1)
                    pointer2 = k - 2 - pointer1
                else:
                    return max(nums1[pointer1], nums2[pointer2])

        lens = len(nums1) + len(nums2)
        if lens % 2 == 0:
            a = findKthSortedArrays(nums1, nums2, lens / 2)
            b = findKthSortedArrays(nums1, nums2, lens / 2 + 1)
            return (a + b) / 2
        else:
            return findKthSortedArrays(nums1, nums2, (lens + 1) / 2)


def findKthSortedArrays(nums1: List[int], nums2: List[int], k) -> int:
    n, m = len(nums1), len(nums2)
    assert 1 <= k <= n + m
    if n == 0:
        return nums2[k - 1]
    elif m == 0:
        return nums1[k - 1]
    elif n == m == 1:
        if k == 1:
            return min(nums1 + nums2)
        else:
            return max(nums1 + nums2)
    elif n < m:
        nums1, nums2 = nums2, nums1
        n, m = m, n
    pointer1 = (k - 1) // 2
    pointer2 = k - 2 - pointer1
    while True:
        flag1 = True
        flag2 = True
        if pointer2 < 0:
            return nums1[pointer1]
        elif pointer1 < 0:
            return nums2[pointer2]
        if pointer1 + 1 >= n:
            flag1 = False
        if pointer2 + 1 >= m:
            flag2 = False
        if pointer2 >= m:
            pointer2 = (pointer2 - 1) // 2
            pointer1 = k - 2 - pointer2
        elif pointer1 >= n:
            pointer1 = (pointer1 - 1) // 2
            pointer2 = k - 2 - pointer1
        elif flag1 and nums1[pointer1 + 1] < nums2[pointer2]:
            pointer2 = (pointer2) // 2
            pointer1 = k - 2 - pointer2
        elif flag2 and nums1[pointer1] > nums2[pointer2 + 1]:
            pointer1 = (pointer1) // 2
            pointer2 = k - 2 - pointer1
        else:
            return max(nums1[pointer1], nums2[pointer2])


nums1 = [1, 2, 3]
nums2 = [4, 5, 6, 7, 8]
k = 5
print(findKthSortedArrays(nums1, nums2, k))

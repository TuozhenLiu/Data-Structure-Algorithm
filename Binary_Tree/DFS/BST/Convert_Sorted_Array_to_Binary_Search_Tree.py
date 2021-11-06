# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/6
# Description: Leetcode 108. Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildaTree(left, right):
            if left > right:
                return None  # 左闭右闭的区间，当区间 left > right的时候，就是空节点,当left = right的时候，不为空
            mid = left + (right - left) // 2  # 保证数据不会越界
            val = nums[mid]
            root = TreeNode(val)
            root.left = buildaTree(left, mid - 1)
            root.right = buildaTree(mid + 1, right)
            return root

        root = buildaTree(0, len(nums) - 1)  # 左闭右闭区间
        return root

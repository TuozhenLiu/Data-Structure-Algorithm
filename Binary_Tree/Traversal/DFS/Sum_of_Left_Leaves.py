# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/5
# Description: Leetcode 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:
# Input: root = [1]
# Output: 0

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
# ----------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        Sum = 0
        if root.left:
            if not root.left.left and not root.left.right:
                Sum += root.left.val
            else:
                Sum += self.sumOfLeftLeaves(root.left)
        if root.right:
            Sum += self.sumOfLeftLeaves(root.right)
        return Sum
    # time complexity: O(N)
    # space complexity: O(N)

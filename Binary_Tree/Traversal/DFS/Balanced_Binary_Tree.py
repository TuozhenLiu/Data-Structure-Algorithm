# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/4
# Description: Leetcode 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
# ----------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_depth(node: TreeNode) -> int:
            if not node:
                return 0
            leftDepth = get_depth(node.left)
            if leftDepth == -1:
                return -1
            rightDepth = get_depth(node.right)
            if rightDepth == -1:
                return -1
            if abs(leftDepth - rightDepth) > 1:
                return -1
            else:
                return max(leftDepth, rightDepth) + 1
        if get_depth(root) == -1:
            return False
        else:
            return True
    # time complexity: O(N)
    # space complexity: O(N)

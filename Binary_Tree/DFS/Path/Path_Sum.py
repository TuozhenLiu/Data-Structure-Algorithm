# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/5
# Description: Leetcode 112. Path Sum

# Given the root of a binary tree and an integer targetSum, return true
# if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false

# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
# ----------------------------------------------------------------------------------------------------------------------
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        path = []
        global result
        result = False

        def get_path(node):
            path.append(node.val)
            if node.left:
                get_path(node.left)
                path.pop()
            if node.right:
                get_path(node.right)
                path.pop()
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    global result
                    result = True

        get_path(root)
        return result


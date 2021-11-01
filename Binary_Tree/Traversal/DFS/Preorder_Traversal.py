# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/9
# Description: Leetcode 144. Binary Tree Preorder Traversal

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
# Input: root = [1,2]
# Output: [1,2]

# Example 5:
# Input: root = [1,null,2]
# Output: [1,2]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?
# ----------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def Traversal(root: TreeNode):
            if root:
                result.append(root.val)
                Traversal(root.left)
                Traversal(root.right)

        Traversal(root)
        return result
    # time complexity: O(N)
    # space complexity: O(N) stack: avg O(logN), worst O(N)

    # iterative
    def preorderTraversal_2(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

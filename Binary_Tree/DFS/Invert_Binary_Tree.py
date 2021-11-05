# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/1
# Description: Leetcode 

# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# ----------------------------------------------------------------------------------------------------------------------
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS recursive 前序(中、后也可)
    def invertTree(self, root: TreeNode) -> TreeNode:
        def Traversal(node):
            if node:
                node.left, node.right = node.right, node.left
                Traversal(node.left)
                Traversal(node.right)
        Traversal(root)
        return root
    # time complexity: O(N)
    # space complexity: O(N)

    # BFS
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

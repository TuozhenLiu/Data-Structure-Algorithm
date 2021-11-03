# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/1
# Description: Leetcode 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Example 3:
# Input: root = []
# Output: 0

# Example 4:
# Input: root = [0]
# Output: 1
# ----------------------------------------------------------------------------------------------------------------------
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
    # time complexity: O(N)
    # space complexity: O(N)

    # DFS
    def maxDepth2(self, root: TreeNode) -> int:
        def get_max_depth(node: TreeNode) -> int:
            if not node:
                return 0
            else:
                return max(get_max_depth(node.left), get_max_depth(node.right)) + 1
        return get_max_depth(root)

    # time complexity: O(N)
    # space complexity: O(H) 平均情况下树的高度与节点数的对数正相关，空间复杂度为O(logN)。


# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/1
# Description: Leetcode 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# Constraints:
# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
    # time complexity: O(N)
    # space complexity: O(N)

    # DFS
    def minDepth2(self, root: TreeNode) -> int:
        def get_min_depth(node: TreeNode) -> int:
            if not node:
                return 0
            elif not node.left:
                return get_min_depth(node.right) + 1
            elif not node.right:
                return get_min_depth(node.left) + 1
            else:
                return min(get_min_depth(node.left), get_min_depth(node.right)) + 1
        return get_min_depth(root)
    # time complexity: O(N)
    # space complexity: O(N)

# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/1
# Description: Leetcode 515. Find Largest Value in Each Tree Row

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:
# Input: root = [1,2,3]
# Output: [1,3]

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
# Input: root = [1,null,2]
# Output: [1,2]

# Example 5:
# Input: root = []
# Output: []

# Constraints
# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1
# ----------------------------------------------------------------------------------------------------------------------
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            in_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                in_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max(in_list))
        return result
    # time complexity: O(N)
    # space complexity: O(N)

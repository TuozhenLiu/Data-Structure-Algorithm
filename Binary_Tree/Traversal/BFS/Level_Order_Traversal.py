# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/10/31
# Description: Leetcode 102. Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# ----------------------------------------------------------------------------------------------------------------------
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 广度优先搜索
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        Queue = deque([root])
        out_list = []
        while Queue:
            in_list = []
            for _ in range(len(Queue)):
                node = Queue.popleft()
                if node.left:
                    Queue.append(node.left)
                if node.right:
                    Queue.append(node.right)
                in_list.append(node.val)
            out_list.append(in_list)
        return out_list
    # time complexity: O(N)
    # space complexity: O(N)

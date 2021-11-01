# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/1
# Description: Leetcode 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
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
    # DFS: 记录深度位置
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = dict()
        stack = []
        cur, deep = root, 0
        while cur or stack:
            if cur:
                stack.append((cur, deep))
                cur = cur.right
                deep += 1
            else:
                cur, deep = stack.pop()
                if deep not in result.keys():
                    result[deep] = cur.val
                cur, deep = cur.left, deep + 1
        return [result[i] for i in range(len(result))]  # [v for k, v in sorted(result.items())] 排序慢
    # time complexity: O(N)
    # space complexity: O(N)

    # BFS:
    def rightSideView2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == l-1:
                    result.append(node.val)
        return result

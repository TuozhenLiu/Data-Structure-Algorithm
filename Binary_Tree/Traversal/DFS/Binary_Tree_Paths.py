# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/5
# Description: Leetcode 257. Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
# ----------------------------------------------------------------------------------------------------------------------
from typing import List
from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归 深拷贝path
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        results = []

        def get_path(node, path):
            path.append(str(node.val))
            if node.left:
                get_path(node.left, deepcopy(path))
            if node.right:
                get_path(node.right, deepcopy(path))
            if not node.left and not node.right:
                results.append(path)

        get_path(root, [])
        return list(map(lambda x: "->".join(x), results))
    # time complexity: O(N^2)
    # space complexity: O(N^2)

    # 回朔 维护一个path
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        results = []
        path = []

        def get_path(node):
            path.append(str(node.val))
            if node.left:
                get_path(node.left)
                path.pop()
            if node.right:
                get_path(node.right)
                path.pop()
            if not node.left and not node.right:
                results.append("->".join(path))

        get_path(root)
        return results

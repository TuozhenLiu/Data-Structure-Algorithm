# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/5
# Description: Leetcode 501. Find Mode in Binary Search Tree

# Given the root of a binary search tree (BST) with duplicates,
# return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]

# Example 2:
# Input: root = [0]
# Output: [0]

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

# Follow up: Could you do that without using any extra space?
# (Assume that the implicit stack space incurred due to recursion does not count).
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        cur = root
        val = None
        count = 0
        max_count = 1
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                # 中序遍历判断
                if cur.val == val:
                    count += 1
                else:
                    if count > max_count:
                        result = [val]
                        max_count = count
                    elif count == max_count:
                        result.append(val)
                    count = 1
                    val = cur.val
                # 中序遍历判断
                cur = cur.right
        # 退出循环补一次判断
        if count > max_count:
            result = [val]
        if count == max_count:
            result.append(val)
        return result


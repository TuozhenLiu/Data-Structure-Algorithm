# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/5
# Description: Leetcode 530. Minimum Absolute Difference in BST

# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105

# Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# ----------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 中序遍历，双指针
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')
        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else:  # 逐一处理节点
                cur = stack.pop()
                if pre:  # 当前节点和前节点的值的差值
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return result

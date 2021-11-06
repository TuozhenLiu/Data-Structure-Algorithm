# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/5
# Description: Leetcode 98. Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
# ----------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_bst(node: TreeNode, upper=float("Inf"), lower=-float("Inf")):
            if not node:
                return True
            if lower < node.val < upper:
                return is_bst(node.left, node.val, lower) and is_bst(node.right, upper, node.val)
            else:
                return False
        return is_bst(root)

    # 中序遍历，双指针
    def isValidBST2(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre and cur.val <= pre.val: # 比较当前节点和前节点的值的大小
                    return False
                pre = cur
                cur = cur.right
        return True

# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/5
# Description: Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
# inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        if not preorder:
            return None
        # 第二步: 前序遍历的第一个就是当前的中间节点.
        root_val = preorder[0]
        root = TreeNode(root_val)
        # 第三步: 找切割点.
        separator_idx = inorder.index(root_val)
        # 第四步: 切割中序数组.
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]
        # 第五步: 切割前序数组.（切割点相同，右节点相同）
        preorder_left = preorder[1:separator_idx + 1]
        preorder_right = preorder[separator_idx + 1:]
        # 第六步: 递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

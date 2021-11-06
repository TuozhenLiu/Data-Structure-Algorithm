# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/6
# Description: Leetcode 701. Insert into a Binary Search Tree

# You are given the root node of a binary search tree (BST) and a value to insert into the tree.
# Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion,
# as long as the tree remains a BST after insertion. You can return any of them.

# Example 1:
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

# Example 3:
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.
# ----------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recrusive
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root
    # time complexity: O(N)
    # space complexity: O(1)

    # iteration
    def insertIntoBST2(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = None
        cur = root

        # 用while循环不断地找新节点的parent
        while cur:
            if cur.val < val:
                parent = cur
                cur = cur.right
            elif cur.val > val:
                parent = cur
                cur = cur.left

        # 运行到这意味着已经跳出上面的while循环,
        # 同时意味着新节点的parent已经被找到.
        # parent已被找到, 新节点已经ready. 把两个节点黏在一起就好了.
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root

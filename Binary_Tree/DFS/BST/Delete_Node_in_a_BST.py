# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/6
# Description: Leetcode 450. Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.

# Example 3:
# Input: root = [], key = 0
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105

# Follow up: Could you solve it with time complexity O(height of tree)?
# ----------------------------------------------------------------------------------------------------------------------
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root  # 第一种情况：没找到删除的节点，遍历到空节点直接返回了
        if root.val == key:
            if not root.left and not root.right:  # 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
                root = None
            elif not root.left and root.right:  # 第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
                root = root.right
            elif root.left and not root.right:  # 第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
                root = root.left
            else:  # 第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
                v = root.right
                while v.left:
                    v = v.left
                else:
                    v.left = root.left
                root = root.right
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)  # 左递归
        if root.val < key:
            root.right = self.deleteNode(root.right, key)  # 右递归
        return root

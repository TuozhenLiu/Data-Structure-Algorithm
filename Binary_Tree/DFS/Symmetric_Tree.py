# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/3
# Description: Leetcode 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# Follow up: Could you solve it both recursively and iteratively?
# ----------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return None

        def compare(left_tree: TreeNode, right_tree: TreeNode) -> bool:
            if not left_tree and not right_tree:
                return True
            elif not left_tree or not right_tree:
                return False
            elif left_tree.val != right_tree.val:
                return False
            else:
                return compare(left_tree.left, right_tree.right) and compare(left_tree.right, right_tree.left)

        return compare(root.left, root.right)
    # time complexity: O(N)
    # space complexity: O(N)


# queue 和 stack 甚至 list 也可以，本质就是拿一个容器存放我们要比较的元素，与递归法使用相同的比较条件
# import collections
#
#
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         queue = collections.deque()
#         queue.append(root.left)  # 将左子树头结点加入队列
#         queue.append(root.right)  # 将右子树头结点加入队列
#         while queue:  # 接下来就要判断这这两个树是否相互翻转
#             leftNode = queue.popleft()
#             rightNode = queue.popleft()
#             if not leftNode and not rightNode:  # 左节点为空、右节点为空，此时说明是对称的
#                 continue
#
#             # 左右一个节点不为空，或者都不为空但数值不相同，返回false
#             if not leftNode or not rightNode or leftNode.val != rightNode.val:
#                 return False
#             queue.append(leftNode.left)  # 加入左节点左孩子
#             queue.append(rightNode.right)  # 加入右节点右孩子
#             queue.append(leftNode.right)  # 加入左节点右孩子
#             queue.append(rightNode.left)  # 加入右节点左孩子
#         return True

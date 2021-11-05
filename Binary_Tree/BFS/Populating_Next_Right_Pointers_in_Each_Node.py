# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/1
# Description: Leetcode 116. Populating Next Right Pointers in Each Node

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A),
# your function should populate each next pointer to point to its next right node, just like in Figure B.
# The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000

# Follow-up:
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
# ----------------------------------------------------------------------------------------------------------------------
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if i != l - 1:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
    # time complexity: O(N)
    # space complexity: O(N)

    # 不用queue
    def connect2(self, root: 'Node') -> 'Node':
        first = root
        while first:
            cur = first
            while cur:  # 遍历每一层的节点
                if cur.left:
                    cur.left.next = cur.right  # 找左节点的next
                if cur.right and cur.next:
                    cur.right.next = cur.next.left  # 找右节点的next
                cur = cur.next  # cur同层移动到下一节点
            first = first.left  # 因为是完美二叉树，从本层直接到下一层
        return root
    # time complexity: O(N)
    # space complexity: O(1)

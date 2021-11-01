# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/1
# Description: Leetcode 429. N-ary Tree Level Order Traversal

# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

# Constraints:
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 104]
# ----------------------------------------------------------------------------------------------------------------------
from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # BFS
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            in_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                in_list.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(in_list)
        return result

    # time complexity: O(N)
    # space complexity: O(N)

    # DFS(stack)
    def levelOrder2(self, root: 'Node') -> List[List[int]]:
        result = []

        def traverse_node(node, deep):
            if len(result) == deep:
                result.append([])
            result[deep].append(node.val)
            for children in node.children:
                traverse_node(children, deep+1)

        if root is not None:
            traverse_node(root, 0)
        return result

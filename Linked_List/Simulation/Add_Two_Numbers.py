# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/7
# Description: Leetcode 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
# ----------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # p2比p1慢一步
        p1 = ListNode(0, l1)
        p2 = l2
        while p1 or p2:
            # 如果有p1，以p1为基础
            if p1.next:
                # 有p2 做加法
                if p2:
                    p1.next.val += p2.val
                # 进位
                if p1.next.val >= 10:
                    p1.next.val -= 10
                    if p1.next.next:
                        p1.next.next.val += 1
                    else:
                        p1.next.next = ListNode(1)
                p1 = p1.next
                if p2:
                    p2 = p2.next
            # 以p2为准
            else:
                p1.next = p2
                break
        return l1
# time complexity: O(N)
# space complexity: O(1)

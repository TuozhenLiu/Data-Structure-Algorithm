# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/8/29
# Description: Leetcode 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# ----------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next=head)
        slow_p = fast_p = dummy_head
        for i in range(n):  # del Nth: fast_p lead slow_p N position
            fast_p = fast_p.next
        while fast_p.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next
        slow_p.next = slow_p.next.next
        return dummy_head.next
# time complexity: O(N)
# space complexity: O(1)

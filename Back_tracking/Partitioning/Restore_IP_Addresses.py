# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/11/22
# Description: Leetcode 93. Restore IP Addresses

# A valid IP address consists of exactly four integers separated by single dots.
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
# but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits,
# return all possible valid IP addresses that can be formed by inserting dots into s.
# You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]

# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]

# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

# Constraints:
# 0 <= s.length <= 20
# s consists of digits only.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def backtracking(s, start_id):
            if len(path) == 4:
                if start_id == len(s):
                    res.append(".".join(path))
                return  # 如果已经分割了四个，但还有剩余数字，也直接return，不再往后搜索。
            if s[start_id] == "0":
                end_index = min(len(s) - (4 - len(path) - 1), start_id + 1)  # 剪枝：避免凑不够四个path
            else:
                end_index = min(len(s) - (4 - len(path) - 1), start_id + 3)  # 剪枝：避免凑不够四个path
            for i in range(start_id, end_index):
                if int(s[start_id: i + 1]) <= 255:
                    path.append(s[start_id: i + 1])
                    backtracking(s, i + 1)
                    path.pop()

        backtracking(s, 0)
        return res

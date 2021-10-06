# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author: Tuozhen
# Date: 2021/9/5
# Description: Leetcode

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates).
# You may return the answer in any order.

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # init hash_table by Inf
        hash_table = [float("Inf")] * 26

        for word in words:
            # init hash_cache by 0
            hash_cache = [0] * 26
            for char in word:
                hash_cache[ord(char) - ord("a")] += 1
            # min: make sure all words common
            for i in range(26):
                hash_table[i] = min(hash_table[i], hash_cache[i])
        result = []
        for i, _ in range(26):
            result.extend([chr(i + ord("a"))] * int(hash_table[i]))

        return result
# Denote N: len(words), M: average len(word) ∣Σ∣: len(vocab) 26
# 遍历所有字符串并计算 hash_cache 的时间复杂度为O(MN)
# 使用 hash_cache 更新 hash_table 的时间复杂度为 O(N∣Σ∣)；
# 由于最终答案包含的字符个数不会超过最短的字符串长度，因此构造最终答案的时间复杂度为O(m+∣Σ∣)，这一项在渐进意义上小于前二者，可以忽略。
# time complexity: O(N(M+∣Σ∣))
# space complexity: O(∣Σ∣)

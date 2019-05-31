_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/stickers-to-spell-word/
# We are given N different types of stickers. Each sticker has a lowercase English word on it.
# You would like to spell out the given target string by cutting individual letters from your collection of stickers
# and rearranging them.
# You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
# What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

# Remove chars from each sticker that are not in target and create mapping from char to set of stickers containing
# that char. Return -1 if every char of target is not contained in at least one sticker.
# Maintain a heap of candidate solutions. Pop item from heap with lowest used stickers, breaking ties by lowest
# remaining target length. For each sticker that contains the first remaining letter of target, remove all usable
# chars from target and add remaining target back to heap.
# Space - O(n * k**2) where n is number of sickers and k is length of target. If target is a string of the same char
# repeated and every sticker is that char, then every sticker will be used for every char of target.
# Time - O(nk log(nk) * k * s**2) every item in heap created by taking every char of sticker, testing for char in
# target, then remving from sticker.

import heapq
from collections import defaultdict

class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        target_set, remaining_target = set(target), set(target)
        char_to_word = defaultdict(set)  # map char to set of words, where each word is a tuple of cleaned chars

        for sticker in stickers:
            cleaned = tuple(x for x in sticker if x in target_set)  # remove chars that are not in target
            sticker_set = set(cleaned)
            for c in sticker_set:
                char_to_word[c].add(cleaned)
            remaining_target -= sticker_set

        if remaining_target:
            return -1

        heap = [(0, len(target), list(target))]  # using a list for target allows remove

        while True:

            used_words, target_len, target_str = heapq.heappop(heap)  # try least used words, then shortest target

            for sticker in char_to_word[target_str[0]]:  # each word that contains first char of target
                new_str = target_str[:]
                for ch in sticker:
                    if ch in new_str:
                        new_str.remove(ch)
                if not new_str:
                    return used_words + 1
                heapq.heappush(heap, (used_words + 1, len(new_str), new_str))
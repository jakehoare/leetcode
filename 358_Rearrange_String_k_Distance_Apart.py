_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rearrange-string-k-distance-apart/
# Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least
# distance k from each other.  All input strings are given in lowercase letters. If it is not possible to rearrange
# the string, return an empty string

# Count the frequency of each letter.  Greedily add the most frequent letter to the result if it has not been used
# in the last k letters.  Keep a heap of remaining frequency of each letter.  Remove most frequent until letter can be
# used, decrement remaining count and add back most frequent.
# Time - O(n log k)
# Space - O(n)

from collections import Counter
import heapq

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = Counter(s)
        heap = [(-count, letter) for letter, count in freq.items()]
        heapq.heapify(heap)

        last_used = {}      # map from letter to index in result of last use
        rearranged = []

        while heap:
            too_close = []          # save most frequent letters that cannot be used
            neg_f, letter = heapq.heappop(heap)

            while letter in last_used and len(rearranged) - last_used[letter] < k:  # keep letter to add back later
                too_close.append((neg_f, letter))
                if not heap:    # no more letters can be used
                    return ""
                neg_f, letter = heapq.heappop(heap)

            last_used[letter] = len(rearranged)
            rearranged.append(letter)
            neg_f += 1
            if neg_f:               # do not put back in heap if freq is zero
                heapq.heappush(heap, (neg_f, letter))

            for item in too_close:  # add back to heap
                heapq.heappush(heap, item)

        return "".join(rearranged)

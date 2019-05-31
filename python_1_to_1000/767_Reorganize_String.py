_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reorganize-string/
# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other
# are not the same. If possible, output any possible result. If not possible, return the empty string.

# Create heap of letter frequencies. Pop the most frequent letter off the heap and append to result if is different
# from the previous letter and add back to heap with decremented count. Else this is the only letter, no solution is
# possible. Else use the next most frequent letter then add the most frequent letter back.
# Time - O(n log k) where len(S) == n and k is the size of the alphabet.
# Space - O(n)

import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        freq = Counter(S)
        if any(count > (len(S) + 1) // 2 for count in freq.values()):   # some letter is too frequent
            return ""

        heap = [(-count, letter) for letter, count in freq.items()]     # max heap of count
        heapq.heapify(heap)

        result = []

        def add_letter(letter, neg_count):
            result.append(letter)
            neg_count += 1
            if neg_count != 0:                                          # remove from hep if no remaining count
                heapq.heappush(heap, (neg_count, letter))

        while heap:

            neg_count, letter = heapq.heappop(heap)

            if not result or result[-1] != letter:
                add_letter(letter, neg_count)
                continue

            if not heap:                                                # no other letters on heap
                return ""

            neg_count2, letter2 = heapq.heappop(heap)                   # use next most frequent letter
            add_letter(letter2, neg_count2)
            heapq.heappush(heap, (neg_count, letter))                   # add back most frequent with same count

        return "".join(result)
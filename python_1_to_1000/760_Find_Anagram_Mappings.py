_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-anagram-mappings/
# Given two lists on integers A and B where B is an anagram of A.
# We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
# These lists A and B may contain duplicates. If there are multiple answers, output any of them.

# Create a mapping from integers in b to their indices in b. If an integer is duplicated then the mapping if to the
# last index. For each num in a, look up its index in the mapping of indices in b.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        B_to_int = {}
        for i, b in enumerate(B):
            B_to_int[b] = i

        result = []
        for a in A:
            result.append(B_to_int[a])

        return result
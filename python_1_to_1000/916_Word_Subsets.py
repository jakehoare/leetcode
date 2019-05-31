_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-subsets/
# We are given two arrays A and B of words.  Each word is a string of lowercase letters.
# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.
# For example, "wrr" is a subset of "warrior", but is not a subset of "world".
# Now say a word a from A is universal if for every b in B, b is a subset of a.
# Return a list of all universal words in A.  You can return the words in any order.

# Find the maximum required number of each letter for all words in B.
# Check each word in A to see if it has at least the required number of each letter in B.
# Time - O(m + n), total length of all words in A and B
# Space - O(1) since dictionary keys are limited by the number of distinct letters

from collections import Counter, defaultdict

class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        required = defaultdict(int)  # map of each required letter in B to its required count

        for b in B:
            freq = Counter(b)
            for letter, count in freq.items():
                required[letter] = max(required[letter], count)

        results = []
        for a in A:

            freq = Counter(a)
            if all(freq[letter] >= count for letter, count in required.items()):
                results.append(a)

        return results

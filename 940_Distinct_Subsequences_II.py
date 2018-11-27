_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distinct-subsequences-ii/
# Given a string S, count the number of distinct, non-empty subsequences of S.
# Since the result may be large, return the answer modulo 10^9 + 7.

# Create a mapping from each char to the count of subsequences that have been extended by the char.
# For each char, we can extend all existing subsequences apart from those previously extended by the same char.
# Also update the mapping for the number of subsequences that have been extended by the char.
# Time - O(n)
# Space - O(1)

from collections import defaultdict

class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        total = 1                   # start with the empty subsequence
        extended = defaultdict(int) # map char to number of subsequences before last using this char

        for c in S:
            total, extended[c] = 2 * total - extended[c], total

        total -= 1                  # remove empty subsequence
        return total % (10 ** 9 + 7)

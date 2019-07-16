_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
# Given a string S, return the number of substrings of length K with no repeated characters.

# Maintain a sliding window of length K over S.
# Count the instances of all chars in the window.
# Increment the count for each new char and decrement for chars leaving the window.
# Maintain a count of repeated chars, to avoid checking all chars for every iteration.
# Time - O(n)
# Space - O(1) for fixed size alphabet.

from collections import defaultdict

class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        if K > 26 or K > len(S):        # must have repeats if more than alphabet size
            return 0

        counts = defaultdict(int)
        repeated, result = 0, 0

        for i, c in enumerate(S):
            counts[c] += 1
            if counts[c] == 2:          # new repeated char
                repeated += 1
            if i >= K:
                counts[S[i - K]] -= 1
                if counts[S[i - K]] == 1:
                    repeated -= 1

            if i >= K - 1:              # from i = K - 1 onwards
                result += repeated == 0 # increment result if no repeated

        return result

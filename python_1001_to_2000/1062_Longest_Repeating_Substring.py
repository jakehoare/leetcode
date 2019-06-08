_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-repeating-substring/
# Given a string S, find out the length of the longest repeating substring(s).
# Return 0 if no repeating substring exists.

# Binary search the range of possible lengths of repeated substring.
# Helper function checks all substrings of a given length.
# Alternatively, for a pair of strings of the same length we can check if there is a repeated substring starting and
# ending at the same indices in O(n) time. Compare S against itself with an offset for all possible offsets.
# Time - O(n**2 log n)
# Space - O(n**2)

class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        def helper(guess):
            seen = set()
            for i in range(n - guess + 1):
                substring = S[i:i + guess]
                if substring in seen:
                    return True
                seen.add(substring)
            return False

        n = len(S)
        low, high = 0, n

        while low <= high:              # until low > high
            mid = (low + high) // 2
            if helper(mid):
                low = mid + 1
            else:
                high = mid - 1

        return low - 1

class Solution2(object):
    def longestRepeatingSubstring(self, S):
        n = len(S)
        result = 0

        for offset in range(1, n):      # compare S[:-i] to S[i:]
            if result >= n - offset:
                break

            sequence = 0
            for i in range(n - offset):
                if S[i] == S[i + offset]:
                    sequence += 1
                    result = max(result, sequence)
                else:
                    sequence = 0

        return result

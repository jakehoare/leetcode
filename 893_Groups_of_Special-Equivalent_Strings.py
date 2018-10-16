_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/groups-of-special-equivalent-strings/
# You are given an array A of strings.
# Two strings S and T are special-equivalent if after any number of moves, S == T.
# A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].
# Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is
# not special-equivalent with any string in S.
# Return the number of groups of special-equivalent strings from A.

# For each string create a canonical representation, which is the same for special-equivalent strings.
# Strings are special-equivalent if their chars at even indices can be arranged to be identical and their chars at
# odd indices can be arranged to be identical.
# The representation is the sorted chars at even indices concatenated to the sorted chars at odd indices.
# Create a set of the unique representations.
# Time - O(n), total length of all strings
# Space - O(n)

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def canonical(s):
            evens = sorted([s[i] for i in range(0, len(s), 2)])
            odds = sorted([s[i] for i in range(1, len(s), 2)])
            return "".join(evens + odds)

        return len({canonical(s) for s in A})
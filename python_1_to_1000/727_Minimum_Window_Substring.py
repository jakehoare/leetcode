_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-window-subsequence/
# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
# If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple
# such minimum-length windows, return the one with the left-most starting index.

# Find all indices in S matching the first letter of T and create a list of windows. For each letter of T, for each
# window find the next letter of S that matches the letter and extend the window. If the letter is not found, remove
# the window. Return the smallest window.
# Time - O(mn), worst case when all letters are identical means len(S) windows
# Space - O(m)

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        next_in_s = [None for _ in range(len(S))]   # next_in_s[i][j] is the next occurrence of letter j in S[i + 1:]
        next_by_letter = [-1 for _ in range(26)]    # or -1 if not found
        for i in range(len(S) - 1, -1, -1):
            next_in_s[i] = next_by_letter[:]
            next_by_letter[ord(S[i]) - ord("a")] = i

        # matches is a list of windows [i, j] where i is the index in S matching the first char of T
        # and j is the index matching the current char of T
        matches = [[i, i] for i, c in enumerate(S) if c == T[0]]
        if not matches:
            return ""

        for i, c in enumerate(T[1:], 1):        # iterate over T

            new_matches = []

            for s_start, s_last in matches:     # for each window
                s_next = next_in_s[s_last][ord(c) - ord("a")]   # find the next index in S matching c
                if s_next != -1:
                    new_matches.append([s_start, s_next])       # update matches if c is found

            if not new_matches:
                return ""
            matches = new_matches

        # return the shortest window
        start, end = min(matches, key = lambda i, j: j - i)
        return S[start:end + 1]
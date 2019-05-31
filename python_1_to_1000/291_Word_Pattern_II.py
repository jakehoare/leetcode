_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-pattern-ii/
# Given a pattern and a string str, find if str follows the same pattern.
# Follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
# Each letter in pattern maps to a substring of str e.g. pattern = "abab", str = "redblueredblue" should return true.
# You may assume both pattern and str contain only lowercase letters.

# For each character c in pattern, attempt to match this with test_s, a prefix of str.  If neither c nor the prefix
# have been used before, set this mapping and recurse.  Delete mapping if recursion does not match remainders.
# If c is already mapped to prefix, recurse. Invalid mapping if either c or test_s are mapped but not to each other.
# Time - O(m*n), for each char of pattern, try each prefix of str
# Space - O(n)

class Solution(object):

    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m, n = len(pattern), len(str)

        def is_match(i, j):

            if i >= m and j >= n:
                return True
            if i >= m:                              # no pattern but some str remains unmatched
                return False

            for end in range(j, n - (m - i) + 1):   # leave at least 1 char in str for each of remaining pattern

                p, test_s = pattern[i], str[j:end + 1]  # try to match test_s with p
                if p not in mapping and test_s not in s_used:   # neither p nor test_s are used
                    mapping[p] = test_s
                    s_used.add(test_s)
                    if is_match(i + 1, end + 1):
                        return True
                    del mapping[p]                  # revert mapping and s_used since failed
                    s_used.discard(test_s)

                elif p in mapping and mapping[p] == test_s:     # p already mapped to test_s
                    if is_match(i + 1, end + 1):
                        return True

            return False

        mapping = {}
        s_used = set()
        return is_match(0, 0)
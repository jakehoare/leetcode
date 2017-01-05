_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-pattern-ii/
# Given a pattern and a string str, find if str follows the same pattern.
# Follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
# You may assume both pattern and str contain only lowercase letters.

# For each character c in pattern, attempt to match this with test_s, a prefix of str.  If neither c nor the prefix
# have been used before, set this mapping and recurse.  Delete mapping if recursion does not match remainders.
# If c is already mapped to prefix, recurse.  Invalid mapping if either c or test_s are mapped but not to each other.
# Time - O(m*n), for each char of pattern, try each prefix of str
# Space - O(n)

class Solution(object):

    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.is_match(pattern, str, {}, set())

    def is_match(self, p, s, mapping, s_used):  # an alternative without s_used is mapping.values()

        if not p and not s:
            return True
        if not p:                               # no pattern but some str remains unmatched
            return False

        for end in range(len(s)-len(p)+1):      # leave at least 1 char in str for each of remaining pattern

            test_s = s[:end+1]                  # try to match test_s with pattern[0]
            if p[0] not in mapping and test_s not in s_used:    # neither p[0] nor test_s are used
                mapping[p[0]] = test_s
                s_used.add(test_s)
                if self.is_match(p[1:], s[end+1:], mapping, s_used):
                    return True
                del mapping[p[0]]       # delete mapping p[0] to test_s
                s_used.discard(test_s)

            elif p[0] in mapping and mapping[p[0]] == test_s:   # p[0] already mapped to test_s
                if self.is_match(p[1:], s[end+1:], mapping, s_used):
                    return True

        return False
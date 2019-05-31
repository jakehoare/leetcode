_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/implement-strstr/
# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# For each pssible starting point in haystack, check characters match with needle and breask if not.
# Alternatively KMP would improve expected time complexity.
# Time - O(n^2)
# Space - O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:           # for/else reaches here if no break
                return i
        return -1
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-palindrome/
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
# Find and return the shortest palindrome you can find by performing this transformation.

# Least number of characters added implies finding the longest prefix palindrome.  Use KMP failure function
# algorithm to find the longest prefix of s that is also a suffix of s[::-1].
# Time - O(n)
# Space - O(n)

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_prefix_suffix = self.kmp_table(s + '*' + s[::-1])
        return s[:longest_prefix_suffix:-1] + s


    def kmp_table(self, word):
        failure = [-1] + [0 for _ in range(len(word)-1)]
        pos = 2             # the next index of failure table to be computed
        candidate = 0

        while pos < len(word):

            if word[pos-1] == word[candidate]:  # prefix/suffix of word[:i] extends the previous prefix/suffix by 1 char
                failure[pos] = candidate + 1
                candidate += 1
                pos += 1
            elif candidate > 0:                 # no extension, update candidate to earlier prefix/suffix
                candidate = failure[candidate]
                failure[pos] = 0
            else:   # candidate == 0
                failure[pos] = 0
                pos += 1

        return failure[-1]
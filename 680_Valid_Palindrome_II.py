_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-palindrome-ii/
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Iterate over s from front and back. If chars do not match, check if the remainder after deleting either of the
# unmatched chars is a palindrome.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i = 0

        while i < n // 2:

            if s[i] != s[n - 1 - i]:
                del_front = s[i + 1:n - i]
                del_back = s[i:n - 1 - i]
                return del_front == del_front[::-1] or del_back == del_back[::-1]

            i += 1

        return True
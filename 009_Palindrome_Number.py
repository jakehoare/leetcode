_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. Do this without extra space.

# Check equivalence of first and last characters, moving inwards.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1

        return True
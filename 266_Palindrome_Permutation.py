_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-permutation/
# Given a string, determine if a permutation of the string could form a palindrome.

# There can be at most one character with an odd count in a palindrome.
# Time - O(n)
# Space - O(1)

from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = Counter(s)
        odd = False                 # no odd has been seen

        for letter, count in freq.items():
            if count % 2 == 1:
                if odd:             # amother char has odd count
                    return False
                odd = True

        return True
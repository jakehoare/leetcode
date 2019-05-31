_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-palindrome/
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that
# can be built with those letters. This is case sensitive, for example "Aa" is not considered a palindrome here.

# Iterate over s maintaining a set of letters seen. If a letter is seen again, add 2 to length of palindrome and
# delete from set. If a letter is not in set, add it. Add 1 for a single letter in the middle of the palindrome if
# there are any single letters after iteration.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        letters = set()

        for c in s:
            if c in letters:
                max_length += 2
                letters.remove(c)
            else:
                letters.add(c)

        return max_length + bool(letters)
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# For each centre point of a character or between 2 characters, expand the palindrome if the end characters are the same.
# Time - O(n^2), 2n centres, each expanded upto n times
# Space - O(n) to store the result

# Could return early by starting with the middle centre and ruling out later centres that could not have longer
# substring than the palindrome already found.

# Note that Manacher's algorithm provides a O(n) time solution.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for centre in range(2*len(s)-1):    # 2n-1 possible centres, each letter and between each pair

            if centre % 2 == 0:     # initialise 2 pointers at the ends of the substring to be checked
                left, right = (centre//2) - 1, (centre//2) + 1
            else:
                left, right = centre//2, (centre//2) + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now beyond the ends of the substring

            if right - left - 1 > len(longest):
                longest = s[left+1:right]

        return longest
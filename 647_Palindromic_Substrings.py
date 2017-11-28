_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindromic-substrings/
# Given a string, your task is to count how many palindromic substrings in this string. The substrings with different
# start indexes or end indexes are counted as different substrings even they consist of same characters.

# For each char or neighbouring pair of chars, extend outwards as long as left and right match.
# Time - O(n**2)
# Space - O(1)

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(2 * len(s) + 1):

            left = right = i // 2
            if i % 2 == 1:
                right += 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
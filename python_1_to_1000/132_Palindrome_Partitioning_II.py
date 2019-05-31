_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-partitioning-ii/
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# Initialise worst case for each prefix as length of prefix - 1.  For each character expand outwards both odd and even
# length palindromes.  Whenever a palindrome is found, update min_cuts for that palindrome plus the left prefix.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_cuts = [i-1 for i in range(len(s)+1)]       # min_cuts[i] is min cuts for prefix s[:i] of length i

        for i in range(len(s)):                         # for each character as centre of palindrome

            left, right = i, i                          # expand to find all odd-length palindromes
            while left >= 0 and right < len(s) and s[left] == s[right]:
                min_cuts[right + 1] = min(min_cuts[right + 1], 1 + min_cuts[left])
                left -= 1
                right += 1

            left, right = i, i+1                        # expand to find all even-length palindromes
            while left >= 0 and right < len(s) and s[left] == s[right]:
                min_cuts[right + 1] = min(min_cuts[right + 1], 1 + min_cuts[left])
                left -= 1
                right += 1

        return min_cuts[-1]

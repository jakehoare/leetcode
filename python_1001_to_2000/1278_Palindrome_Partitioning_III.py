_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-partitioning-iii/
# You are given a string s containing lowercase letters and an integer k. You need to :
# First, change some characters of s to other lowercase English letters.
# Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
# Return the minimal number of characters that you need to change to divide the string.

# Helper function returns the minimum chars to change to make k palindromes from a suffix of s.
# If the length of the suffix is the same as k, each char can be a palindrome and no changes are needed.
# If k == 1, the suffix must be changed to a single palindrome.
# Else convert the substring s[i:j + 1] to a palindrome and recurse for k - 1 remaining substrings.
# Time - O(n ** 3 * k) since O(nk) calls to helper, each with O(n) iterations over j, each taking O(n) for cost().
# Space - O(nk)

class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        def cost(left, right):      # cost to change s[i:j + 1] into a palindrome
            result = 0
            while left < right:
                if s[left] != s[right]:
                    result += 1
                left += 1
                right -= 1
            return result

        memo = {}

        def helper(i, k):           # chars to change s[i:] into k palindromes
            if k >= n - i:
                return 0
            if k == 1:
                return cost(i, n - 1)
            if (i, k) in memo:
                return memo[(i, k)]

            chars_changed = float("inf")
            for j in range(i, n - k + 1):   # until k - 1 == remaining string length
                chars_changed = min(chars_changed, cost(i, j) + helper(j + 1, k - 1))

            memo[(i, k)] = chars_changed
            return chars_changed

        return helper(0, k)

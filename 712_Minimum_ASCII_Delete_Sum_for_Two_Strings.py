_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

# Dynamic programming, similar to edit distance. Find the cost of equalising each prefix of s1 and prefix of s2.
# If either prefix is empty then all characters of the other prefix must be deleted. If the final chars of prefixes are
# equal then cost is same as for both prefixes without final chars. Else minumum cost of deleting a char from either
# prefix.
# Time - O(mn)
# Space - O(n)

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [0]        # for empty prefix of s1
        for c in s2:    # cost is all chars in prefix of s2
            dp.append(dp[-1] + ord(c))

        for i in range(len(s1)):

            new_dp = [dp[0] + ord(s1[i])]   # empty prefix of s2, cost is sum of chars in prefix of s1

            for j in range(len(s2)):
                if s1[i] == s2[j]:          # delete neither character
                    new_dp.append(dp[j])
                else:                       # delete either character
                    new_dp.append(min(ord(s1[i]) + dp[j + 1], ord(s2[j]) + new_dp[-1]))

            dp = new_dp

        return dp[-1]
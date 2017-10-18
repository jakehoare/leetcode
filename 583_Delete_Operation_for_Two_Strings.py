_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-operation-for-two-strings/
# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where
# in each step you can delete one character in either string.

# Retain the longest common subsequence of both words, after deleting all other characters. LCS is found by dynamic
# programming. If the final chars of a word are the same, LCS is 1 + the LCS of the words without their final chars.
# Else take the longest LCS after ignoring the final char from one word.
# Time - O(m * n)
# Space - O(n)

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def LCS(s, t):
            prev_dp = [0 for _ in range(len(word2) + 1)]

            for i in range(1, len(word1) + 1):  # length of word1 prefix
                dp = [0]

                for j in range(1, len(word2) + 1):  # length of word2 prefix
                    if word1[i - 1] == word2[j - 1]:
                        dp.append(1 + prev_dp[j - 1])
                    else:
                        dp.append(max(dp[-1], prev_dp[j]))

                prev_dp = dp

            return prev_dp[-1]

        return len(word1) + len(word2) - 2 * LCS(word1, word2)
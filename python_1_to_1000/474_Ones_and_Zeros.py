_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ones-and-zeroes/
# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with
# strings consisting of only 0s and 1s. Now your task is to find the maximum number of strings that you can form with
# given m 0s and n 1s. Each 0 and 1 can be used at most once.

# Dynamic programming. max_form[i][j] is the max number of strings that can be formed form i zeros and j ones.
# For each string, if i or j are insufficient cannot form string so keep max_form unchanged. If can form string, take
# max of incremented max_form and using s_zeros, s_ones, or same max_form and not using any zeros or ones.
# Time - O(mnk), where k = len(strs)
# Space - O(mn)

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        max_form = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:

            s_zeros = sum([True for c in s if c == "0"])
            s_ones = len(s) - s_zeros

            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= s_zeros and j >= s_ones:    # keep max_form[i][j] unchanged if insufficient 0s or 1s
                        max_form[i][j] = max(max_form[i][j], 1 + max_form[i - s_zeros][j - s_ones])

        return max_form[-1][-1]     # for all strs, max_form from m, n

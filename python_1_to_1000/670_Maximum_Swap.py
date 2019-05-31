_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-swap/
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you could get.

# Iterate backwards from the least to the most significant digit. When we have already seen a greater digit than the
# current digit they could be swapped and increase the value. Track the first occurrence of greatest digit seen.
# If the current digit is lower, we have a new candidate for swapping. If it is higher, we have a new max_seen.
# The last candidates found result in the greatest increase because they increase the most significant digit possible.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = [int(c) for c in str(num)]          # convert to list of digits

        max_seen, max_seen_i = -1, -1           # max digit seen (from back) and its index
        demote, promote = -1, -1                # indices of best pair to swap

        for i in range(len(s) - 1, -1, -1):     # iterate from least significant digit
            digit = s[i]
            if max_seen > digit:                # greater digit later in num so swap will increase value
                demote, promote = i, max_seen_i
            elif digit > max_seen:              # update max_seen on first occurrence of greater digit
                max_seen, max_seen_i = digit, i

        if demote == -1:                        # nothing can be swapped
            return num

        s[demote], s[promote] = s[promote], s[demote]
        result = 0
        for digit in s:
            result = result * 10 + digit
        return result
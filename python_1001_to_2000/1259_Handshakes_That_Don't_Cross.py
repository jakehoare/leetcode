_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/handshakes-that-dont-cross/
# You are given an even number of people num_people that stand around a circle and
# each person shakes hands with someone else, so that there are num_people / 2 handshakes total.
# Return the number of ways these handshakes could occur such that none of the handshakes cross.
# Since this number could be very big, return the answer mod 10^9 + 7

# Dynamic programming.
# For each even number of people, choose one arbitrary person and handshake with each other person so there is an
# even number of people on both sides of the handshake pair.
# Sum the results for each other person, which is the product of the results for the two groups on both sides
# of the handshaking pair.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        dp = [1]                # dp[i] is the result for i // 2 people

        for people in range(2, num_people + 1, 2):
            result = 0
            for left in range(0, people - 1, 2):    # number of people on the left of the handshake pair
                result += dp[left // 2] * dp[(people - left - 2) // 2]
            dp.append(result)

        return dp[-1] % (10 ** 9 + 7)

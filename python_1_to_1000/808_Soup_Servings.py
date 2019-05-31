_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/soup-servings/
# There are two types of soup: type A and type B. Initially we have N ml of each type of soup.
# There are four kinds of operations:
# Serve 100 ml of soup A and 0 ml of soup B
# Serve 75 ml of soup A and 25 ml of soup B
# Serve 50 ml of soup A and 50 ml of soup B
# Serve 25 ml of soup A and 75 ml of soup B
# When we serve some soup, we give it to someone and we no longer have it.
# Each turn, we will choose from the four operations with equal probability 0.25.
# If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.
# We stop once we no longer have some quantity of both types of soup.
# Note that we do not have the operation where all 100 ml's of soup B are used first.
# Return the probability that soup A will be empty first, plus half the probability that A and B become empty at
# the same time.
# Answers within 10^-6 of the true value will be accepted as correct.

# Convert the volume of soup to a number of portions. Given a number of portions of A and of B, recurse for each of the
# 4 possible operations, sum the results and divide by 4 to get the probability of A being empty first.
# Memoize results to avoid repetition. If N is large enough (4800 found experimentally) then the result is within
# 10**-6 of 1 so we simply return 1 to the avoid the time limit being exceeded.
# Time - O(1) due to the upper limit on N of 4800
# Space - O(1)

class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        memo = {}

        def helper(A, B):

            if A <= 0 and B <= 0:       # base case, both A and Bempty together
                return 0.5
            if A <= 0:                  # base case, only A empty
                return 1
            if B <= 0:                  # base case, only B empty
                return 0

            if (A, B) in memo:
                return memo[(A, B)]

            result = 0.25 * (helper(A - 4, B) + helper(A - 3, B - 1) + helper(A - 2, B - 2) + helper(A - 1, B - 3))
            memo[(A, B)] = result
            return result

        portions = math.ceil(N / float(25))
        if N > 4800:                    #
            return 1
        return helper(portions, portions)
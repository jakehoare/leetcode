_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# We are playing the Guess Game. The game is as follows:  I pick a number from 1 to n. You have to guess which
# number I picked.  Every time you guess wrong, I'll tell you whether the number I picked is higher or lower. However,
# when you guess a number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.
# Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

# Dynamic programming.  Min money for any range is the minimum cost after all possible next guesses.  Min cost of
# a particular guess is the guess + worst case of having to recurse on the range either above or below the guess.
# Best guess  is never in LHS of range since then the RHS is longer and has greater numbers so we always want LHS to be
# longer.
# Alternatively, top-down recursive.
# Time - O(n**3)
# Space - O(n**2)

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # min_money[i][j] is min money to guarantee win if search range length is i+1 starting from j+1
        # if length == 1, min_money = 0 since no guess required
        # if length == 2, min_money = lower value of range
        min_money = [[0 for _ in range(n)], [i for i in range(1, n)]]

        for range_length in range(3, n + 1):
            min_money.append([])
            for lower in range(1, n + 2 - range_length):
                upper = lower + range_length - 1
                min_cost = float('inf')
                for guess in range((lower + upper)  // 2, upper):   # guesses of LHS and upper are never optimal
                    cost = guess + max(min_money[guess - lower - 1][lower - 1], min_money[upper - guess - 1][guess])
                    min_cost = min(min_cost, cost)

                min_money[-1].append(min_cost)

        return min_money[n - 1][0]

_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/can-i-win/
# In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first
# causes the running total to reach or exceed 100 wins. What if we change the game so that players cannot re-use
# integers?
# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can
# force a win, assuming both players play optimally.

# Keep unused numbers in an ordered list (not a set, so can be converted to stable tuple for memo, largest can be
# identified). If for any number, opposition cannot win then can win. Memoise lists as tuples.
# Time - O(n * n!), n = maxChoosableInteger. n choices initially, n-1, n-2. Each choice takes O(n) to construct list.
# Space - O(n * n!)

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False  # all numbers cannot reduce desiredTotal to zero

        return self.next_player_win(desiredTotal, list(range(1, maxChoosableInteger + 1)), {})


    def next_player_win(self, target, unused, memo):

        if unused[-1] >= target:
            return True

        tup = tuple(unused)
        if tup in memo:
            return memo[tup]

        for i in range(len(unused) - 1, -1, -1):

            opposition_win = self.next_player_win(target - unused[i], unused[:i] + unused[i + 1:], memo)
            if not opposition_win:
                memo[tup] = True
                return True

        memo[tup] = False
        return False

_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flip-game-ii/
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters:
# + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can
# no longer make a move and therefore the other person will be the winner.
# Write a function to determine if the starting player can guarantee a win.

# Find every '++' in s and if there is no winning strategy for opponent after converting it to '--' then this is a
# winning strategy.
# Time - O(n * n!), if string contains only '+' then n - 1 choices for first pair to replace, (n - 1)(n - 3)
# for second pair .. each replacement takes O(n)
# Space - O(n * n!)

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def helper(s):

            if s in memo:
                return memo[s]

            for i in range(len(s) - 1):
                if s[i:i + 2] == '++' and not helper(s[:i] + '--' + s[i + 2:]):
                    memo[s] = True
                    return True

            memo[s] = False
            return False

        memo = {}
        return helper(s)


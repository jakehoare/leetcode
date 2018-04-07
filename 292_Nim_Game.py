_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/nim-game/
# You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of
# you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner.
# You will take the first turn to remove the stones.
# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can
# win the game given the number of stones in the heap.

# Can win if n is not divisible by 4, since then I can make it so n is divisible by 4 for my opponent. On each
# subsequent turn I will always make it so n is divisible by 4 or take the last 1, 2 or 3 stones.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
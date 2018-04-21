_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/guess-number-higher-or-lower/
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

# Binary search.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while True:

            mid = (low + high) // 2
            g = guess(mid)

            if g == -1:         # search lower region
                high = mid - 1
            elif g == 1:        # search higher region
                low = mid + 1
            else:
                return mid

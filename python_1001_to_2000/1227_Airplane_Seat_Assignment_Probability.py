_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/airplane-seat-assignment-probability/
# n passengers board an airplane with exactly n seats.
# The first passenger has lost the ticket and picks a seat randomly.
# But after that, the rest of passengers will:
# Take their own seat if it is still available,
# Pick other seats randomly when they find their seat occupied
# What is the probability that the n-th person can get his own seat?

# For n > 1, the first person chooses their own seat with probability 1 / n,
# in which case everybody gets their own seat.
# Else the next person chooses the first person's seat with probability 1 /(n - 1) and
# everybody else gets their own seat. Summing the series results in 0.5.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 1 if n == 1 else 0.5

_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/new-21-game/
# Alice plays the following game, loosely based on the card game "21".
# Alice starts with 0 points, and draws numbers while she has less than K points.
# During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.
# Each draw is independent and the outcomes have equal probabilities.
# Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

# Maintain the sum of the probabilities being at all numbers that can reach the next number. Update the next i as the
# window divided by W since each number in window has 1/W probability of moving to i. Add to window with new
# probability and remove probability from front of window.
# Time - O(N)
# Space - O(N)

class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or N >= K + W:        # no draws or every reachable number <= N
            return 1

        probability = [0] * (N + 1)
        probability[0] = 1.0
        window = 1.0                    # sum of probabilities of numbers that can reach next number

        for i in range(1, N + 1):

            probability[i] = window / W # 1 / W times the probability of each number that can reach i
            if i < K:
                window += probability[i]        # add to window
            if i - W >= 0:
                window -= probability[i - W]    # drop out from window

        return sum(probability[K:])
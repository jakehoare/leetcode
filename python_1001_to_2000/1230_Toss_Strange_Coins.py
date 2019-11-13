_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/toss-strange-coins/
# You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.
# Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.

# Dynamic programming. Given the probability of each number of heads from n - 1 tosses,
# we calculate the probability of each number of heads from n tosses.
# For each previous number of each, we can toss a head and get an additional head,
# or toss a tail and keep the same number of heads.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        probs = [1]  # probs[i] is probability of i heads, initially from 0 tosses

        for coin in prob:
            new_probs = [0] * (len(probs) + 1)
            for heads, p in enumerate(probs[:target + 1]):
                new_probs[heads] += p * (1 - coin)
                new_probs[heads + 1] += p * coin

            probs = new_probs

        return probs[target]

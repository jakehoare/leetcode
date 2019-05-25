_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/last-stone-weight-ii/
# We have a collection of rocks, each rock has a positive integer weight.
# Each turn, we choose any two rocks and smash them together.
# Suppose the stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.
# Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

# We need to partition the stones into two disjoint sets where the difference between the sums of the sets is as
# small as possible.
# Make the set of all possible sums by including or excluding each stone.
# Return the minimum of the absolute difference between any s sum and its compliment (sum(stones) - s).
# Time - O(2**n)
# Space - O(2**n)

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        all_sums = {0}

        for stone in stones:    # add stone to all previous sums, also retain all previous sums
            all_sums |= {stone + prev_sum for prev_sum in all_sums}

        return min(abs(sum(stones) - s - s) for s in all_sums)

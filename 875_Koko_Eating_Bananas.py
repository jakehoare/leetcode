_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/koko-eating-bananas/
# Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas.
# The guards have gone and will come back in H hours.
# Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas,
# and eats K bananas from that pile.
# If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
# Return the minimum integer K such that she can eat all the bananas within H hours.

# Binary search the range of possible speeds. Maximum possible rate is to eat the largest pile in an hour.
# Minimum possible rate is to eat bananas constantly, so the sum of all bananas in the total time.
# Chech the middle rate between maximum and minimum and adjust the search range until one integer remains.
# The time to eat any pile is the size of the pile / rate, rounded up to the nearest integer.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        bananas, max_pile = sum(piles), max(piles)
        min_rate = (bananas + H - 1) // H           # equivalent to ceil(bananas / H)
        max_rate = max_pile

        while min_rate < max_rate:

            rate = (min_rate + max_rate) // 2

            time = 0
            for pile in piles:
                time += (pile + rate - 1) // rate   # time to eat this pile
                if time > H:                        # stop if already taken too long
                    break

            if time > H:                            # increase minimum rate
                min_rate = rate + 1
            else:                                   # result is this rate or lower
                max_rate = rate

        return min_rate
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# A conveyor belt has packages that must be shipped from one port to another within D days.
# The i-th package on the conveyor belt has a weight of weights[i].
# Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages being shipped within D days.

# Binary search the range of possible capacities. Lowest possible capacity is the max weight of any item.
# Greatest possible capacity is the sum of all items, which can be shipped in one day.
# Time - O(n log nm) for n weights of max weight m
# Space - O(1)

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def can_ship(capacity):     # determine whether weights can be shipped given a capacity
            days = D
            load = 0

            for weight in weights:
                if weight + load > capacity:    # use a new ship
                    days -= 1
                    load = 0
                load += weight
                if days == 0:       # all days have been used and some weight remains
                    return False

            return True

        min_capacity = max(weights)
        max_capacity = sum(weights)

        while min_capacity < max_capacity:

            mid_capacity = (min_capacity + max_capacity) // 2
            if can_ship(mid_capacity):
                max_capacity = mid_capacity         # above mid_capacity is not the lowest possible capacity
            else:
                min_capacity = mid_capacity + 1     # range of capacities is above mid_capacity

        return min_capacity

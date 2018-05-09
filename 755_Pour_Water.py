_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/pour-water/
# We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each
# index is 1. After V units of water fall at index K, how much water is at each index?
# Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows
# according to the following rules:
# If the droplet would eventually fall by moving left, then move left.
# Otherwise, if the droplet would eventually fall by moving right, then move right.
# Otherwise, rise at it's current position.
# Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction.
# Also, "level" means the height of the terrain plus any water in that column.
# We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be
# partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.

# For each drop, move left until the next index is higher, recording the lowest index. If the drop has fallen, update
# heights. Else follow the same procedure on the right. If the drop has not fallen on the right, put it at index K.
# Time - O(Vn) where len(heights) == n
# Space - O(n)

class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        heights = [float("inf")] + heights + [float("inf")]     # pad before and after with infinite walls
        K += 1

        while V > 0:                                            # iterate over drops
            V -= 1

            i = K
            lowest, lowest_i = heights[K], K
            while heights[i - 1] <= lowest:                     # move left if same or lower
                i -= 1
                if heights[i] < lowest:                         # update lowest seen
                    lowest, lowest_i = heights[i], i

            if lowest < heights[K]:                             # fallen on left, no need to look right
                heights[lowest_i] += 1
                continue

            i = K
            lowest, lowest_i = heights[K], K
            while heights[i + 1] <= lowest:
                i += 1
                if heights[i] < lowest:
                    lowest, lowest_i = heights[i], i

            if lowest < heights[K]:
                heights[lowest_i] += 1
            else:
                heights[K] += 1

        return heights[1:-1]

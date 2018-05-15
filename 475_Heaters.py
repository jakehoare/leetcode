_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/heaters/
# Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm
# all the houses.
# Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that
# all houses could be covered by those heaters.
# So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum
# radius standard of heaters.

# Sort heaters and houses. Add sentinel heaters at + and - infinity. For each house, move along the heaters until the
# current heater is on the left of the house and the next heater is at or on the right of the house. One of these
# heaters is the closest to the house. Update the radius to be the max of the current radius and the closest heater.
# Time - O(m log m + n log n)
# Space - O(m) where m = len(heaters)

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]

        i = 0
        radius = -1

        for house in houses:

            while heaters[i + 1] < house:
                i += 1
            left_distance = house - heaters[i]
            right_distance = heaters[i + 1] - house         # could be zero
            closest = min(left_distance, right_distance)
            radius = max(radius, closest)

        return radius

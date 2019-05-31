_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/boats-to-save-people/
# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.
# It is guaranteed each person can be carried by a boat.

# Sort the people in weight order. Maintain 2 pointers to the lightest and heaviest people not yet allocated to a boat.
# Add the heaviest person to a boat. If the lightest person can join them without going over the weight limit, then add
# the lightest person. When the heaviest person is added to a boat, if the lightest person cannot join them then there
# is no other person that can join them and the heaviest person must be alone.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        people.sort()
        light, heavy = 0, len(people) - 1

        while light <= heavy:

            boats += 1                                  # add heaviest to a new boat

            if people[light] + people[heavy] <= limit:  # capacity for lightest and heaviest
                light += 1

            heavy -= 1

        return boats
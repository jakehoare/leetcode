_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximize-distance-to-closest-person/
# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
# Return that maximum distance to closest person.

# Iterate over seats, maintaining a list of empty seats as tuples of (index of empty seat, distance to seat on left).
# If a seat is occupied, update max_distance for each empty seat with the minimum of the distances to its left and
# right occupied seats. Else add to the list of empty seats if max_distance could be improved.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        empty_seats = []
        max_distance = 0
        last_seat = float("-inf")

        for i, seat in enumerate(seats):

            if seat == 1:                                   # occupied, update max_distance for all empty_seats
                while empty_seats:
                    seat_i, left_distance = empty_seats.pop()
                    max_distance = max(max_distance, min(left_distance, i - seat_i))
                last_seat = i

            elif i - last_seat > max_distance:              # add to empty_seats if max_distance can be improved
                empty_seats.append((i, i - last_seat))

        while empty_seats:                                  # remaining seats have no occupied seat on right
            seat_i, left_distance = empty_seats.pop()
            max_distance = max(max_distance, left_distance)

        return max_distance
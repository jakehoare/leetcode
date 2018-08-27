_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/exam-room/
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.
# If there are multiple such seats, they sit in the seat with the lowest number.
# Also, if no one is in the room, then the student sits at seat number 0.
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat
# the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.
# It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

# Maintain a sorted list of seats that are occupied. If room is empty use the first seat. Else check the distances to
# the first seat, between all pairs of seats and to the last seat. Insert in sorted order and remove to leave.
# Time - O(n) for seat() and leave()
# Space - O(n)

import bisect

class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.seats = []
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        if not self.seats:                      # empty room, use seat zero
            self.seats.append(0)
            return 0

        max_dist, index = self.seats[0], 0      # max_dist is the distance from zero to the first occupied seat

        for i in range(len(self.seats) - 1):    # each pair of occupied seats
            dist = (self.seats[i + 1] - self.seats[i]) // 2     # best case distance
            if dist > max_dist:                 # improved best case
                max_dist = dist
                index = self.seats[i] + dist

        if self.N - 1 - self.seats[-1] > max_dist:  # put in last seat if further distance
            index = self.N - 1

        bisect.insort(self.seats, index)        # insert seat in order
        return index

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.seats.remove(p)
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/self-crossing/
# You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north,
# then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on.
# In other words, after each move your direction changes counter-clockwise.

# There are 3 scenarios for a crossing (described from the perspective of the first move m0 being vertically up),
# 1) After 4 moves. Down move m2 <= up move m0 and left move m3 >= right move m1.
# 2) After 5 moves. Left move m1 == right move m3 and final up move m4 >= distance to start m2 - m0.
# 3) After 6 moves. Final up move m4 <= previous down move m2 and also >= distance to start m2 - m0.  Final right move
# m5 >= previous left move m3 and also left move m3 > right move m1 and final right move m5 >= distance to
# start m3 - m1.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        for i in range(len(x)):
            # assume staring with verical move up
            if i >= 3:
                # move down <= move up and move left >= move right
                if x[i - 1] <= x[i - 3] and x[i] >= x[i - 2]:
                    return True
            if i >= 4:
                # move right equal to move left and last move up >= vertical distance from start
                if x[i - 1] == x[i - 3] and x[i] >= x[i - 2] - x[i - 4]:
                    return True
            if i >= 5:
                # final move right >= horizontal distance to start and left move > first right move and
                # final vertical move >= vertical distance to start but also <= down move
                if x[i] >= x[i - 2] - x[i - 4] and x[i - 2] > x[i - 4] and x[i - 3] - x[i - 5] <= x[i - 1] <= x[i - 3]:
                    return True

        return False

_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reaching-points/
# A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
# Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves
# exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
# sx, sy, tx, ty will all be integers in the range [1, 10^9].

# Move back from tx, ty since there can be only one valid step (because sx and sy are both positive). In the other
# direction from sx, sy there are 2 possible moves. While both tx and ty are more than sx and sy respectively, subtract
# either ty from ty or ty from tx. Do this as many times as possible in one step with the modulo operator.
# When either tx <= sx or ty <= sy, check if tx == sx and ty can reach sy by taking steps of sx (or vica versa).
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > sx and ty > sy:
            tx, ty = tx % ty, ty % tx           # either tx % ty ==

        if tx == sx and (ty - sy) % sx == 0:
            return True
        return ty == sy and (tx - sx) % sy == 0
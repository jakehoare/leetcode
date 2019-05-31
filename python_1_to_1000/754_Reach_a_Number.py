_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reach-a-number/
# You are standing at position 0 on an infinite number line. There is a goal at position target.
# On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
# Return the minimum number of steps required to reach the destination.

# Take steps until we reach or go past target. position = steps * (steps + 1) // 2. Invert this and solve quadratic
# polynomial to find the number of steps to reach or exceed position. If we are at exact target or an even number
# of steps away then can reach target by inverting the sign of some moves. Else take one or two more steps until we
# are an even number of moves from target.
# Time - O(1)
# Space - O(1)

import math

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)  # symmetry of positive and negative solutions

        steps = int(math.ceil((math.sqrt(1 + 8 * target) - 1) / 2)) # ceil to round up
        target -= steps * (steps + 1) // 2                          # find remaining distance after steps

        if target % 2 == 0:  # includes target == 0
            return steps

        target += steps + 1  # take one more step
        if target % 2 == 0:
            return steps + 1

        return steps + 2    # take one more step, must now be an even distance from target

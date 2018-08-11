_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/race-car/
# Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)
# Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).
# When you get an instruction "A", your car does the following: position += speed, speed *= 2.
# When you get an instruction "R", your car does the following: if your speed is positive then speed = -1,
# otherwise speed = 1.  (Your position stays the same.)
# For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.
# Now for some target position, say the length of the shortest sequence of instructions to get there.

# After k steps of acceleration, we have travelled 2 ** k - 1 distance. Find k such that distance >= target,
# this is the number of bits used in target.
# If this distance reaches the target exactly, we cannot do better. Else we either go past the target, reverse and
# recurse for the remaining distance having already moved k + 1 steps, or reverse after k - 1 steps then accelerate
# for j steps before reversing again. Memoize results to avoid repetition.
# Time - O(n log n) since each distance up to n may be calculated, each taking log n to iterate over j
# Space - O(n)

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        min_steps = {0: 0}          # map distance to min steps

        def helper(dist):

            if dist in min_steps:
                return min_steps[dist]

            k = dist.bit_length()
            if 2 ** k - 1 == dist:                          # k steps reaches target exactly
                return k

            steps = k + 1 + helper(2 ** k - 1 - dist)       # k steps goes past target, reverse and recurse
            for j in range(k - 1):                          # k - 1 steps, reverse, j steps of acceleration and reverse
                steps = min(steps, k + j + 1 + helper(dist - 2 ** (k - 1) + 2 ** j))

            min_steps[dist] = steps
            return steps

        return helper(target)
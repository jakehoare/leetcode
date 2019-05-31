_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/elimination-game/
# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other
# number afterward until you reach the end of the list.  Repeat the previous step again, but this time from right to
# left, remove the right most number and every other number from the remaining numbers.
# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
# Find the last number that remains starting with a list of length n.

# Track the first remaining number until only 1 number is left.  On left to right passes, head moves by step.  On right
# to left passes, head moves by step only if an odd number remain else head stays.  Step doubles and remaining halves
# every pass.
# Time - O(log n), half remaining each pass
# Space - O(1)

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1        # first remaining number
        l_to_r = True   # direction of next movement
        step = 1        # numbers jumped over in each move

        while n > 1:    # remaining live numbers

            if l_to_r:
                head += step
            else:       # head only moves if odd number remaining
                if n % 2 != 0:
                    head += step

            step *= 2
            n //= 2     # reduce by half, +1 if n is odd
            l_to_r = not l_to_r

        return head

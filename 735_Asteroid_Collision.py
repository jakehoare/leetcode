_author_ = 'jake'
_project_ = 'leetcode'


# https://leetcode.com/problems/asteroid-collision/
# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
# right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Stack consists of a stable configuration of asteroids. For each new asteroid add to stack if no collision. Else
# determine which to destroy. If top of stack is destroyed then repeat.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:

            while stack and stack[-1] > 0 > asteroid:  # collision

                if stack[-1] == -asteroid:      # destroy both
                    stack.pop()
                    break
                elif stack[-1] > -asteroid:     # destroy asteroid
                    break
                else:                           # destroy top of stack
                    stack.pop()

            else:  # no collision between asteroid and top of stack
                stack.append(asteroid)

        return stack
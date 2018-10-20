_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/super-egg-drop/
# You are given K eggs, and you have access to a building with N floors from 1 to N.
# Each egg is identical in function, and if an egg breaks, you cannot drop it again.
# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break,
# and any egg dropped at or below floor F will not break.
# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N).
# Your goal is to know with certainty what the value of F is.
# What is the minimum number of moves that you need to know with certainty what F is,
# regardless of the initial value of F?

# If we know the maximum height of building for which we can learn the highest floor that an egg can be dropped from
# without breaking for a certain number of drops (d) and a certain number of eggs (e). Call this f(d, e).
# We also know the same result for the same number of drops and one fewer egg = f(d, e - 1).
# Now we take an additional drop from floor f(d, e - 1) + 1.
# If it breaks, we know that we can find the result with one less egg f(d, e - 1).
# If it doesn't break, we can explore the f(d, e) floors above the one we just dropped from.
# So we can get the result for a building of height 1 + f(d, e - 1) + f(d, e).

# Time - O(K log N) since floors[K] grows exponentially with each drop.
# Space - O(K)

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        drops = 0
        floors = [0 for _ in range(K + 1)]  # floors[i] is the number of floors that can be checked with i eggs

        while floors[K] < N:

            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1

        return drops
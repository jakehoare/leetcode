_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/dungeon-game/
# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
# The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the princess.
# The knight has an initial health point represented by a positive integer. If at any point his health point drops
# to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
# other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
# In order to reach the princess as quickly as possible, the knight moves only rightward or downward in each step.
# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

# Dynamic programming.  Min health to reach end from any room is health lost/gained in that room + min required
# after moving down or right, floored at 1 since health cannot be zero.
# Time - O(n * m)
# Space - O(n + m)

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])

        for r in range(rows - 1):       # add new final column and row of infinity
            dungeon[r].append(float('inf'))
        dungeon.append([float('inf') for _ in range(cols + 1)])

        dungeon[rows - 1].append(1)     # final room requires min health of 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                dungeon[r][c] = max(1, -dungeon[r][c] + min(dungeon[r+1][c], dungeon[r][c+1]))

        return dungeon[0][0]

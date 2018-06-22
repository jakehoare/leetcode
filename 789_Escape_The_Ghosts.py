_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/escape-the-ghosts/
# You are playing a simplified Pacman game. You start at the point (0, 0), and your destination is
# (target[0], target[1]). There are several ghosts on the map, the i-th ghost starts at (ghosts[i][0], ghosts[i][1]).
# Each turn, you and all ghosts simultaneously *may* move in one of 4 cardinal directions: north, east, west, or south,
# going from the previous point to a new point 1 unit of distance away.
# You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts
# may take.) If you reach any square (including the target) at the same time as a ghost, it doesn't count as an escape.
# Return True if and only if it is possible to escape.

# If any ghost can reach the target before or at the same time as pacman then no escape is possible.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def manhattan(position):
            return abs(position[0] - target[0]) + abs(position[1] - target[1])

        target_distance = manhattan((0, 0))

        return all(manhattan(ghost) > target_distance for ghost in ghosts)
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
# Storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.
# The game is represented by a grid of size n*m, where each element is a wall, floor, or a box.
# Your task is move the box 'B' to the target position 'T' under the following rules:
# Player is represented by character 'S' and can move up, down, left, right in the grid if it is a floor (empty cell).
# Floor is represented by character '.' that means free cell to walk.
# Wall is represented by character '#' that means obstacle  (impossible to walk there).
# There is only one box 'B' and one target cell 'T' in the grid.
# The box can be moved to an adjacent free cell by standing next to the box and
# then moving in the direction of the box. This is a push.
# The player cannot walk through the box.
# Return the minimum number of pushes to move the box to the target.
# If there is no way to reach the target, return -1.

# A-star search.
# Maintain a heap of states where a state consists of box and person locations together.
# Heap is ordered by the number of moves so far to reach a state + heuristic estimate of remaining moves.
# Heuristic (an under-estimate of the remaining moves required) is the Manhattan distance between box and target.
# Repeatedly pop the state with the lowest heuristic + previous moves off the heap.
# Attempt to move the person in all 4 directions.
# If any direction moves the person to the box, check if the box can move to the next position in the grid.
# Time - O(log(mn) * m**2 * n**2) since there are m**2 * n**2 states.
# Space - O(m**2 * n**2)

import heapq

class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "T":
                    target = (r, c)
                if grid[r][c] == "B":
                    start_box = (r, c)
                if grid[r][c] == "S":
                    start_person = (r, c)

        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])

        def out_bounds(location):  # return whether the location is in the grid and not a wall
            r, c = location
            if r < 0 or r >= rows:
                return True
            if c < 0 or c >= cols:
                return True
            return grid[r][c] == "#"

        heap = [[heuristic(start_box), 0, start_person, start_box]]
        visited = set()

        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves
            if (person, box) in visited:  # do not visit same state again
                continue
            visited.add((person, box))

            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_person = (person[0] + dr, person[1] + dc)
                if out_bounds(new_person):
                    continue

                if new_person == box:
                    new_box = (box[0] + dr, box[1] + dc)
                    if out_bounds(new_box):
                        continue
                    heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box])  # box remains same

        return -1
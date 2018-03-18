_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/cut-off-trees-for-golf-event/
# You are asked to cut off trees in a forest for a golf event.
# The forest is represented as a non-negative 2D map, in this map:
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents
# the tree's height.
# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with
# lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all
# the trees. If you can't cut off all the trees, output -1 in that situation.
# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

# Find all trees and sort in increasing height order. DFS from (0, 0) to check all treas can be reached.
# Sum distances between trees by attempting to take the most direct path. Any node that is not closer to destination
# is added to next_queue and is used once queue is exhausted. The number of diversions increases until a path is found.
# Time - O(m**2 n**2) since mn maximum number of trees and each path explores all mn calls.
# Space - O(mn)

class Solution(object):
    def cutOffTree(self, forest):

        rows, cols = len(forest), len(forest[0])
        trees = sorted((h, r, c) for r, row in enumerate(forest)    # trees sorted by increasing height
                       for c, h in enumerate(row) if h > 1)

        to_visit = set((r, c) for _, r, c in trees)                 # check if all trees can be reached
        visited = set()
        queue = [(0, 0)]

        while queue:
            r, c = queue.pop()
            to_visit.discard((r, c))
            visited.add((r, c))
            for r1, c1 in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                # add to queue all neighbours within grid, not obstacles and have not visited already
                if 0 <= r1 < rows and 0 <= c1 < cols and forest[r1][c1] and (r1, c1) not in visited:
                    queue.append((r1, c1))

        if to_visit:            # cannot reach all trees
            return -1

        def distance(r1, c1, r2, c2):

            direct = abs(r1 - r2) + abs(c1 - c2)  # manhattan distance
            diversions = 0
            queue = [(r1, c1)]  # cells on paths with current number of diversions
            next_queue = []     # cells on paths with next number of diversions
            visited = set()

            while True:

                if not queue:  # cannot reach r2, c2 on path with current diversions
                    queue, next_queue = next_queue, []  # try paths with next number of diversions
                    diversions += 1

                r1, c1 = queue.pop()
                if (r1, c1) == (r2, c2):  # reached destination
                    return direct + diversions * 2  # for every diversion, must take a step back in correct direction

                if (r1, c1) in visited:
                    continue
                visited.add((r1, c1))

                for r1, c1, closer in (r1 + 1, c1, r1 < r2), (r1 - 1, c1, r1 > r2), (r1, c1 + 1, c1 < c2), (
                r1, c1 - 1, c1 > c2):
                    if 0 <= r1 < rows and 0 <= c1 < cols and forest[r1][c1]:
                        (queue if closer else next_queue).append((r1, c1))

        result = 0
        r1, c1 = 0, 0                               # starting location
        for _, r2, c2 in trees:
            result += distance(r1, c1, r2, c2)      # add distance between trees to result
            r1, c1 = r2, c2                         # set next starting location

        return result
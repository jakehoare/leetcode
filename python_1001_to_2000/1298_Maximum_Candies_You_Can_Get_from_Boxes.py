_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
# Given n boxes, each box is given in the format [status, candies, keys, containedBoxes] where:
# status[i]: an integer which is 1 if box[i] is open and 0 if box[i] is closed.
# candies[i]: an integer representing the number of candies in box[i].
# keys[i]: an array contains the indices of the boxes you can open with the key in box[i].
# containedBoxes[i]: an array contains the indices of the boxes found in box[i].
# You will start with some boxes given in initialBoxes array.
# You can take all the candies in any open box and you can use the keys in it to
# open new boxes and you also can use the boxes you find in it.
# Return the maximum number of candies you can get following the rules above.

# Breadth first search.
# Maintain sets of all open and unopened boxes reached.
# For each opened box in each round, take all candies, use keys to open all boxes and update set of unopened boxes.
# After visiting each opened box, update the opened boxes.
# Time - O(n + m) for n boxes and m total keys (same key may be in multiple boxes).
# Space - O(n)

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        OPEN, VISITED = 1, 2

        result = 0
        open_boxes, closed_boxes = set(), set()
        for initial_box in initialBoxes:     # put in either opened or unopened set
            container = open_boxes if status[initial_box] == OPEN else closed_boxes
            container.add(initial_box)

        while open_boxes:

            for open_box in open_boxes:
                if status[open_box] == VISITED:     # avoid re-vistiing
                    continue
                status[open_box] = VISITED

                result += candies[open_box]
                for key in keys[open_box]:          # open when box is reached, no need to retain key
                    status[key] = OPEN
                closed_boxes.update(containedBoxes[open_box])

            open_boxes = {box for box in closed_boxes if status[box] == OPEN}
            closed_boxes -= open_boxes

        return result



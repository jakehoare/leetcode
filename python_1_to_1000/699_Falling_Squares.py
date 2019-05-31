_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/falling-squares/
# On an infinite number line (x-axis), we drop given squares in the order they are given.
# The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being
# positions[i][0] and sidelength positions[i][1].
# The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently
# landed squares. We wait for each square to stick before dropping the next.
# The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they
# touch (either the number line or another square). Squares dropped adjacent to each other will not stick together
# prematurely.
# Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have
# dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].

# For each box, check for overlap with each box already dropped. If overlap update top of box as side length + top of
# overlapping box.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        box_heights = [positions[0][1]]  # top edge height of dropped boxes
        max_heights = [positions[0][1]]

        for left, side in positions[1:]:
            top = side  # default to on ground, top of box is side length

            for i in range(len(box_heights)):  # loop over each previously dropped box
                left2, side2 = positions[i]
                if left2 < left + side and left2 + side2 > left:  # horizontal overlap
                    top = max(top, box_heights[i] + side)  # on previous box

            box_heights.append(top)
            max_heights.append(max(top, max_heights[-1]))

        return max_heights
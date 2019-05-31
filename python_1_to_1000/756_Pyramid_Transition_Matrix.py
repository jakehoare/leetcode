_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/pyramid-transition-matrix/
# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.
# For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A`
# and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.
# We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples
# allowed. Each allowed triple is represented as a string of length 3.
# Return true if we can build the pyramid all the way to the top, otherwise false.

# Create a mapping from a pair of blocks to a list allowed blocks on top. Then depth-first search for the next block.
# If a completed row has one block, we have found the top of the pyramid. If a row has one less block than the previous
# row then start the next row. Else find a list of possible next blocks. If there are none then we cannot find any
# solution. If any of the next blocks allows us to fill the pyramid then there is a solution, else there is not.
# Time - O(k ** (n**2)) where k is the size of the alphabet and n == len(bottom). There are O(n**2) blocks to be added.
# Space - O(n**2)

from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        triangles = defaultdict(list)
        for triple in allowed:
            triangles[triple[:-1]].append(triple[-1])

        def helper(prev, current):          # inputs are the previous row and the (partial) current row

            if len(prev) == 1:              # finished pyramid
                return True
            n = len(current)
            if n == len(prev) - 1:          # start a new row
                return helper(current, "")

            colours = triangles[prev[n:n + 2]]  # allowed next blocks
            if not colours:
                return False

            for colour in colours:
                if helper(prev, current + colour):
                    return True
            return False

        return helper(bottom, "")
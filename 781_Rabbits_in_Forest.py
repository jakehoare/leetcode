_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rabbits-in-forest/
# In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other
# rabbits have the same color as them. Those answers are placed in an array.
# Return the minimum number of rabbits that could be in the forest.

# Maintain a mapping for each colour (an integer) to the number of as yet unseen rabbits with that colour. If a rabbit
# has as many other rabbits as another rabbit already seen, then decrement the unseen count. Else increase the total
# count for the new colour by the rabbit plus all others.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        colours = {}                            # map colour to number of unseen rabbits of that colour
        rabbits = 0

        for rabbit in answers:

            if colours.get(rabbit, 0) > 0:      # default 0 if a new colour
                colours[rabbit] -= 1
            else:
                rabbits += rabbit + 1           # new colour
                colours[rabbit] = rabbit

        return rabbits
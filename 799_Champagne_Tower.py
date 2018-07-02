_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/champagne-tower/
# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses,
# and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.
# Then, some champagne is poured in the first glass at the top.  When the top most glass is full, any excess liquid
# poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full,
# any excess champagne will fall equally to the left and right of those glasses, and so on.
# A glass at the bottom row has it's excess champagne fall on the floor.
# Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is
# (both i and j are 0 indexed.)

# Calculate the volume of champagne that is added to each glass. For each glass in the current row, subtract 1 glass
# which is the champagne that remains and divid the remainder by the 2 glasses below (floored at zero).
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        glasses = [poured]

        for row in range(query_row):

            new_glasses = [0 for _ in range(len(glasses) + 1)]

            for i, glass in enumerate(glasses):
                pour = max(glass - 1, 0) / 2.0
                new_glasses[i] += pour
                new_glasses[i + 1] += pour

            glasses = new_glasses

        return min(glasses[query_glass], 1)
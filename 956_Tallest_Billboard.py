_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/tallest-billboard/
# You are installing a billboard and want it to have the largest height.
# The billboard will have two steel supports, one on each side. Each steel support must be an equal height.
# You have a collection of rods which can be welded together.
# For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.
# Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.

# Maintain a dictionary mapping the difference in side heights to the greatest total length used with that difference.
# Use only non-negative differences.
# For each rod, update each height difference by both adding and subtracting the rod.
# Return the greatest total length used with a difference of zero.
# Time - O(2 ** n) since 2 ** (n - 1) possible diffs.
# Space - O(2 ** (n - 1))

from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        diffs = {0 : 0}     # key is difference, value is max total length

        for rod in rods:

            new_diffs = defaultdict(int, diffs)

            for diff, used_len in diffs.items():

                new_diffs[diff + rod] = max(used_len + rod, new_diffs[diff + rod])
                new_diffs[abs(diff - rod)] = max(used_len + rod, new_diffs[abs(diff - rod)])

            diffs = new_diffs

        return diffs[0] // 2
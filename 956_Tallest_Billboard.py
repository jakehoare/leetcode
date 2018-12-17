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
# When there is a difference of zero, we have a possible solution.
# Time - O(2 ** n) since 2 ** (n - 1) possible diffs.
# Space - O(2 ** (n - 1))

class Solution:
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        best = 0        # best total length for both sides of equal height
        diffs = {}      # map difference in side lengths to total length used

        for rod in rods:

            new_diffs = dict(diffs)
            if rod not in new_diffs or rod > new_diffs[rod]:        # add the rod as a single side to the dictionary
                new_diffs[rod] = rod

            for diff, used_len in diffs.items():

                if diff + rod not in new_diffs or used_len + rod > new_diffs[diff + rod]:
                    new_diffs[diff + rod] = used_len + rod          # better total length used for diff + rod

                if abs(diff - rod) not in new_diffs or used_len + rod > new_diffs[abs(diff - rod)]:
                    new_diffs[abs(diff - rod)] = used_len + rod     # better total length for abs(diff - rod)

            diffs = new_diffs
            if 0 in diffs:      # sides are balanced
                best = max(best, diffs[0])

        return best // 2
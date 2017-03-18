_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/russian-doll-envelopes/
# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit
# into another if and only if both the width and height of one envelope is greater than the width and height of the
# other envelope.  What is the maximum number of envelopes can you Russian doll? (put one inside other)

# Create nested envelopes by wrapping larger ones around smaller.  Sort by increasing width, with ties broken by
# decreasing height.  If widths are unique then when envelopes are considered in order we can always wrap the
# next envelope around any previous in the width dimension.  If widths are same then largest height first ensures we
# do not put same width envelopes inside each other.
# Maintain a list of the smallest outer envelope height for each number of nested envelopes.  For each envelope find the
# longest nested list that can be extended.  Update the best extended list with the new envelope if it has smaller
# height, or make a new longest list.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # increasing width, ties broken by decreasing height
        envelopes.sort(key = lambda x : (x[0], -x[1]))

        # nested[i] is smallest height outer envelope for i - 1 in total
        nested = []

        # find the index of the first number in nested >= target
        # i.e. the first nested that can be improved (or stay same) by target
        # i.e. index after last nested than target can increase
        def bin_search(target):
            left, right = 0, len(nested) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > nested[mid]:    # first greater than target must be on RHS
                    left = mid + 1
                else:               # target <= nested[mid], target cannot fit around nested[mid] so look st LHS
                    right = mid - 1
            return left

        for _, h in envelopes:
            i = bin_search(h)
            if i == len(nested):
                nested.append(h)
            else:
                nested[i] = h       # h <= nested[i] so nested[i] can only improve

        return len(nested)


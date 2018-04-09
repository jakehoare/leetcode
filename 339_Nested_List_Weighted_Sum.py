_author_ = 'jake'
_project_ = 'leetcode'


# https://leetcode.com/problems/nested-list-weight-sum/
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Iterate over the nestedList. If an element isInteger, add it to the total multiplied by its depth. Else increment
# the depth and recurse to sum the deeper list.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def helper(nested, depth):

            total = 0
            for item in nested:

                if item.isInteger():
                    total += depth * item.getInteger()
                else:
                    total += helper(item.getList(), depth + 1)

            return total

        return helper(nestedList, 1)
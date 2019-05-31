_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flatten-nested-list-iterator/
# Given a nested list of integers, implement an iterator to flatten it.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Recursively flatten the list.  If isInteger() then append that integer to the list, else depth first search.
# Time - O(n) to initialise, O(1) for next() and hasNext()
# Space - O(n)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flat = []
        def flatten(nested):
            for n in nested:
                if n.isInteger():
                    self.flat.append(n.getInteger())
                else:
                    flatten(n.getList())
        flatten(nestedList)
        self.flat = self.flat[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.flat.pop()


    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.flat)

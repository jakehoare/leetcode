_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a
# list of disjoint intervals in order of interval starting value.

# Create a wrapper class for interval that adds a parent attribute.  For each number map it to an IntervalNode which
# may itself be mapped to further IntervalNodes in a tree.  Separately track all ultimate intervals in a set.
# When a new value is added, check for integers above and below for their ultimate parent intervals.  Collapsing the
# tree in a union-find structure.  If only one is found, update that interval with the new value.
# If both are found, update the lower interval to merge them, remove the upper interval and update the parent of the
# upper IntervalNode to the lower IntervalNode.
# Alternatively store intervals as an sorted list with O(n) to insert then sort then O(1) to getIntervals().
# Alternatively store vals as an unsorted list then sort the list and merge to form intervals in getIntervals().
# Alternatively, use BST.
# Time - O(log*n) to find parent,  O(n log n) to sort intervals
# Space - O(n)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class IntervalNode(object):
    def __init__(self, interval):
        self.inner = interval
        self.parent = self

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.parents = {}           # mapping from val to its IntervalNode
        self.intervals = set()      # all intervals that have not been joined

    def get_parent(self, v):
        if v not in self.parents:
            return None
        interval_node = self.parents[v]
        while interval_node != interval_node.parent:
            interval_node.parent = interval_node.parent.parent
            interval_node = interval_node.parent
        return interval_node

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.parents:             # already seen val, ignore
            return

        lower = self.get_parent(val - 1)
        upper = self.get_parent(val + 1)

        if lower and upper:                 # update lower, remove upper
            lower.inner.end = upper.inner.end
            self.parents[val] = lower
            upper.parent = lower
            self.intervals.remove(upper.inner)

        elif lower:
            lower.inner.end += 1
            self.parents[val] = lower

        elif upper:
            upper.inner.start -= 1
            self.parents[val] = upper

        else:
            new_inner = Interval(val, val)
            self.parents[val] = IntervalNode(new_inner)
            self.intervals.add(new_inner)


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = list(self.intervals)
        result.sort(key = lambda x : x.start)
        return result
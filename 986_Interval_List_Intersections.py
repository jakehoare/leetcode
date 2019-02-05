_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/interval-list-intersections/
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that is either empty,
# or can be represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# Maintain pointers to the next indices of A and B to be checked for overlap.
# Indices overlap if the greatest starting edge is before or equal to the least ending edge.
# Move the pointer past the interval with the lowest ending edge to the next interval in that list.
# Time - O(m + n)
# Space - O(m + n), every interval overlaps at both ends

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        i, j = 0, 0                         # next indices of A and B to be tested

        while i < len(A) and j < len(B):

            last_start = max(A[i].start, B[j].start)
            first_end = min(A[i].end, B[j].end)
            if last_start <= first_end:     # no overlap if max start is after first end
                result.append(Interval(s=last_start, e=first_end))

            if A[i].end < B[j].end:         # move past interval that ends first
                i += 1
            else:
                j += 1

        return result

_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/odd-even-jump/
# You are given an integer array A.  From some starting index, you can make a series of jumps.
# The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in
# the series are called even numbered jumps.
#
# You may from index i jump forward to index j (with i < j) in the following way:
# During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the
# smallest possible value. If there are multiple such indexes j, you can only jump to the smallest such index j.
# During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the
# largest possible value. If there are multiple such indexes j, you can only jump to the smallest such index j.
# (It may be the case that for some index i, there are no legal jumps.)
# A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by
# jumping some number of times (possibly 0 or more than once.)
# Return the number of good starting indexes.

# Create lists of the next smaller and the next larger element from each element of the array.
# Lists are made by sorting the indices of A in ascending and descending order of the values. Indices are popped from
# a stack when a next smaller or larger element is found.
# Then iterate backwards over A, when an index has a next larger element, we can make an odd jump to the next larger
# element and reach the end if we can make an even jump from there.
# Time - O(n log n)
# Space - O(n)

class Solution:
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)

        def next_list():                                # returns list of index next larger or smaller element
            result = [None] * n
            stack = []
            for i in indices:
                while stack and i > stack[-1]:          # i is after top of stack
                    result[stack.pop()] = i             # i is index of next larger or smaller element after stack top
                stack.append(i)
            return result

        indices = sorted(range(n), key=lambda x: A[x])  # sort indices of A by increasing A[x]
        next_larger = next_list()
        indices.sort(key=lambda x: -A[x])               # sort indices of A by decreasing A[x]
        next_smaller = next_list()

        odd = [False] * (n - 1) + [True]                # default can reach the end only from last element
        even = [False] * (n - 1) + [True]

        for i in range(n - 2, -1, -1):                  # iterate form back to front
            if next_larger[i] is not None:
                odd[i] = even[next_larger[i]]
            if next_smaller[i] is not None:
                even[i] = odd[next_smaller[i]]

        return sum(odd)                                 # count of odd indices that can reach end

_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/h-index-ii/
# Follow up for 274_H-Index: What if the citations array is sorted in ascending order?

# Binary search.  If the number of citations of the paper at index mid is at least the count of papers with
# a smaller or equal number of citations then search on the left, else search right.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2

            if citations[mid] >= n-mid:
                right = mid - 1
            else:
                left = mid + 1

        return n-left